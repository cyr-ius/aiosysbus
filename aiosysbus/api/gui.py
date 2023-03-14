"""Livebox User interface."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class UserInterface:
    """User interface."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def getLanguage(self) -> dict[str, Any] | None:
        """Return language."""
        return await self._access.post("UserInterface", "getLanguage")

    async def setLanguage(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set language."""
        return await self._access.post("UserInterface", "setLanguage", conf)

    async def getState(self) -> dict[str, Any] | None:
        """Return state."""
        return await self._access.post("UserInterface", "getState")

    async def setState(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set state."""
        return await self._access.post("UserInterface", "setState", conf)

    async def getDebugInformation(self) -> dict[str, Any] | None:
        """Return Debug information."""
        return await self._access.post("UserInterface", "getDebugInformation")
