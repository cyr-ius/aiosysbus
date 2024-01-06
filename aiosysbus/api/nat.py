"""NAT settings."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Nat:
    """NAT settings."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_firewall_PortForwarding(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get port forwarding configuration

        conf = {"parameters":{"origin":"webui"}}
        """
        return await self._auth.post("Firewall", "getPortForwarding", conf)

    async def async_set_firewall_PortForwarding(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set port forwarding configuration

        conf = {"parameters":{"description":"FTP","persistent":true,"enable":true,
        "protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21",
        "externalPort":"21","origin":"webui","sourceInterface":"data",
        "sourcePrefix":"","id":"FTP"}}
        """
        return await self._auth.post("Firewall", "setPortForwarding", conf)

    async def async_get_firewall_DMZ(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DMZ configuration"""
        return await self._auth.post("Firewall", "getDMZ", conf)

    async def async_set_firewall_DMZ(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set DMZ configuration"""
        return await self._auth.post("Firewall", "setDMZ", conf)

    async def async_set_firewall_IPv6Level(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set level for IPv6 Firewall

        conf = {"parameters":{"level":"Low"}}
        """
        return await self._auth.post("Firewall", "setFirewallIPv6Level", conf)

    async def async_set_firewall_Level(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set level for IPv4 Firewall

        conf = {"parameters":{"level":"Low"}}
        """
        return await self._auth.post("Firewall", "setFirewallLevel", conf)

    async def async_set_firewall_Commit(self) -> dict[str, Any]:
        """Commit rules"""
        return await self._auth.post("Firewall", "commit")

    async def async_get_upnp_Pinhole(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Upnp configuration

        conf = {"parameters":{"origin":"upnp"}}
        """
        return await self._auth.post("Firewall", "getPinhole", conf)

    async def async_get_dyndns_Hosts(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Dynamic DNS Hosts configuration"""
        return await self._auth.post("DynDNS", "getHosts", conf)

    async def async_get_dyndns_Services(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Dynamic DNS services configuration"""
        return await self._auth.post("DynDNS", "getServices", conf)

    async def async_set_dns_name(
        self, mac: str, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set DNS name

        mac = '00:01:2B:3C:4D:5E'
        conf = {"parameters":{"name":"nestor","source":"dns"}}
        """
        return await self._auth.post("Devices/Device/" + mac, "setName", conf)

    async def async_get_upnp_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Upnp configuration"""
        return await self._auth.post("UPnP-IGD", "get", conf)

    async def async_set_upnp_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set Upnp configuration

        conf = {"Enable":"1"}
        """
        return await self._auth.post("UPnP-IGD", "put", conf)
