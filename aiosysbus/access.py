import json
import logging
from requests.exceptions import RequestException

from urllib.parse import urlsplit
from aiosysbus.exceptions import NotOpenError, AuthorizationError, HttpRequestError

logger = logging.getLogger(__name__)


class Access:
    def __init__(self, session, base_url, username, password, timeout):
        self.session = session
        self.base_url = base_url
        self.username = username
        self.password = password
        self.timeout = timeout
        self.session_token = None
        self.session_permissions = None
        self.retry = 0
        self.max_retry = 3

    def _get_challenge(self, base_url, timeout=10):
        """
        Return challenge from livebox API
        """
        url_tbl = urlsplit(base_url)
        url = "{}://{}".format(url_tbl.scheme, url_tbl.netloc)
        logger.debug(url)

        try:
            self.session.get(url, timeout=timeout)
        except Exception as e:
            raise NotOpenError("Open session failed (APIResponse: {0})".format(str(e)))
        return True

    def _get_session_token(self):
        """Get session token from livebox.

        Returns (session_token, session_permissions)
        """
        # Get challenge from API
        challenge = self._get_challenge(self.base_url, self.timeout)

        if challenge:
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

            r = self.session.post(
                self.base_url, data=auth, headers=sah_headers, timeout=self.timeout
            )
            resp = r.json()

            # raise exception if resp.success != True
            if not resp.get("data"):
                raise AuthorizationError(
                    "Starting session failed (APIResponse: {0})".format(
                        json.dumps(resp)
                    )
                )

            session_token = resp.get("data").get("contextID")
            session_permissions = resp.get("data").get("groups")
            logger.debug("Token %s",session_token)

            return (session_token, session_permissions)

    def _refresh_session_token(self):
        """Refresh token."""
        # Get token for the current session
        session_token, session_permissions = self._get_session_token()
        self.session_token = session_token
        self.session_permissions = session_permissions

    def _retry(self, response, callback, *kwargs):
        if response.status_code == 401 and self.retry < self.max_retry:
            self.retry += 1
            #~ self._authenticate()
            callback(kwargs)
        else:
            self.retry = 0

    def _get_headers(self):
        """Get headers."""
        return {
            "X-Context": self.session_token,
            "Content-Type": "application/x-sah-ws-1-call+json; charset=UTF-8",
        }

    def _perform_request(self, verb, **kwargs):
        """Perform the given request, refreshing the session token if needed."""
        if not self.session_token:
            self._refresh_session_token()

        url = self.base_url

        request_params = {
            **kwargs,
            "headers": self._get_headers(),
            "timeout": self.timeout,
        }

        logger.debug("Payload for request: %s - %s", str(url),str(request_params))

        # call request
        r = verb(url, **request_params)

        # raise exception if r is empty
        if not r.status_code == 200:
            raise HttpRequestError("Error HttpRequest (APIResponse: %s)" % str(r.status_code))
        resp = r.json()
        logger.debug("Result: %s", str(resp))

        if resp.get("error_code") in ["auth_required", "invalid_session"]:
            self._refresh_session_token()
            request_params["headers"] = self._get_headers()
            try:
                r = verb(url, **request_params)
                resp = r.json()
            except RequestException as e:
                logger.error(e)

        return resp["result"] if "result" in resp else None

    def get(self, service, method, parameters={}):
        """Send get request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.get, json=data)

    def post(self, service, method, parameters={}):
        """Send post request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.post, json=data)

    def put(self, service, method, parameters={}):
        """Send put request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.put, json=data)

    def delete(self, service, method, parameters={}):
        """Send delete request and return results."""
        data = {"service": service, "method": method, "parameters": parameters}
        return self._perform_request(self.session.delete, json=data)

    def get_permissions(self):
        """Returns the permissions for this session/app."""
        if not self.session_permissions:
            self._refresh_session_token()
        return self.session_permissions

    def connect(self):
        """Check connect successful."""
        if not self.session_token:
            self._refresh_session_token()           
