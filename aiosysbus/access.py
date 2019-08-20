import json
import logging

from urllib.parse import urljoin,urlsplit
from aiosysbus.exceptions import *

logger = logging.getLogger(__name__)
#~ logger.setLevel(logging.DEBUG)

class Access:
    def __init__(self, session, base_url, password, username, http_timeout):
        self.session = session
        self.base_url = base_url
        self.password = password
        self.username = username
        self.timeout = http_timeout
        self.session_token = None
        self.session_permissions = None

    async def _get_challenge(self, base_url, timeout=10):
        '''
        Return challenge from livebox API
        '''
        url_tbl = urlsplit(base_url)
        url = url_tbl.scheme+'://'+url_tbl.netloc
        
        logger.debug(url)
        try:
            r = self.session.get(url, timeout=timeout)
        except Exception as e:
            raise NotOpenError('Open session failed (APIResponse: {0})'
                                         .format(str(e)))            
        return True

    async def _get_session_token(self, base_url, password, username, timeout=10):
        """
        Get session token from livebox.
        Returns (session_token, session_permissions)
        """
        # Get challenge from API
        challenge = await self._get_challenge(base_url, timeout)

        if challenge:
            auth = json.dumps({'service':'sah.Device.Information',
                                        'method':'createContext',
                                        'parameters':{'applicationName':'so_sdkut',
                                            'username':username,
                                            'password':password}})        
            sah_headers = { 'Content-Type':'application/x-sah-ws-1-call+json', 'Authorization':'X-Sah-Login' }
            r = self.session.post(base_url,data=auth, headers=sah_headers, timeout=timeout)
            resp = r.json()

            # raise exception if resp.success != True
            if not resp.get('data'):
                raise AuthorizationError('Starting session failed (APIResponse: {0})'
                                         .format(json.dumps(resp)))

            session_token = resp.get('data').get('contextID')
            session_permissions = resp.get('data').get('groups')

            return(session_token, session_permissions)

    async def _refresh_session_token(self):
        # Get token for the current session
        session_token, session_permissions = await self._get_session_token(
            self.base_url,
            self.password,
            self.username,
            self.timeout)

        logger.debug('Session opened')
        logger.debug('Permissions: ' + str(session_permissions))
        self.session_token = session_token
        self.session_permissions = session_permissions

    def _get_headers(self):
        return {'X-Context': self.session_token,
                      'Content-Type':'application/x-sah-ws-1-call+json; charset=UTF-8'}

    async def _perform_request(self, verb, end_url, **kwargs):
        '''
        Perform the given request, refreshing the session token if needed
        '''
        if not self.session_token:
            await self._refresh_session_token()

        url = self.base_url+end_url
        
        request_params = {
            **kwargs,
            "headers": self._get_headers(),
            "timeout": self.timeout
        }
        
        logger.debug('Request url: '+str(url))
        logger.debug('Payload for request: '+str(request_params))
        
        # call request
        r = verb(url, **request_params)
        
        # raise exception if r is empty
        if  not r.status_code == 200:
            raise HttpRequestError('Error HttpRequest (APIResponse: {0})'
                                     .format(str(r.status_code )))
        resp = r.json()
        logger.debug('Result: '+str(resp))

        if resp.get('error_code') in ['auth_required', "invalid_session"]:
            await self._refresh_session_token()
            request_params["headers"] = self._get_headers()
            try:
                r = verb(url, **request_params)
                resp = r.json()
            except requests.exceptions.RequestException as e: 
                logger.error(e)

        return resp['result'] if 'result' in resp else None

    async def get(self, end_url):
        '''
        Send get request and return results
        '''
        return await self._perform_request(self.session.get, end_url)

    async def post(self, end_url, payload=None):
        '''
        Send post request and return results
        '''
        data = json.dumps(payload) if payload is not None else None
        return await self._perform_request(self.session.post, end_url, data=data)

    async def put(self, end_url, payload=None):
        '''
        Send post request and return results
        '''
        data = json.dumps(payload) if payload is not None else None
        return await self._perform_request(self.session.put, end_url, data=data)

    async def delete(self, end_url, payload=None):
        '''
        Send delete request and return results
        '''
        data = json.dumps(payload) if payload is not None else None
        return await self._perform_request(self.session.delete, end_url, data=data)

    async def get_permissions(self):
        '''
        Returns the permissions for this session/app.
        '''
        if not self.session_permissions:
            await self._refresh_session_token()
        return self.session_permissions
