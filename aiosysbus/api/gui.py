"""Livebox User interface."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class UserInterface:
    """User interface."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_getLanguage(self) -> dict[str, Any]:
        """return await language."""
        return await self._auth.post("UserInterface", "getLanguage")

    async def async_setLanguage(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set language."""
        return await self._auth.post("UserInterface", "setLanguage", conf)

    async def async_getState(self) -> dict[str, Any]:
        """return await state."""
        return await self._auth.post("UserInterface", "getState")

    async def async_setState(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set state."""
        return await self._auth.post("UserInterface", "setState", conf)

    async def async_getDebugInformation(self) -> dict[str, Any]:
        """return await Debug information."""
        return await self._auth.post("UserInterface", "getDebugInformation")
