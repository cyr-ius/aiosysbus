"""Livebox connection information."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Connection:
    """Connection class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_lan_luckyAddrAddress(self) -> dict[str, Any] | None:
        """LAN IP Address."""
        return self._access.post("NeMo.Intf.lan", "luckyAddrAddress")

    def get_data_luckyAddrAddress(self) -> dict[str, Any] | None:
        """WAN IP Address."""
        return self._access.post("NeMo.Intf.data", "luckyAddrAddress")

    def get_lo_DHCPOption(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """DHCP Option."""
        return self._access.post("NeMo.Intf.lo", "getDHCPOption", conf)

    def get_dsl0_DSLStats(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Xdsl Connection Statistics."""
        return self._access.post("NeMo.Intf.dsl0", "getDSLStats", conf)

    def get_dsl0_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Xdsl information."""
        return self._access.post("NeMo.Intf.dsl0", "getMIBs", conf)

    def get_data_MIBS(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """All datas informations.

        conf = {"mibs":"dsl","traverse":"down"}
        """
        return self._access.post("NeMo.Intf.data", "getMIBs", conf)

    def get_lan_MIBS(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """LAN Information."""
        return self._access.post("NeMo.Intf.lan", "getMIBs", conf)
