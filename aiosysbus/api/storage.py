"""Storage & co."""

class HTTPService:
    """HTTPService class."""

    def __init__(self, access):
        """Init."""
        self._access = access        

    def get_webdav_authmodes(self, conf=None):
        """Get authentication modes."""
        return self._access.post("HTTPService", "getAuthenticationModes", conf)

    def add_webdav_user(self, conf=None):
        """Add user for WebDav."""
        return self._access.post("HTTPService.WebDav.DigestManager", "addUser", conf)

    def set_webdav_user(self, conf=None):
        """Change user for WebDav."""
        return self._access.post("HTTPService.WebDav.DigestManager", "changeUser", conf)

    def set_webdav_password(self, conf=None):
        """Change password for WebDav user."""
        return self._access.post("HTTPService.WebDav.DigestManager", "changePassword", conf)

    def import_webdav(self, conf=None):
        """Upload to WebDav."""
        return self._access.post("HTTPService.WebDav.DigestManager", "Upload", conf)

class StorageService:
    """Locations class."""

    def __init__(self, access):
        """Init."""
        self._access = access

class USBHosts:
    """USBHosts class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_usb_device(self, conf=None):
        """Get USB device."""
        return self._access.post("USBHosts", "get", conf)

    def get_usb_devices(self, conf=None):
        """Get All USB devices."""
        return self._access.post("USBHosts", "getDevices", conf)

    def get_usb_plug(self, conf=None):
        """Get USB plugged."""
        return self._access.post("USBHosts", "devicePlug", conf)

    def get_usb_unplug(self, conf=None):
        """Get USB unplugged."""
        return self._access.post("USBHosts", "deviceUnplugged", conf)