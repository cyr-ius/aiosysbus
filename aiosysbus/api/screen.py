"""Screen (LCD) interface."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Screen:
    """Class Screen."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_getShowWifiPassword(self) -> dict[str, Any] | None:
        """Show status display wifi password (display on box)."""
        return await self._access.post("Screen", "getShowWifiPassword")

    async def async_setShowWifiPassword(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set wifi password (display on box)."""
        return await self._access.post("Screen", "setShowWifiPassword", conf)
