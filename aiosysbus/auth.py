"""API Access for livebox."""

from __future__ import annotations

import asyncio
import logging
import socket
from typing import Any

from aiohttp import ClientError, ClientResponse, ClientSession
from yarl import URL

from .exceptions import (
    AuthenticationFailed,
    HttpRequestFailed,
    RetrieveFailed,
    TimeoutExceededError,
    UnexpectedResponse,
)

_LOGGER = logging.getLogger(__name__)
MAX_RETRY = 5
CONTENT_TYPES = [
    "application/x-sah-ws-1-call+json",
    "application/x-sah-ws-1-call+json; charset=UTF-8",
    "application/json",
    "application/json; charset=UTF-8",
]


class IgnoreIllegalKeyFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        return not (
            message.startswith("Can not load response cookies: Illegal key '")
            and message.endswith(("/accept-language'", "/sessid'"))
        )


client_logger = logging.getLogger("aiohttp.client")
client_logger.addFilter(IgnoreIllegalKeyFilter())


class Auth:
    """Class to make authenticated requests."""

    def __init__(
        self,
        session: ClientSession,
        base_url: URL,
        username: str,
        password: str,
        timeout: int,
        verify_tls: bool,
    ) -> None:
        """Init class."""
        self.session = session
        self.base_url = base_url
        self.username = username
        self.password = password
        self.timeout = timeout
        self.verify_tls = verify_tls

        self.session_token: str | None = None
        self.session_permissions: str | None = None
        self.retry = MAX_RETRY

        self._cookies: dict[str, str] = {}

    async def async_request(
        self, method: str, json: dict[str, Any] | None = None
    ) -> Any:
        """Make a request."""
        if not self.session_token:
            await self._async_refresh_session_token()

        headers = {
            "X-Context": self.session_token,
            "Content-Type": "application/x-sah-ws-1-call+json; charset=UTF-8",
        }
        if self._cookies:
            headers["Cookie"] = ";".join(
                f"{key}={value}" for key, value in self._cookies.items()
            )

        try:
            _LOGGER.debug("METHOD:%s URL:%s", method, self.base_url)
            _LOGGER.debug("DATA:%s", json)
            async with asyncio.timeout(self.timeout):
                response = await self.session.request(
                    method,
                    self.base_url,
                    json=json,
                    headers=headers,
                    verify_ssl=self.verify_tls,
                )
        except (TimeoutError, asyncio.CancelledError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to Livebox"
            ) from error
        except (ClientError, socket.gaierror) as error:
            raise HttpRequestFailed(
                "Error occurred while communicating with Livebox"
            ) from error

        self._parse_cookies(response)

        content_type = response.headers.get("Content-Type", "")
        if (response.status // 100) in [4, 5]:
            if content_type in CONTENT_TYPES:
                result: dict[str, Any] = await response.json()
                response.close()
                raise HttpRequestFailed(result)

            result = await response.read()
            response.close()
            raise HttpRequestFailed(result)

        if content_type not in CONTENT_TYPES:
            result = await response.text()
            msg = f"Unexpected response, content-type incorrect ({content_type})"
            raise UnexpectedResponse(msg)

        rjson = await response.json()
        result = rjson.get("result", {})
        if error_msg := result.get("errors"):
            self.retry -= 1
            if self.retry > 0:
                _LOGGER.debug("Retrying (%s) request..", self.retry)
                await self._async_refresh_session_token()
                return await self.async_request(method, json)
            raise RetrieveFailed(error_msg)

        self.retry = MAX_RETRY
        _LOGGER.debug("RESPONSE: %s", result)
        return result

    async def post(
        self, service: str, method: str, params: dict[str, Any] | None = None
    ) -> Any:
        """Send post request and return results."""
        data = {"service": service, "method": method, "parameters": params}
        return await self.async_request(method="post", json=data)

    async def async_logout(self) -> bool:
        """Release the session context on the livebox.

        Sends the same request as the web interface when logging out.
        The livebox accepts a limited number of contexts, so a context that is
        not released stays allocated until it expires.
        Returns True when the livebox confirms the release, False otherwise.
        The local session is cleared in any case.
        """
        if not self.session_token:
            return False

        headers = {
            "Content-Type": "application/x-sah-ws-1-call+json",
            "Authorization": f"X-Sah-Logout {self.session_token}",
        }
        if self._cookies:
            headers["Cookie"] = ";".join(
                f"{key}={value}" for key, value in self._cookies.items()
            )

        json = {
            "service": "sah.Device.Information",
            "method": "releaseContext",
            "parameters": {"applicationName": "so_sdkut"},
        }

        try:
            async with asyncio.timeout(self.timeout):
                response = await self.session.request(
                    method="post",
                    url=self.base_url,
                    json=json,
                    headers=headers,
                    verify_ssl=self.verify_tls,
                )
            if response.status != 200:
                _LOGGER.debug("Logout failed (HTTP status %s)", response.status)
                response.close()
                return False

            rjson = await response.json(content_type=None)
        except (TimeoutError, asyncio.CancelledError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to Livebox."
            ) from error
        except (ClientError, socket.gaierror) as error:
            raise HttpRequestFailed(
                "Error occurred while communicating with Livebox."
            ) from error
        except ValueError:
            _LOGGER.debug("Logout failed (invalid response)")
            return False
        finally:
            self._clear_session()

        if isinstance(rjson, dict) and rjson.get("status") == 0:
            _LOGGER.debug("Session context released")
            return True

        _LOGGER.debug("Logout failed (APIResponse: %s)", rjson)
        return False

    def _clear_session(self) -> None:
        """Forget the current session."""
        self.session_token = None
        self.session_permissions = None
        self._cookies = {}

    async def _async_refresh_session_token(self) -> None:
        """Refresh token."""
        session_token, session_permissions = await self.async_get_session_token()
        self.session_token = session_token
        self.session_permissions = session_permissions

    async def async_get_session_token(self) -> tuple[str | None, str | None]:
        """Get session token from livebox.

        Returns (session_token, session_permissions)
        """
        # Get challenge from API
        await self._async_get_challenge(self.base_url)

        headers = {
            "Content-Type": "application/x-sah-ws-1-call+json",
            "Authorization": "X-Sah-Login",
        }
        if self._cookies:
            headers["Cookie"] = ";".join(
                f"{key}:{value}" for key, value in self._cookies.items()
            )

        json = {
            "service": "sah.Device.Information",
            "method": "createContext",
            "parameters": {
                "applicationName": "so_sdkut",
                "username": self.username,
                "password": self.password,
            },
        }

        try:
            async with asyncio.timeout(self.timeout):
                response = await self.session.request(
                    method="post", url=self.base_url, json=json, headers=headers
                )
        except (TimeoutError, asyncio.CancelledError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to Livebox."
            ) from error
        except (ClientError, socket.gaierror) as error:
            raise HttpRequestFailed(
                "Error occurred while communicating with Livebox."
            ) from error

        self._parse_cookies(response)
        content_type = response.headers.get("Content-Type", "")
        if content_type not in CONTENT_TYPES:
            raise UnexpectedResponse(
                f"Unexpected response, content-type incorrect {content_type}"
            )

        if (response.status // 100) in [4, 5]:
            if content_type in CONTENT_TYPES:
                result = await response.json()
                response.close()
                raise HttpRequestFailed(result)

            result = await response.read()
            response.close()
            raise HttpRequestFailed(result)

        rjson = await response.json()
        if not rjson.get("data"):
            raise AuthenticationFailed(
                f"Starting session failed (APIResponse: {rjson})"
            )

        session_token = rjson.get("data").get("contextID")
        session_permissions = rjson.get("data").get("groups")
        _LOGGER.debug("Token %s", session_token)
        return (session_token, session_permissions)

    async def _async_get_challenge(self, base_url: URL) -> None:
        """Return challenge from livebox API."""
        try:
            async with asyncio.timeout(self.timeout):
                response = await self.session.request(method="get", url=base_url.parent)
        except (
            TimeoutError,
            asyncio.CancelledError,
            ClientError,
            socket.gaierror,
        ) as error:
            raise HttpRequestFailed(
                "An error occurred while retrieving the challenge"
            ) from error

        self._parse_cookies(response)

    def _parse_cookies(self, response: ClientResponse) -> None:
        """Parse cookies manually due to invalid key."""
        for hdr in response.headers.getall("Set-Cookie", ()):
            kvp = hdr.split(";")[0].split("=")
            if len(kvp) == 2:
                self._cookies[kvp[0]] = kvp[1]
