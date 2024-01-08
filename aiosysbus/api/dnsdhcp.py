"""Livebox DHCP v4,v6 and Dynamic DNS update."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Dhcp:
    """DHCP class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_reset_dhcp_stats(self) -> dict[str, Any]:
        """Reset DHCPv4 statistics."""
        return await self._auth.post("DHCPv4.Server", "clearStatistics")

    async def async_get_dhcp_pool(self) -> dict[str, Any]:
        """Get DHCP Pool."""
        return await self._auth.post("DHCPv4.Server", "getDHCPServerPool")

    async def async_set_dhcp_staticlease(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any]:
        """Set static lease.

        conf = {"pool":"default", "MACAddress":"01:02:03:04:05:06",
        "IPAddress":"192.168.1.55"}
        """
        pool = conf.pop("pool")
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{pool}", "addStaticLease", conf
        )

    async def async_set_dhcp_staticlease_frompool(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any]:
        """Set static lease.

        conf = {"pool":"default", "MACAddress":"01:02:03:04:05:06",
        "IPAddress":"192.168.1.55"}
        """
        pool = conf.pop("pool")
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{pool}", "addLeaseFromPool", conf
        )

    async def async_del_dhcp_staticlease(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Remove static lease.

        conf = {"MACAddress":"01:02:03:04:05:06"}
        """
        pool = (conf if conf else {}).pop("pool", "default")
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{pool}", "deleteStaticLease", conf
        )

    async def async_get_dhcp_staticleases(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get leases."""
        pool = (conf if conf else {}).pop("pool", "default")
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{pool}", "getStaticLeases", conf
        )

    async def async_get_dhcp_leases(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get leases."""
        pool = (conf if conf else {}).pop("pool", "default")
        return await self._auth.post(f"DHCPv4.Server.Pool.{pool}", "getLeases", conf)

    async def async_set_dhcp_leasetime(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set lease time."""
        pool = (conf if conf else {}).pop("pool", "default")
        return await self._auth.post(f"DHCPv4.Server.Pool.{pool}", "setLeaseTime", conf)

    async def async_set_dhcp_leaserenew(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set lease force renew."""
        return await self._auth.post(
            "DHCPv4.Server.Pool.Rule.Lease", "forceRenew", conf
        )

    async def async_get_dhcp_stats(self) -> dict[str, Any]:
        """Get DHCP Pool."""
        return await self._auth.post("DHCPv4.Server.Stats", "get")

    async def async_set_dhcp_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set DHCP configuration.

        conf = {"Address":"01:02:03:04:05:06","Netmask":"192.168.1.55",
        "DHCPEnable":"","DHCPMinAddress":"","DHCPMaxAddress":""}
        """
        return await self._auth.post("NMC", "setLANIP", conf)

    async def async_get_dhcp_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DHCP configuration."""
        return await self._auth.post("NMC", "getLANIP", conf)

    async def async_get_prefixinformation(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get prefix infos.

        conf = {"interface":""}
        """
        return await self._auth.post("DHCPv6.Server", "getPrefixInformation", conf)

    async def async_enable_dhcp6(self) -> dict[str, Any]:
        """Enable DHCP Ipv6."""
        return await self._auth.post("DHCPv6.Server", "enableDHCPv6Server")

    async def async_get_dhcp6_status(self) -> dict[str, Any]:
        """Get DHCP Server status."""
        return await self._auth.post("DHCPv6.Server", "getDHCPv6ServerStatus")


class DynDNS:
    """Dynamic DNS class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_services(self) -> dict[str, Any]:
        """Get DHCP Server status."""
        return await self._auth.post("DynDNS", "getServices")

    async def async_get_hosts(self) -> dict[str, Any]:
        """Get DHCP Server status."""
        return await self._auth.post("DynDNS", "getHosts")

    async def async_set_host(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set host."""
        return await self._auth.post("DynDNS", "addHost", conf)

    async def async_del_host(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Del Host."""
        return await self._auth.post("DynDNS", "delHost", conf)

    async def async_get_ddns(self) -> dict[str, Any]:
        """Get status."""
        return await self._auth.post("DynDNS", "getGlobalEnable")

    async def async_set_ddns(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Enable dynamic dns."""
        return await self._auth.post("DynDNS", "setGlobalEnable", conf)
