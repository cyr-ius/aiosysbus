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

    async def get_events(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get all events."""
        return await self._access.post("eventmanager", "get_events", conf)

    async def open_channel(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Open channel."""
        return await self._access.post("eventmanager", "open_channel", conf)

    async def subscribe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Subscribe Event."""
        return await self._access.post("eventmanager", "subscribe", conf)

    async def unsubscribe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Unsubscribe Event."""
        return await self._access.post("eventmanager", "unsubscribe", conf)
