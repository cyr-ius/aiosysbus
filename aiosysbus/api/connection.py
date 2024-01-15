"""Livebox connection information."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Connection:
    """Connection class."""

    def __init__(self, access: Auth) -> None:
        """Init."""
        self._access = access

    async def async_get_lan_luckyAddrAddress(self) -> dict[str, Any] | None:
        """LAN IP Address."""
        return await self._access.post("NeMo.Intf.lan", "luckyAddrAddress")

    async def async_get_data_luckyAddrAddress(self) -> dict[str, Any] | None:
        """WAN IP Address."""
        return await self._access.post("NeMo.Intf.data", "luckyAddrAddress")

    async def async_get_lo_DHCPOption(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """DHCP Option."""
        return await self._access.post("NeMo.Intf.lo", "getDHCPOption", conf)

    async def async_get_dsl0_DSLStats(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Xdsl Connection Statistics."""
        return await self._access.post("NeMo.Intf.dsl0", "getDSLStats", conf)

    async def async_get_dsl0_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Xdsl information."""
        return await self._access.post("NeMo.Intf.dsl0", "getMIBs", conf)

    async def async_get_data_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """All data information.

        conf = {"mibs":"dsl","traverse":"down"}
        """
        return await self._access.post("NeMo.Intf.data", "getMIBs", conf)

    async def async_get_lan_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """LAN Information."""
        return await self._access.post("NeMo.Intf.lan", "getMIBs", conf)
