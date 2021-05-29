"""Livebox User interface."""


class UserInterface:
    """User interface."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def getLanguage(self):
        """Return language."""
        return self._access.post("UserInterface", "getLanguage")

    def setLanguage(self, conf):
        """Set language."""
        return self._access.post("UserInterface", "setLanguage", conf)

    def getState(self):
        """Return state."""
        return self._access.post("UserInterface", "getState")

    def setState(self, conf):
        """Set state."""
        return self._access.post("UserInterface", "setState", conf)

    def getDebugInformation(self):
        """Return Debug information."""
        return self._access.post("UserInterface", "getDebugInformation")
