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

    def getLanguage(self) -> dict[str, Any] | None:
        """Return language."""
        return self._access.post("UserInterface", "getLanguage")

    def setLanguage(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set language."""
        return self._access.post("UserInterface", "setLanguage", conf)

    def getState(self) -> dict[str, Any] | None:
        """Return state."""
        return self._access.post("UserInterface", "getState")

    def setState(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set state."""
        return self._access.post("UserInterface", "setState", conf)

    def getDebugInformation(self) -> dict[str, Any] | None:
        """Return Debug information."""
        return self._access.post("UserInterface", "getDebugInformation")
