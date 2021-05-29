"""Livebox connection information."""

class Connection:
    """Connection class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_lan_luckyAddrAddress(self):
        """LAN IP Address."""
        return self._access.post("NeMo.Intf.lan", "luckyAddrAddress")

    def get_data_luckyAddrAddress(self):
        """WAN IP Address."""
        return self._access.post("NeMo.Intf.data", "luckyAddrAddress")

    def get_lo_DHCPOption(self, conf=None):
        """DHCP Option."""
        return self._access.post("NeMo.Intf.lo", "getDHCPOption", conf)

    def get_dsl0_DSLStats(self, conf=None):
        """Xdsl Connection Statistics."""
        return self._access.post("NeMo.Intf.dsl0", "getDSLStats", conf)

    def get_dsl0_MIBS(self, conf=None):
        """Xdsl information."""
        return self._access.post("NeMo.Intf.dsl0", "getMIBs", conf)

    def get_data_MIBS(self, conf=None):
        """All datas informations.

        conf = {"mibs":"dsl","traverse":"down"}
        """
        return self._access.post("NeMo.Intf.data", "getMIBs", conf)

    def get_lan_MIBS(self, conf=None):
        """LAN Information."""
        return self._access.post("NeMo.Intf.lan", "getMIBs", conf)
