""" API for livebox routeur."""
import logging
import requests

from aiosysbus.access import Access
from aiosysbus.exceptions import NotOpenError, AuthorizationError
from aiosysbus.api import Call, Connection, Dhcp, Nat, Screen, System, Wifi

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
        """ Instantiate modules."""
        # Instantiate Livebox modules
        if self._access:
            self.call = Call(self._access)
            self.connection = Connection(self._access)
            self.dhcp = Dhcp(self._access)
            self.nat = Nat(self._access)
            self.screen = Screen(self._access)
            self.system = System(self._access)
            self.wifi = Wifi(self._access)

    def _get_base_url(self, host, port):
        """Returns base url for HTTPS requests."""
        return "http://{0}:{1}/ws".format(host, port)

    def get_permissions(self):
        """
        Returns the permissions for this app.
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
        """ Instantiate modules."""
        
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
            except AuthorizationError as e:
                raise AuthorizationError(e)
            except NotOpenError as e:
                raise NotOpenError(e)              
            
            # Instantiate Livebox modules
            self._load_modules()
