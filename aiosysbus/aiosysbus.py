"""API for livebox routeur."""
import logging
import inspect
import requests

from .access import Access
from .exceptions import AuthorizationError, HttpRequestError, NotOpenError
import aiosysbus.api as Api

logger = logging.getLogger(__name__)


class AIOSysbus:
    """Sysbus is API for livebox."""

    def __init__(self, username, password, timeout=10, host="192.168.1.1", port="80"):
        """Load parameters."""
        self._access = None
        self._session = requests.session()
        self._username = username
        self._password = password
        self._timeout = timeout
        self._host = host
        self._port = port
        self._authorize = False

    def _load_modules(self):
        """Instantiate modules."""
        for name in Api.__dict__.keys():
            obj = getattr(Api, name)
            if inspect.isclass(obj):
                setattr(self, name.lower(), obj(self._access))

    def _get_base_url(self, host, port):
        """Return base url for HTTPS requests."""
        return "http://{0}:{1}/ws".format(host, port)

    def get_permissions(self):
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

    def connect(self):
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
