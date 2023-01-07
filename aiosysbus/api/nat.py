"""NAT settings."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Nat:
    """NAT settings."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_firewall_PortForwarding(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get port forwarding configuration

        conf = {"parameters":{"origin":"webui"}}
        """
        return self._access.post("Firewall", "getPortForwarding", conf)

    def set_firewall_PortForwarding(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set port forwarding configuration

        conf = {"parameters":{"description":"FTP","persistent":true,"enable":true,
        "protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21",
        "externalPort":"21","origin":"webui","sourceInterface":"data",
        "sourcePrefix":"","id":"FTP"}}
        """
        return self._access.post("Firewall", "setPortForwarding", conf)

    def get_firewall_DMZ(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DMZ configuration"""
        return self._access.post("Firewall", "getDMZ", conf)

    def set_firewall_DMZ(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set DMZ configuration"""
        return self._access.post("Firewall", "setDMZ", conf)

    def set_firewall_IPv6Level(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set level for IPv6 Firewall

        conf = {"parameters":{"level":"Low"}}
        """
        return self._access.post("Firewall", "setFirewallIPv6Level", conf)

    def set_firewall_Level(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set level for IPv4 Firewall

        conf = {"parameters":{"level":"Low"}}
        """
        return self._access.post("Firewall", "setFirewallLevel", conf)

    def set_firewall_Commit(self) -> dict[str, Any] | None:
        """Commit rules"""
        return self._access.post("Firewall", "commit")

    def get_upnp_Pinhole(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Upnp configuration

        conf = {"parameters":{"origin":"upnp"}}
        """
        return self._access.post("Firewall", "getPinhole", conf)

    def get_dyndns_Hosts(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Dynamic DNS Hosts configuration"""
        return self._access.post("DynDNS", "getHosts", conf)

    def get_dyndns_Services(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Dynamic DNS services configuration"""
        return self._access.post("DynDNS", "getServices", conf)

    def set_dns_name(self, mac, conf):  # type:ignore[no-untyped-def]
        """Set DNS name

        mac = '00:01:2B:3C:4D:5E'
        conf = {"parameters":{"name":"nestor","source":"dns"}}
        """
        return self._access.post("Devices/Device/" + mac + ":setName", conf)

    def get_upnp_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Upnp configuration"""
        return self._access.post("UPnP-IGD", "get", conf)

    def set_upnp_config(self, conf):  # type:ignore[no-untyped-def]
        """Set Upnp configuration

        conf = {"Enable":"1"}
        """
        return self._access.post("UPnP-IGD?_restAction=put", conf)
