"""Livebox Events."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Event:
    """Event class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_events(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get all events."""
        return self._access.post("eventmanager", "get_events", conf)

    def open_channel(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Open channel."""
        return self._access.post("eventmanager", "open_channel", conf)

    def subscribe(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Subscribe Event."""
        return self._access.post("eventmanager", "subscribe", conf)

    def unsubscribe(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Unsubscribe Event."""
        return self._access.post("eventmanager", "unsubscribe", conf)
