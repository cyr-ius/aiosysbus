"""SgcOmci information."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class SgcOmci:
    """SgcOmci class"""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_optical(self) -> dict[str, Any]:
        """Get optical information."""
        return await self._auth.post("SgcOmci.Optical", "get")
