import logging
import requests

import aiosysbus
from aiosysbus.exceptions import *
from aiosysbus.access import Access
from aiosysbus.api.system import System
from aiosysbus.api.dhcp import Dhcp
from aiosysbus.api.wifi import Wifi
from aiosysbus.api.call import Call
from aiosysbus.api.connection import Connection
from aiosysbus.api.nat import Nat

# Default application descriptor
app_desc = {
    'username': 'admin',
    'app_name': 'aiosysbus',
    'app_version': aiosysbus.__version__
    }

logger = logging.getLogger(__name__)


class Sysbus:
    
    def __init__(self, app_desc=app_desc, timeout=10):
        self.timeout = timeout
        self.app_desc = app_desc
        self._access = None
    
    async def open(self, host, port,password):
        self.password = password
        self._access = await self._get_livebox_access(host, port, self.password, self.app_desc, self.timeout)
       
        # Instantiate Livebox modules
        self.system = System(self._access)
        self.dhcp = Dhcp(self._access)
        self.wifi = Wifi(self._access)
        self.call = Call(self._access)
        self.connection = Connection(self._access)
        self.nat = Nat(self._access)

    async def close(self):
        '''
        Close the livebox session
        '''
        if self._access is None:
            raise NotOpenError('Livebox is not open')
        #~ await self._access.post('login/logout')
        self._session.close()
        
    async def _get_livebox_access(self, host, port, password, app_desc, timeout=10):
        '''
        Returns an access object used for HTTP requests.
        '''

        base_url = self._get_base_url(host, port)
        self._session = requests.session()

        # Create livebox http access module
        lvbx_access = Access(self._session, base_url, password, app_desc['username'], timeout)

        return lvbx_access        

    def _get_base_url(self, host, port):
        '''
        Returns base url for HTTPS requests
        :return:
        '''
        return 'http://{0}:{1}/sysbus/'.format(host, port)        


    async def get_permissions(self):
        '''
        Returns the permissions for this app.
        The permissions are returned as a dictionary key->boolean where the
        keys are the permission identifier (cf. the constants PERMISSION_*).
        A permission not listed in the returned permissions is equivalent to
        having this permission set to false.
        Note that the permissions are the one the app had when the session was
        opened. If they have been changed in the meantime, they may be outdated
        until the session token is refreshed.
        If the session has not been opened yet, returns None.
        '''
        if self._access:
            return await self._access.get_permissions()
        else:
            return None        
