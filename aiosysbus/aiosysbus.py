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

    call: Api.Call
    connection: Api.Connection
    deviceinfo: Api.DeviceInfo
    devices: Api.Devices
    dhcp: Api.Dhcp
    event: Api.Event
    lan: Api.Lan
    nat: Api.Nat
    phonebook: Api.Phonebook
    schedule: Api.Schedule
    system: Api.System
    usbhosts: Api.USBHosts
    userinterface: Api.UserInterface
    wifi: Api.Wifi

    def __init__(
        self,
        username: str,
        password: str,
        session: ClientSession | None = None,
        timeout: int = 120,
        host: str = "192.168.1.1",
        port: int = 80,
        use_tls: bool = False,
    ) -> None:
        """Load parameters."""
        self._auth: Auth | None = None
        self._session = session or ClientSession()
        self._cleanup_session = session is None
        self._username = username
        self._password = password
        self._timeout = timeout
        self._host = host
        self._port = port
        self._authorize = False
        self._use_tls = use_tls

    async def async_connect(self) -> None:
        """Instantiate modules."""
        scheme = "https" if self._use_tls else "http"
        base_url = yurl.build(
            scheme=scheme, host=self._host, port=self._port, path="/ws"
        )
        self._auth = Auth(
            session=self._session,
            base_url=base_url,
            username=self._username,
            password=self._password,
            timeout=self._timeout,
        )

        if self._auth:
            try:
                await self._auth.async_get_session_token()
            except AuthenticationFailed as error:
                raise AuthenticationFailed(error) from error
            except AiosysbusException as error:
                raise AiosysbusException(error) from error

            # Instantiate Livebox modules
            self._load_modules()

    def _load_modules(self) -> None:
        """Instantiate modules."""
        for name, obj in Api.__dict__.items():
            if inspect.isclass(obj):
                setattr(self, name.lower(), obj(self._auth))

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
        if self._auth:
            return self._auth.session_permissions
        return None

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
