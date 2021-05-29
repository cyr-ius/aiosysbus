"""Screen (LCD) interface."""

class Screen:
    """Class Screen."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def getShowWifiPassword(self):
        """Show status display wifi password (display on box)."""
        return self._access.post("Screen", "getShowWifiPassword")

    def setShowWifiPassword(self, conf):
        """Set wifi password (display on box)."""
        return self._access.post("Screen", "setShowWifiPassword", conf)
