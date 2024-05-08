"""API for livebox routeur."""

from __future__ import annotations

import inspect
import logging
from typing import Self

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
        This method simply allows you to check if the authentication works
        """
        try:
            await self._auth.async_get_session_token()
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
