"""Network settings."""

class Wifi:
    """Wifi setting."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_wifi(self, conf=None):
        """Get wifi configuration."""
        return self._access.post("NMC.Wifi", "get", conf)

    def set_wifi(self, conf):
        """Set wifi configuration."""
        return self._access.post("NMC.Wifi", "set", conf)

    def get_wifi_Stats(self, conf=None):
        """Wifi Statistics."""
        return self._access.post("NMC.Wifi", "getStats", conf)

    def start_wifi_pairing(self):
        """Wifi start pairing."""
        return self._access.post("NMC.Wifi", "startPairing")

    def stop_wifi_pairing(self):
        """Wifi stop pairing."""
        return self._access.post("NMC.Wifi", "stopPairing")

    def start_wifi_autochannel(self):
        """Wifi select auto channel."""
        return self._access.post("NMC.Wifi", "startAutoChannelSelection")

    def get_openmode_Status(self, conf=None):
        """Get Wifi sharing information."""
        return self._access.post("Wificom.OpenMode", "getStatus", conf)

    def get_securemode_Status(self, conf=None):
        """Get secure for wifi."""
        return self._access.post("Wificom.SecureMode", "getStatus", conf)

class Lan:
    """Home Lan."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_lan(self, conf=None):
        """Results for Lan."""
        return self._access.post("HomeLan", "getResults", conf)

    def get_lan_interfaces(self, conf=None):
        """Get Interfaces."""
        return self._access.post("HomeLan", "getInterfacesName", conf)

    def get_lan_maxnumber(self, conf=None):
        """Max number of records."""
        return self._access.post("HomeLan", "getMaxNumberOfRecords", conf)

    def get_lan_interval(self, conf=None):
        """Get reading interval."""
        return self._access.post("HomeLan", "getReadingInterval", conf)

    def get_lan_status(self, conf=None):
        """Get Status."""
        return self._access.post("HomeLan", "getStatus", conf)

    def import_lan(self, conf):
        """Import."""
        return self._access.post("HomeLan", "import", conf)

    def export_lan(self, conf):
        """Export."""
        return self._access.post("HomeLan", "export", conf)

    def get_lan_ip(self, conf=None):
        """Reboot livebox."""
        return self._access.post("NMC", "getLANIP", conf)

    def set_lan_ip(self, conf=None):
        """Reboot livebox."""
        return self._access.post("NMC", "setLANIP", conf)

    def get_IPv6(self, conf=None):
        """Get IPv6 information."""
        return self._access.post("NMC.IPv6", "get", conf)

    def set_IPv6(self, conf):
        """Set IPv6 information."""
        return self._access.post("NMC.IPv6", "set", conf)
