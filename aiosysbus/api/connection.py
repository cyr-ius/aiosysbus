"""Livebox connection information."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class Connection:
    """Connection class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_lan_luckyAddrAddress(self) -> dict[str, Any]:
        """LAN IP Address."""
        return await self._auth.post("NeMo.Intf.lan", "luckyAddrAddress")

    async def async_get_data_luckyAddrAddress(self) -> dict[str, Any]:
        """WAN IP Address."""
        return await self._auth.post("NeMo.Intf.data", "luckyAddrAddress")

    async def async_get_lo_DHCPOption(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """DHCP Option."""
        return await self._auth.post("NeMo.Intf.lo", "getDHCPOption", conf)

    async def async_get_dsl0_DSLStats(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Xdsl Connection Statistics."""
        return await self._auth.post("NeMo.Intf.dsl0", "getDSLStats", conf)

    async def async_get_dsl0_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Xdsl information."""
        return await self._auth.post("NeMo.Intf.dsl0", "getMIBs", conf)

    async def async_get_data_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """All data information.

        conf = {"mibs":"dsl","traverse":"down"}
        """
        return await self._auth.post("NeMo.Intf.data", "getMIBs", conf)

    async def async_get_lan_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """LAN Information."""
        return await self._auth.post("NeMo.Intf.lan", "getMIBs", conf)
