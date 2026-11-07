"""API for livebox routeur."""

from __future__ import annotations

import inspect
import logging
from typing import Any, Self

from aiohttp import ClientSession
from yarl import URL as yurl

from . import api as Api
from .auth import Auth
from .exceptions import AiosysbusException, AuthenticationFailed

logger = logging.getLogger(__name__)


class AIOSysbus:
    """Sysbus is API for livebox."""

    def __init__(
        self,
        username: str,
        password: str,
        session: ClientSession | None = None,
        timeout: int = 120,
        host: str = "192.168.1.1",
        port: int = 80,
        use_tls: bool = False,
        verify_tls: bool = True,
    ) -> None:
        """Load parameters."""
        self._session = session or ClientSession()
        base_url = yurl.build(
            scheme="https" if use_tls else "http", host=host, port=port, path="/ws"
        )
        self._auth = Auth(
            session=self._session,
            base_url=base_url,
            username=username,
            password=password,
            timeout=timeout,
            verify_tls=verify_tls,
        )

        self._cleanup_session = session is None
        self._authorize = False

        # Instantiate Livebox modules
        self._load_modules()

    @property
    def is_connected(self) -> bool:
        """Check if connected."""
        return self._session is not None and not self._session.closed

    def _load_modules(self) -> None:
        """Instantiate modules."""
        for name, obj in Api.__dict__.items():
            if inspect.isclass(obj):
                setattr(self, name.lower(), obj(self._auth))

    async def async_connect(self) -> None:
        """Test authentication.

        There is no need to use this method to call the APIs,
        as they automatically obtain a session token.
        This method simply allows you to check if the authentication works.
        The session is kept, so it is reused by the next calls and can be
        released with async_logout.
        """
        try:
            await self._auth._async_refresh_session_token()
        except AuthenticationFailed as error:
            raise AuthenticationFailed(error) from error
        except AiosysbusException as error:
            raise AiosysbusException(error) from error

    async def async_get_permissions(self) -> str | None:
        """Return the permissions for this app.

        The permissions are returned as a dictionary key->boolean where the
        keys are the permission identifier (cf. the constants PERMISSION_*).
        A permission not listed in the returned permissions is equivalent to
        having this permission set to false.
        Note that the permissions are the one the app had when the session was
        opened. If they have been changed in the meantime, they may be outdated
        until the session token is refreshed.
        If the session has not been opened yet, returns None.
        """
        return self._auth.session_permissions

    async def async_logout(self) -> bool:
        """Release the session on the livebox.

        The livebox accepts a limited number of sessions, call this method
        when the API is no longer used. A new session is opened automatically
        by the next call.
        Returns True when the livebox confirms the release.
        """
        return await self._auth.async_logout()

    @property
    def session_state(self) -> dict[str, Any] | None:
        """Return the current session, or None when no session is open.

        The returned dict ({"context_id": str, "cookies": dict}) can be saved
        and given to async_release_session by a later process, so a session
        left open by a crash can still be released.
        """
        if not self._auth.session_token:
            return None
        return {
            "context_id": self._auth.session_token,
            "cookies": dict(self._auth._cookies),
        }

    async def async_release_session(self, session_state: dict[str, Any]) -> bool:
        """Release a session saved with session_state.

        The current session of this client is not modified.
        Returns True when the livebox confirms the release, False otherwise
        (including when session_state holds no context).
        """
        context_id = session_state.get("context_id")
        if not context_id or not isinstance(context_id, str):
            return False
        cookies = session_state.get("cookies") or {}
        return await self._auth.async_release_context(context_id, dict(cookies))

    async def async_close(self) -> None:
        """Close session."""
        if self._cleanup_session and self._session:
            await self._session.close()

    async def __aenter__(self) -> Self:
        """Async enter."""
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit."""
        await self.async_close()
