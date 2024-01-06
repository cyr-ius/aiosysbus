"""Screen (LCD) interface."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Screen:
    """Class Screen."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_getShowWifiPassword(self) -> dict[str, Any]:
        """Show status display wifi password (display on box)."""
        return await self._auth.post("Screen", "getShowWifiPassword")

    async def async_setShowWifiPassword(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set wifi password (display on box)."""
        return await self._auth.post("Screen", "setShowWifiPassword", conf)
