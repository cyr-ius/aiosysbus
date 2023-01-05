"""API for livebox routeur."""
from __future__ import annotations

import inspect
import logging

import requests

from . import api as Api
from .access import Access
from .exceptions import AuthorizationError, HttpRequestError, NotOpenError

logger = logging.getLogger(__name__)


class AIOSysbus:  # pylint: disable=[too-many-instance-attributes]
    """Sysbus is API for livebox."""

    connection: Api.Connection
    deviceinfo: Api.DeviceInfo
    nat: Api.Nat
    system: Api.System

    # pylint: disable-next=[too-many-arguments]
    def __init__(
        self,
        username: str,
        password: str,
        timeout: int = 10,
        host: str = "192.168.1.1",
        port: str = "80",
    ) -> None:
        """Load parameters."""
        self._access: Access | None = None
        self._session = requests.session()
        self._username = username
        self._password = password
        self._timeout = timeout
        self._host = host
        self._port = port
        self._authorize = False

    def _load_modules(self) -> None:
        """Instantiate modules."""
        for name, obj in Api.__dict__.items():
            if inspect.isclass(obj):
                setattr(self, name.lower(), obj(self._access))

    def _get_base_url(self, host: str, port: str) -> str:
        """Return base url for HTTPS requests."""
        return f"http://{host}:{port}/ws"

    def get_permissions(self) -> str | None:
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
        if self._access:
            return self._access.get_permissions()
        return None

    def connect(self) -> None:
        """Instantiate modules."""
        # Create livebox http access module
        base_url = self._get_base_url(self._host, self._port)
        self._access = Access(
            session=self._session,
            base_url=base_url,
            username=self._username,
            password=self._password,
            timeout=self._timeout,
        )

        if self._access:
            try:
                self._access.connect()
            except HttpRequestError as error:
                raise HttpRequestError from error
            except AuthorizationError as error:
                raise AuthorizationError from error
            except NotOpenError as error:
                raise NotOpenError from error

            # Instantiate Livebox modules
            self._load_modules()

    def close(self) -> None:
        """Close session."""
        self._session.close()
