"""API Access for livebox."""
from __future__ import annotations

import asyncio
import logging
import socket
from typing import Any

from aiohttp import ClientError, ClientResponseError, ClientSession

from .exceptions import (
    AuthenticationFailed,
    HttpRequestFailed,
    NotOpenError,
    RetrieveFailed,
    TimeoutExceededError,
    UnexpectedResponse,
)

_LOGGER = logging.getLogger(__name__)
MAX_RETRY = 5


class Auth:
    """Class to make authenticated requests."""

    def __init__(
        self,
        session: ClientSession,
        base_url: str,
        username: str,
        password: str,
        timeout: int,
    ) -> None:
        """Init class."""
        self.session = session
        self.base_url = base_url
        self.username = username
        self.password = password
        self.timeout = timeout

        self.session_token: str | None = None
        self.session_permissions: str | None = None
        self.retry = MAX_RETRY

    async def async_request(
        self, method: str, json: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Make a request."""
        if not self.session_token:
            await self._async_refresh_session_token()

        headers = {
            "X-Context": self.session_token,
            "Content-Type": "application/x-sah-ws-1-call+json; charset=UTF-8",
        }

        try:
            _LOGGER.debug("METHOD:%s URL:%s", method, self.base_url)
            _LOGGER.debug("DATA:%s", json)
            async with asyncio.timeout(self.timeout):
                response = await self.session.request(
                    method, self.base_url, json=json, headers=headers
                )
                response.raise_for_status()
        except (asyncio.CancelledError, asyncio.TimeoutError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to Livebox."
            ) from error
        except (ClientError, ClientResponseError, socket.gaierror) as error:
            raise HttpRequestFailed(
                "Error occurred while communicating with Livebox."
            ) from error

        content_type = response.headers.get("Content-Type", "")
        if (response.status // 100) in [4, 5]:
            if "application/json" in content_type:
                result = await response.json()
                response.close()
                raise HttpRequestFailed(result)

            result = await response.read()
            response.close()
            raise HttpRequestFailed(result)

        if "application/json" not in content_type:
            result = await response.text()
            msg = "Unexpected response from the Livebox API"
            raise UnexpectedResponse(
                msg,
                {"Content-Type": content_type, "response": result},
            )

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

    async def get(self, method: str) -> dict[str, Any] | None:
        """Send get request and return results."""
        return await self.async_request(method="get")

    async def post(
        self, service: str, method: str, params: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Send post request and return results."""
        data = {"service": service, "method": method, "parameters": params}
        return await self.async_request(method="post", json=data)

    async def put(
        self, service: str, method: str, params: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Send put request and return results."""
        data = {"service": service, "method": method, "parameters": params}
        return await self.async_request(method="put", json=data)

    async def delete(
        self, service: str, method: str, params: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Send delete request and return results."""
        data = {"service": service, "method": method, "parameters": params}
        return await self.async_request(method="delete", json=data)

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
        except (asyncio.CancelledError, asyncio.TimeoutError) as error:
            raise TimeoutExceededError(
                "Timeout occurred while connecting to Livebox."
            ) from error
        except (ClientError, ClientResponseError, socket.gaierror) as error:
            raise HttpRequestFailed(
                "Error occurred while communicating with Livebox."
            ) from error

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            raise UnexpectedResponse(
                "Unexpected response , content-type incorrect (%s)", content_type
            )

        if (response.status // 100) in [4, 5]:
            if "application/json" in content_type:
                result = await response.json()
                response.close()
                raise HttpRequestFailed(result)

            result = await response.read()
            response.close()
            raise HttpRequestFailed(result)

        rjson = await response.json()
        if not rjson.get("data"):
            raise AuthenticationFailed(
                "Starting session failed (APIResponse: %s)", rjson
            )

        session_token = rjson.get("data").get("contextID")
        session_permissions = rjson.get("data").get("groups")
        _LOGGER.debug("Token %s", session_token)
        return (session_token, session_permissions)

    async def _async_get_challenge(self, base_url: str) -> None:
        """Return challenge from livebox API."""
        try:
            async with asyncio.timeout(self.timeout):
                await self.session.request(method="get", url=base_url.parent)
        except (
            asyncio.CancelledError,
            asyncio.TimeoutError,
            ClientError,
            socket.gaierror,
        ) as error:
            raise NotOpenError("Open session failed") from error
