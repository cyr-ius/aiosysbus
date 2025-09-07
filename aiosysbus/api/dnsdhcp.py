"""Livebox DHCP v4,v6 and Dynamic DNS update."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class Dhcp:
    """DHCP class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_reset_dhcp_stats(self) -> None:
        """Reset DHCPv4 statistics."""
        return await self._auth.post("DHCPv4.Server", "clearStatistics")

    async def async_get_dhcp_pool(self) -> dict[str, Any]:
        """Get DHCP Pool.

        Arguments:
        - id (str)
        """
        return await self._auth.post("DHCPv4.Server", "getDHCPServerPool")

    async def async_set_dhcp_pool(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get DHCP Pool.

        Arguments:
        - name (str)
        - interface (str)
        """
        return await self._auth.post("DHCPv4.Server", "createPool", conf)

    # Server Pool

    async def async_set_dhcp_lease_frompool(
        self, conf: dict[str, Any], domain: str = "default"
    ) -> str:
        """Set static lease.

        Arguments:
         - MACAddress (str)
        """
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{domain}", "addLeaseFromPool", conf
        )

    async def async_set_dhcp_staticlease(
        self, conf: dict[str, Any], domain: str = "default"
    ) -> None:
        """Set static lease.

        Arguments:
         - MACAddress (str)
         - IPAddress (str) optional
         - Enable (bool) optional
        """
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{domain}", "setLeaseTime", conf
        )

    async def async_del_dhcp_staticlease(
        self, conf: dict[str, Any], domain: str = "default"
    ) -> None:
        """Remove static lease.

        Arguments:
        - domain (str) "default" or "guest"
         - MACAddress (str)
        """
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{domain}", "deleteStaticLease", conf
        )

    async def async_get_dhcp_staticleases(
        self, domain: str = "default"
    ) -> list[dict[str, Any]]:
        """Get leases.

        Arguments:
        - domain (str) "default" or "guest"
        """
        return await self._auth.post(f"DHCPv4.Server.Pool.{domain}", "getStaticLeases")

    async def async_get_dhcp_leases(
        self, conf: dict[str, Any] | None = None, domain: str = "default"
    ) -> list[dict[str, Any]]:
        """Get leases.

        Arguments:
        - domain (str) "default" or "guest"
         - rule (str) optional
        """
        return await self._auth.post(f"DHCPv4.Server.Pool.{domain}", "getLeases", conf)

    async def async_set_dhcp_leasetime(
        self, conf: dict[str, Any], domain: str = "default"
    ) -> dict[str, Any]:
        """Set lease time.

        Arguments:
         - domain (str) "default" or "guest"
         - leasetime (int)
        """
        return await self._auth.post(
            f"DHCPv4.Server.Pool.{domain}", "setLeaseTime", conf
        )

    # DHCPv4.Server.Pool.Rule.Lease

    async def async_set_dhcp_leaserenew(self) -> None:
        """Set lease force renew."""
        return await self._auth.post("DHCPv4.Server.Pool.Rule.Lease", "forceRenew")

    # DHCPv4.Server.Stats

    async def async_get_dhcp_stats(self) -> list[dict[str, Any]]:
        """Get DHCP Pool."""
        return await self._auth.post("DHCPv4.Server.Stats", "getDoraCyclesDetails")

    # DHCPv6.Server
    async def async_get_pdprefixlease(self) -> list[dict[str, Any]]:
        """GET PD Prefix leases."""
        return await self._auth.post("DHCPv6.Server", "getPDPrefixLeases")

    async def async_get_pdprefixinfo(self) -> list[dict[str, Any]]:
        """GET PD Prefix information."""
        return await self._auth.post("DHCPv6.Server", "getPDPrefixInformation")

    async def async_enable_dhcp6(self, conf: dict[str, Any]) -> None:
        """Enable DHCP Ipv6.

        Arguments:
        -enable (bool)
        """
        return await self._auth.post("DHCPv6.Server", "enableDHCPv6Server", conf)

    async def async_get_dhcp6_status(self) -> str:
        """Get DHCP Server status."""
        return await self._auth.post("DHCPv6.Server", "getDHCPv6ServerStatus")

    async def async_dhcp6_create_pool(self, conf: dict[str, Any]) -> str:
        """Get DHCP Server status.

        Arguments:
        - name(str)
        - interface (str)

        """
        return await self._auth.post("DHCPv6.Server", "createPool", conf)


class Dns:
    """DNS class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_set_mode(self, conf: dict[str, str]) -> None:
        """Set mode.

        Argument:
        - mode (str)
        """
        return await self._auth.post("DNS", "setMode")

    async def async_get_mode(self) -> str:
        """Get mode."""
        return await self._auth.post("DNS", "getMode")

    async def async_get_dnsservers(self, conf: dict[str, str]) -> str:
        """Get DNS Servers.

        Argument:
        - flag (str)
        """
        return await self._auth.post("DNS", "getDNSServers", conf)

    async def async_get_dnsservers_by_type(self, conf: dict[str, str]) -> str:
        """Get DNS Servers by type.

        Argument:
        - type (str)
        """
        return await self._auth.post("DNS", "getDNSServersByType", conf)

    # DNS Server

    async def async_set_host(self, conf: dict[str, Any] | None = None) -> bool:
        """Get DNS Servers by type.

        Argument:
        - name (str) optional
        - ip_address_v4 (list) optional
        - ip_address_v6 (list) optional
        - type (str) optional
        - commit (bool) optional
        """
        return await self._auth.post("DNS.Server", "setHost", conf)

    async def async_list_hosts(self, conf: dict[str, Any] | None = None) -> list[Any]:
        """List hosts.

        Argument:
        - type (str) optional
        """
        return await self._auth.post("DNS.Server", "listHosts", conf)

    async def async_delete_hosts(self, conf: dict[str, Any] | None = None) -> bool:
        """List hosts.

        Argument:
        - name (str) optional
        - commit (bool) optional
        """
        return await self._auth.post("DNS.Server", "deleteHost", conf)

    async def async_set_route(self, conf: dict[str, Any] | None = None) -> bool:
        """Set route.

        Argument:
        - id (str) optional
        - dns (bool) optional
        - src (bool) optional
        - srcmask (int) optional
        - domain (domain) optional
        - metric (int) optional
        - intf (str) optional
        - commit (bool) optional
        - flags (int) optional
        """
        return await self._auth.post("DNS.Server", "setRoute", conf)

    async def async_delete_route(self, conf: dict[str, Any] | None = None) -> bool:
        """Delete route.

        Argument:
        - id (str) optional
        - dns (bool) optional
        - commit (bool) optional
        """
        return await self._auth.post("DNS.Server", "deleteRoute", conf)

    async def async_set_domain(self, conf: dict[str, Any] | None = None) -> bool:
        """Set domain.

        Argument:
        - domain (domain) optional
        """
        return await self._auth.post("DNS.Server", "setDomain", conf)

    async def async_get_domain(self) -> str:
        """Get domain."""
        return await self._auth.post("DNS.Server", "getDomain")

    async def async_get_metrics(self) -> str:
        """Get metrics."""
        return await self._auth.post("DNS.Server", "getMetrics")

    async def async_reset_metrics(self) -> str:
        """Reset metrics."""
        return await self._auth.post("DNS.Server", "resetMetrics")

    async def async_get_servers(self) -> dict[str, Any]:
        """Get servers."""
        return await self._auth.post("DNS.Server", "getServers")

    async def async_configure_cache(self, conf: dict[str, Any]) -> None:
        """Set configure cache.

        Argument:
        - enable (bool)
        - maxCachedEntries (int) optional
        - commit (bool) optional
        """
        return await self._auth.post("DNS.Server", "configureCache", conf)

    async def async_check_server(self) -> bool:
        """Check server."""
        return await self._auth.post("DNS.Server", "checkServer")

    async def async_commit(self) -> bool:
        """Commit"."""
        return await self._auth.post("DNS.Server", "commit")

    # DNS Server cache

    async def async_dump(self) -> list[Any]:
        """Cache dump."""
        return await self._auth.post("DNS.Server.Cache", "dump")

    async def async_flush(self) -> bool:
        """Cache flush"."""
        return await self._auth.post("DNS.Server.Cache", "flush")


class DynDNS:
    """Dynamic DNS class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_services(self) -> list[dict[str, Any]]:
        """Get services."""
        return await self._auth.post("DynDNS", "getServices")

    async def async_get_hosts(self) -> list[dict[str, Any]]:
        """Get hosts."""
        return await self._auth.post("DynDNS", "getHosts")

    async def async_add_host(self, conf: dict[str, Any] | None = None) -> bool:
        """Set host.

        Arguments:
        - service (str) optional
        - hostname (str) optional
        - username (str) optional
        - password (str) optional
        - enable (bool) optional
        """
        return await self._auth.post("DynDNS", "addHost", conf)

    async def async_del_host(self, conf: dict[str, Any] | None = None) -> bool:
        """Del Host.

        Arguments:
        - hostname (str) optional
        """
        return await self._auth.post("DynDNS", "delHost", conf)

    async def async_set_global_enable(self, conf: dict[str, Any] | None = None) -> None:
        """Set Global enable.

        Arguments:
        - enable (bool) optional
        """
        return await self._auth.post("DynDNS", "setGlobalEnable", conf)

    async def async_get_global_enable(self) -> bool:
        """Get Global enable."""
        return await self._auth.post("DynDNS", "getGlobalEnable")

    async def async_set_enable_cgnat(self, conf: dict[str, Any] | None = None) -> None:
        """Set enable on Cgnat.

        Arguments:
        - value (bool) optional
        """
        return await self._auth.post("DynDNS", "setEnableOnCgnat", conf)

    async def async_get_enable_cgnat(self) -> bool:
        """Get enable on Cgnat."""
        return await self._auth.post("DynDNS", "getEnableOnCgnat")
