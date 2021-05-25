"""Livebox Events."""


class Event:
    """Event class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_events(self, conf=None):
        """Get all events."""
        return self._access.post("eventmanager", "get_events", conf)

    def open_channel(self, conf=None):
        """Open channel."""
        return self._access.post("eventmanager", "open_channel", conf)

    def subscribe(self, conf=None):
        """Subscribe Event."""
        return self._access.post("eventmanager", "subscribe", conf)

    def unsubscribe(self, conf=None):
        """Unsubscribe Event."""
        return self._access.post("eventmanager", "unsubscribe", conf)
