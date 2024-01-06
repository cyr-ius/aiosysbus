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

    async def async_getLanguage(self) -> dict[str, Any] | None:
        """return await language."""
        return await self._access.post("UserInterface", "getLanguage")

    async def async_setLanguage(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set language."""
        return await self._access.post("UserInterface", "setLanguage", conf)

    async def async_getState(self) -> dict[str, Any] | None:
        """return await state."""
        return await self._access.post("UserInterface", "getState")

    async def async_setState(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set state."""
        return await self._access.post("UserInterface", "setState", conf)

    async def async_getDebugInformation(self) -> dict[str, Any] | None:
        """return await Debug information."""
        return await self._access.post("UserInterface", "getDebugInformation")
