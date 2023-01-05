"""API Acces for livebox."""
from __future__ import annotations

import json
import logging
from typing import Any, Callable
from urllib.parse import urlsplit

from requests import RequestException, Response, Session

from .exceptions import AuthorizationError, HttpRequestError, NotOpenError

logger = logging.getLogger(__name__)


class Access:  # pylint: disable=[too-many-instance-attributes]
    """Access control."""

    # pylint: disable-next=[too-many-arguments]
    def __init__(
        self,
        session: Session,
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
        self.retry = 0
        self.max_retry = 3

    def _get_challenge(self, base_url: str, timeout: int = 10) -> None:
        """Return challenge from livebox API."""
        url_tbl = urlsplit(base_url)
        url = f"{url_tbl.scheme}://{url_tbl.netloc}"

        try:
            self.session.get(url, timeout=timeout)
        except RequestException as error:
            raise NotOpenError("Open session failed") from error

    def _get_session_token(self) -> tuple[str | None, str | None]:
        """Get session token from livebox.

        Returns (session_token, session_permissions)
        """
        # Get challenge from API
        self._get_challenge(self.base_url, self.timeout)

        auth = json.dumps(
            {
                "service": "sah.Device.Information",
                "method": "createContext",
                "parameters": {
                    "applicationName": "so_sdkut",
                    "username": self.username,
                    "password": self.password,
                },
            }
        )

        sah_headers = {
            "Content-Type": "application/x-sah-ws-1-call+json",
            "Authorization": "X-Sah-Login",
        }

        try:
            response = self.session.post(
                self.base_url, data=auth, headers=sah_headers, timeout=self.timeout
            )
        except RequestException as error:
            raise HttpRequestError("Error HttpRequest") from error

        resp = response.json()
        if not resp.get("data"):
            raise AuthorizationError(
                f"Starting session failed (APIResponse: {json.dumps(resp)})"
            )

        session_token = resp.get("data").get("contextID")
        session_permissions = resp.get("data").get("groups")
        logger.debug("Token %s", session_token)

        return (session_token, session_permissions)

    def _refresh_session_token(self) -> None:
        """Refresh token."""
        # Get token for the current session
        session_token, session_permissions = self._get_session_token()
        self.session_token = session_token
        self.session_permissions = session_permissions

    def _retry(
        self, response: Response, callback: Callable[..., Any], *kwargs: Any
    ) -> None:
        if response.status_code == 401 and self.retry < self.max_retry:
            self.retry += 1
            callback(kwargs)
        else:
            self.retry = 0

    def _get_headers(self) -> dict[str, str]:
        """Get headers."""
        if not self.session_token:
            raise NotOpenError("Session token is missing")
        return {
            "X-Context": self.session_token,
            "Content-Type": "application/x-sah-ws-1-call+json; charset=UTF-8",
        }

    def _perform_request(
        self, verb: Callable[..., Response], **kwargs: Any
    ) -> dict[str, Any] | None:
        """Perform the given request, refreshing the session token if needed."""
        if not self.session_token:
            self._refresh_session_token()

        url = self.base_url

        request_params = {
            **kwargs,
            "headers": self._get_headers(),
            "timeout": self.timeout,
        }

        logger.debug("Payload for request: %s - %s", str(url), str(request_params))

        # call request
        try:
            response = verb(url, **request_params)
        except RequestException as error:
            raise HttpRequestError("Error HttpRequest") from error

        if not response.status_code == 200:
            raise HttpRequestError(
                f"Error HttpRequest (APIResponse: {str(response.status_code)})"
            )
        resp: dict[str, dict[str, Any]] = response.json()
        logger.debug("Result: %s", str(resp))

        if resp.get("result", {}).get("errors"):
            self.retry += 1
            self._refresh_session_token()
            if self.retry < self.max_retry:
                logger.debug("Retrying (%s) request..", self.retry)
                self._perform_request(verb, **kwargs)
            else:
                raise HttpRequestError(f"{resp['result'].get('errors')}")

        return resp["result"] if "result" in resp else None

    def get(
        self, service: str, method: str, parameters: dict[str, Any] | None = {}
    ) -> dict[str, Any] | None:
        """Send get request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.get, json=data)

    def post(
        self, service: str, method: str, parameters: dict[str, Any] | None = {}
    ) -> dict[str, Any] | None:
        """Send post request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.post, json=data)

    def put(
        self, service: str, method: str, parameters: dict[str, Any] | None = {}
    ) -> dict[str, Any] | None:
        """Send put request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.put, json=data)

    def delete(
        self, service: str, method: str, parameters: dict[str, Any] | None = {}
    ) -> dict[str, Any] | None:
        """Send delete request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.delete, json=data)

    def get_permissions(self) -> str | None:
        """Return the permissions for this session/app."""
        if not self.session_permissions:
            self._refresh_session_token()
        return self.session_permissions

    def connect(self) -> None:
        """Check connect successful."""
        if not self.session_token:
            self._refresh_session_token()
