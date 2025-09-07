"""Network settings."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class HomeLan:
    """Home Lan."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_results(self, conf: dict[str, Any] | None = None) -> bool:
        """Results for Lan.

        Arguments:
        - Seconds (int) optional
        - NumberOfReadings (int) optional
        - InterfaceName (list) optional
        - BeginTrafficTimestamp (int) optional
        - EndTrafficTimestamp (int) optional
        """
        return await self._auth.post("HomeLan", "getResults", conf)

    async def async_get_devices_results(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Get devices results.

        Arguments:
        - Seconds (int) optional
        - NumberOfReadings (int) optional
        - DeviceName (list) optional
        - BeginTrafficTimestamp (int) optional
        - EndTrafficTimestamp (int) optional
        """
        return await self._auth.post("HomeLan", "getDeviceResults", conf)

    async def async_get_saturation_results(self) -> bool:
        """Get saturation results."""
        return await self._auth.post("HomeLan", "getSaturationResults")

    async def async_get_wan_counters(self) -> bool:
        """Get wan counters results."""
        return await self._auth.post("HomeLan", "getWANCounters")

    async def async_get_interfaces_names(self) -> bool:
        """Get Interfaces."""
        return await self._auth.post("HomeLan", "getInterfacesNames")

    async def async_get_devices_names(self) -> bool:
        """Get Interfaces."""
        return await self._auth.post("HomeLan", "getDevicesNames")

    async def async_get_status(self) -> bool:
        """Get Status."""
        return await self._auth.post("HomeLan", "getStatus")

    async def async_get_maxnumber_records(self) -> bool:
        """Max number of records."""
        return await self._auth.post("HomeLan", "getMaxNumberOfRecords")

    async def async_get_reading_interval(self) -> bool:
        """Get reading interval."""
        return await self._auth.post("HomeLan", "getReadingInterval")

    async def async_get_devices_status(self) -> bool:
        """Get Interfaces."""
        return await self._auth.post("HomeLan", "getDevicesStatus")

    async def async_get_devices_reading_interval(self) -> bool:
        """Get reading interval."""
        return await self._auth.post("HomeLan", "getDevicesReadingInterval")

    async def async_import_lan(self) -> bool:
        """Import."""
        return await self._auth.post("HomeLan", "import")

    async def async_export_lan(self) -> dict[str, Any]:
        """Export."""
        return await self._auth.post("HomeLan", "export")

    async def async_add_device(self, conf: dict[str, Any] | None = None) -> bool:
        """Get devices results.

        Arguments:
        - macaddress (str) optional
        """
        return await self._auth.post("HomeLan", "addDevice", conf)

    async def async_delete_device(self, conf: dict[str, Any] | None = None) -> bool:
        """Get devices results.

        Arguments:
        - macaddress (str) optional
        """
        return await self._auth.post("HomeLan", "deleteDevice", conf)

    async def async_start_device_monitoring(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Start device monitoring.

        Arguments:
        - duration (int) optional
        - interval (int) optional
        """
        return await self._auth.post("HomeLan", "startDeviceMonitoringTest", conf)

    async def async_stop_device_monitoring(self) -> None:
        """Stop device monitoring.."""
        return await self._auth.post("HomeLan", "stopDeviceMonitoringTest")

    async def async_start_interface_monitoring(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Start interface monitoring.

        Arguments:
        - duration (int) optional
        - interval (int) optional
        """
        return await self._auth.post("HomeLan", "startInterfaceMonitoringTest", conf)

    async def async_stop_interface_monitoring(self) -> None:
        """Stop interface monitoring."""
        return await self._auth.post("HomeLan", "stopInterfaceMonitoringTest")

    async def async_get_saturation_measures(self) -> bool:
        """Get saturation measures."""
        return await self._auth.post("HomeLan", "getSaturationMeasures")

    async def async_get_interface(self) -> bool:
        """Get saturation measures."""
        return await self._auth.post("HomeLan.Interface", "get")

    async def async_get_device(self) -> bool:
        """Get saturation measures."""
        return await self._auth.post("HomeLan.Device", "get")


class Firewall:
    """Firewall settings."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_commit(self) -> bool:
        """Commit rules."""
        return await self._auth.post("Firewall", "commit")

    async def async_set_respond_ping(self, conf: dict[str, Any]) -> bool:
        """Set respond to ping.

        Arguments:
        - sourceInterface (str)
        - service_enable (service_enable_t)
        """
        return await self._auth.post("Firewall", "setRespondToPing", conf)

    async def async_get_respond_ping(
        self, conf: dict[str, Any]
    ) -> dict[str, Any]:  # service_enable_t
        """Get respond to ping.

        Arguments:
        - sourceInterface (str)
        """
        return await self._auth.post("Firewall", "getRespondToPing", conf)

    async def async_set_redirect(self, conf: dict[str, Any] | None = None) -> str:
        """Set redirect.

        Arguments:
        - id (str) optional
        - sourceInterface (str) optional
        - destinationPort (str) optional
        - protocol (str) optional
        - ipversion (int) optional
        - enable (bool) optional
        """
        return await self._auth.post("Firewall", "setRedirect", conf)

    async def async_delete_redirect(self, conf: dict[str, Any]) -> str:
        """Delete redirect.

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "deleteRedirect", conf)

    async def async_get_redirect(self, conf: dict[str, Any]) -> str:
        """Get redirect

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "getRedirect", conf)

    async def async_set_protocol_forwarding(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set protocol forwarding configuration.

        Arguments:
        - id (str) optional
        - destinationIPAddress (str) optional
        - protocol (str) optional
        - sourceInterface (str) optional
        - sourcePrefix (str) optional
        - enable (bool) optional
        - persistent (bool) optional
        - description (str) optional

        Example:
        {"description":"FTP","persistent":true,"enable":true,"protocol":"6",
        "destinationIPAddress":"192.168.1.250","sourceInterface":"data",
        "sourcePrefix":"","id":"FTP"}}
        """
        return await self._auth.post("Firewall", "setProtocolForwarding", conf)

    async def async_delete_protocol_forwarding(self, conf: dict[str, Any]) -> bool:
        """Delete protocol forwarding.

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "deleteProtocolForwarding", conf)

    async def async_get_protocol_forwarding(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get IPV4 protocol forwarding

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "getProtocolForwarding", conf)

    async def async_set_port_forwarding(self, conf: dict[str, Any]) -> str:
        """Set port forwarding.

        Arguments:
        - id (str) optional
        - origin (str)
        - sourceInterface (str)
        - externalPort (int) optional
        - internalPort (int)
        - destinationIPAddress (str)
        - sourcePrefix (str) optional
        - protocol (str)
        - enable (bool) optional
        - persistent (bool) optional
        - description (str) optional
        - destinationMACAddress (str) optional
        - leaseDuration (int) optional
        - upnpv1Compat (bool) optional

        Example:
        {"description":"FTP","persistent":true,"enable":true,"protocol":"6",
        "destinationIPAddress":"192.168.1.250","internalPort":"21",
        "externalPort":"21","origin":"webui","sourceInterface":"data",
        "sourcePrefix":"","id":"FTP"}}
        """
        return await self._auth.post("Firewall", "setPortForwarding", conf)

    async def async_refresh_port_forwarding(self, conf: dict[str, Any]) -> str:
        """Refresh port forwarding.

        Arguments:
        - id (str)
        - origin (str)
        - description (str) optional
        - persistent (bool) optional
        - leaseDuration (bool) optional
        """
        return await self._auth.post("Firewall", "refreshPortForwarding", conf)

    async def async_delete_port_forwarding(self, conf: dict[str, Any]) -> bool:
        """Refresh port forwarding.

        Arguments:
        - id (str) optional
        - origin (str)
        - destinationIPAddress (str) optional
        """
        return await self._auth.post("Firewall", "deletePortForwarding", conf)

    async def async_get_port_forwarding(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get port forwarding configuration

        Arguments:
        - id (str) optional
        - origin (str) optional

        Example: {"origin":"webui"}
        """
        return await self._auth.post("Firewall", "getPortForwarding", conf)

    async def async_enable_port_forwarding(self, conf: dict[str, Any]) -> None:
        """Get port forwarding configuration

        Arguments:
        - id (str)
        - origin (str)
        - enable (bool)
        """
        return await self._auth.post("Firewall", "enablePortForwarding", conf)

    async def async_set_pinhole(self, conf: dict[str, Any]) -> str:
        """Set pinhole.

        Arguments:
        - id (str) optional
        - origin (str)
        - sourceInterface (str)
        - sourcePort (int) optional
        - destinationPort (int)
        - destinationIPAddress (str)
        - sourcePrefix (str) optional
        - protocol (str)
        - ipversion (int) optional
        - enable (bool) optional
        - persistent (bool) optional
        - description (str) optional
        - destinationMACAddress (str) optional
        """
        return await self._auth.post("Firewall", "setPinhole", conf)

    async def async_delete_pinhole(self, conf: dict[str, Any]) -> bool:
        """Delete pinhole.

        Arguments:
        - id (str) optional
        - origin (str)
        """
        return await self._auth.post("Firewall", "deletePinhole", conf)

    async def async_get_upnp_Pinhole(
        self, conf: dict[str, Any] | None = None
    ) -> list[Any]:
        """Get pinhole.

        Arguments:
        - id (str) optional
        - origin (str) optional
        """
        return await self._auth.post("Firewall", "getPinhole", conf)

    async def async_set_firewall_DMZ(self, conf: dict[str, Any]) -> str:
        """Set DMZ.

        Arguments:
        - id (str) optional
        - sourceInterface (str)
        - destinationIPAddress (str)
        - sourcePrefix (str) optional
        - enable (bool)
        """
        return await self._auth.post("Firewall", "setDMZ", conf)

    async def async_delete_firewall_DMZ(self, conf: dict[str, Any]) -> bool:
        """Delete DMZ.

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "deleteDMZ", conf)

    async def async_get_firewall_DMZ(self, conf: dict[str, Any]) -> list[Any]:
        """Get DMZ.

        Arguments:
        - id (str)
        """
        return await self._auth.post("Firewall", "getDMZ", conf)

    async def async_set_custom_rule(self, conf: dict[str, Any]) -> str:
        """Set custom rule.

        Arguments:
        - id (str) optional
        - chain (str) optional
        - action (str)
        - destinationPort (str) optional
        - sourcePort (str) optional
        - destinationPrefix (str) optional
        - sourcePrefix (str) optional
        - protocol (str) optional
        - ipversion (int) optional
        - ipversion (str) optional
        - enable (bool) optional
        - description (str) optional
        - destinationMAC (str) optional
        - sourceMAC (str) optional
        - persistent (bool) optional
        """
        return await self._auth.post("Firewall", "setCustomRule", conf)

    async def async_delete_custom_rule(self, conf: dict[str, Any]) -> bool:
        """Delete custom rule.

        Arguments:
        - id (str)
        - chain (str) optional
        """
        return await self._auth.post("Firewall", "deleteCustomRule", conf)

    async def async_get_custom_rule(self, conf: dict[str, Any]) -> list[Any]:
        """Get custom rule.

        Arguments:
        - id (str) optional
        - chain (str) optional
        """
        return await self._auth.post("Firewall", "getCustomRule", conf)

    async def async_set_list_entry(self, conf: dict[str, Any]) -> None:
        """Set list entry.

        Arguments:
        - ilistNamed (str)
        - entryId (str)
        - destinationPrefix (str)
        - protocol (str)
        - enable (bool) optional
        - sourcePrefix (str) optional
        """
        return await self._auth.post("Firewall", "setListEntry", conf)

    async def async_delete_list_entry(self, conf: dict[str, Any]) -> None:
        """Delete list entry.

        Arguments:
        - listName (str)
        - entryId (str)
        """
        return await self._auth.post("Firewall", "deleteListEntry", conf)

    async def async_get_list_entry(self, conf: dict[str, Any]) -> list[Any]:
        """Get list entry.

        Arguments:
        - listName (str)
        - entryId (str) optional
        """
        return await self._auth.post("Firewall", "getListEntries", conf)

    async def async_set_firewall_Level(self, conf: dict[str, Any]) -> bool:
        """Set level for IPv4 Firewall

        Arguments:
        - level (str)

        Example: {"level":"Low"}
        """
        return await self._auth.post("Firewall", "setFirewallLevel", conf)

    async def async_set_firewall_IPv6Level(self, conf: dict[str, Any]) -> bool:
        """Set level for IPv6 Firewall

        Arguments:
        - level (str)

        Example: {"level":"Low"}
        """
        return await self._auth.post("Firewall", "setFirewallIPv6Level", conf)

    async def async_get_firewall_IPv6Level(self, conf: dict[str, Any]) -> str:
        """Get level for IPv6 Firewall

        Arguments:
        - level (str)

        Example: {"level":"Low"}
        """
        return await self._auth.post("Firewall", "getFirewallIPv6Level", conf)

    async def async_get_firewall_Level(self, conf: dict[str, Any]) -> str:
        """Get level for IPv4 Firewall

        Arguments:
        - level (str)

        Example: {"level":"Low"}
        """
        return await self._auth.post("Firewall", "getFirewallLevel", conf)

    # async def async_set_dns_name(
    #     self, mac: str, conf: dict[str, Any] | None = None
    # ) -> dict[str, Any]:
    #     """Set DNS name

    #     mac = '00:01:2B:3C:4D:5E'
    #     conf = {"parameters":{"name":"nestor","source":"dns"}}
    #     """
    #     return await self._auth.post("Devices/Device/" + mac, "setName", conf)


class UPnPIGD:
    """UPnP-IGD class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self) -> dict[str, Any]:
        """Get Upnp configuration."""
        return await self._auth.post("UPnP-IGD", "get")

    async def async_set(self, conf: dict[str, Any] | None = None) -> bool:
        """Set Upnp configuration.

        Argument:
        -parameters (dict) optional
        """
        return await self._auth.post("UPnP-IGD", "set", conf)


class SFP:
    """SFP information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self) -> dict[str, Any]:
        """Get Upnp configuration"""
        return await self._auth.post("SFP", "get")

    async def async_set_registration_id(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Set registration id.

        Argument:
        -RegistrationID (str) optional
        """
        return await self._auth.post("SFP", "setRegistrationID", conf)
