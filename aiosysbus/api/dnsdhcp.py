"""Livebox DHCP v4,v6 and Dynamic DNS update."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Dhcp:
    """DHCP class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def reset_dhcp_stats(self) -> dict[str, Any] | None:
        """Reset DHCPv4 statistics."""
        return await self._access.post("DHCPv4.Server", "clearStatistics")

    async def get_dhcp_pool(self) -> dict[str, Any] | None:
        """Get DHCP Pool."""
        return await self._access.post("DHCPv4.Server", "getDHCPServerPool")

    async def set_dhcp_staticlease(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Set static lease.

        conf = {"pool":"default", "MACAddress":"01:02:03:04:05:06",
        "IPAddress":"192.168.1.55"}
        """
        pool = conf.pop("pool")
        return await self._access.post(
            f"DHCPv4.Server.Pool.{pool}", "addStaticLease", conf
        )

    async def set_dhcp_staticlease_frompool(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Set static lease.

        conf = {"pool":"default", "MACAddress":"01:02:03:04:05:06",
        "IPAddress":"192.168.1.55"}
        """
        pool = conf.pop("pool")
        return await self._access.post(
            f"DHCPv4.Server.Pool.{pool}", "addLeaseFromPool", conf
        )

    async def del_dhcp_staticlease(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Remove static lease.

        conf = {"MACAddress":"01:02:03:04:05:06"}
        """
        pool = conf.pop("pool")
        return await self._access.post(
            f"DHCPv4.Server.Pool.{pool}", "deleteStaticLease", conf
        )

    async def get_dhcp_staticleases(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Get leases."""
        pool = conf.pop("pool")
        return await self._access.post(
            f"DHCPv4.Server.Pool.{pool}", "getStaticLeases", conf
        )

    async def get_dhcp_leases(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Get leases."""
        pool = conf.pop("pool")
        return await self._access.post(f"DHCPv4.Server.Pool.{pool}", "getLeases", conf)

    async def set_dhcp_leasetime(
        self, conf: dict[str, Any] = {"pool": "default"}
    ) -> dict[str, Any] | None:
        """Set lease time."""
        pool = conf.pop("pool")
        return await self._access.post(
            f"DHCPv4.Server.Pool.{pool}", "setLeaseTime", conf
        )

    async def set_dhcp_leaserenew(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set lease force renew."""
        return await self._access.post(
            "DHCPv4.Server.Pool.Rule.Lease", "forceRenew", conf
        )

    async def get_dhcp_stats(self) -> dict[str, Any] | None:
        """Get DHCP Pool."""
        return await self._access.post("DHCPv4.Server.Stats", "get")

    async def set_dhcp_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set DHCP configuration.

        conf = {"Address":"01:02:03:04:05:06","Netmask":"192.168.1.55",
        "DHCPEnable":"","DHCPMinAddress":"","DHCPMaxAddress":""}
        """
        return await self._access.post("NMC", "setLANIP", conf)

    async def get_dhcp_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DHCP configuration."""
        return await self._access.post("NMC", "getLANIP", conf)

    async def get_prefixinformation(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get prefix infos.

        conf = {"interface":""}
        """
        return await self._access.post("DHCPv6.Server", "getPrefixInformation", conf)

    async def enable_dhcp6(self) -> dict[str, Any] | None:
        """Enable DHCP Ipv6."""
        return await self._access.post("DHCPv6.Server", "enableDHCPv6Server")

    async def get_dhcp6_status(self) -> dict[str, Any] | None:
        """Get DHCP Server status."""
        return await self._access.post("DHCPv6.Server", "getDHCPv6ServerStatus")


class DynDNS:
    """Dynamic DNS class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_services(self) -> dict[str, Any] | None:
        """Get DHCP Server status."""
        return await self._access.post("DynDNS", "getServices")

    async def get_hosts(self) -> dict[str, Any] | None:
        """Get DHCP Server status."""
        return await self._access.post("DynDNS", "getHosts")

    async def set_host(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set host."""
        return await self._access.post("DynDNS", "addHost", conf)

    async def del_host(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Del Host."""
        return await self._access.post("DynDNS", "delHost", conf)

    async def get_ddns(self) -> dict[str, Any] | None:
        """Get status."""
        return await self._access.post("DynDNS", "getGlobalEnable")

    async def set_ddns(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Enable dynamic dns."""
        return await self._access.post("DynDNS", "setGlobalEnable", conf)
