"""NMC."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class Nmc:
    """Event class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self) -> dict[str, Any]:
        """Get NMC."""
        return await self._auth.post("NMC", "get")

    async def async_set(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Set NMC.

        Argument:
        - parameters (dict) optional
        """
        return await self._auth.post("NMC", "set", conf)

    async def async_set_wanmode(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Set WAN mode.

        Argument:
        - WanMode (str)
        - Username (str) optional
        - Password (str) optional
        """
        return await self._auth.post("NMC", "setWanMode", conf)

    async def async_get_wanmodelist(self) -> str:
        """Get WAN mode list."""
        return await self._auth.post("NMC", "getWanModeList")

    async def async_get_wan_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set WAN mode.

        Argument:
        - LinkType (str) optional
        - LinkState (str) optional
        - WanState (str) optional
        - MACAddress (str) optional
        - Protocol (str) optional
        - ConnectionState (str) optional
        - LastConnectionError (str) optional
        - IPAddress (str) optional
        - RemoteGateway (str) optional
        - DNSServers (str) optional
        """
        return await self._auth.post("NMC", "getWANStatus", conf)

    async def async_reset(self, conf: dict[str, Any] | None = None) -> None:
        """Reset livebox.

        Argument:
        - reason (str) optional
        """
        return await self._auth.post("NMC", "reset", conf)

    async def async_reboot(self, conf: dict[str, Any] | None = None) -> None:
        """Reboot livebox.

        Argument:
        - reason (str) optional
        """
        return await self._auth.post("NMC", "reboot", conf)

    async def async_set_lan_ip(self, conf: dict[str, Any]) -> None:
        """Set Lan ip.

        Arguments:
        - Address (str)
        - Netmask (str)
        - DHCPEnable (bool)
        - DHCPMinAddress (str)
        - DHCPMaxAddress (str)
        - LeaseTime (int) optional
        """
        return await self._auth.post("NMC", "setLANIP", conf)

    async def async_get_lan_ip(self, conf: dict[str, Any] | None = None) -> None:
        """Get Lan ip.

        Arguments:
        - Address (str) optional
        - Netmask (str) optional
        - DHCPEnable (bool) optional
        - DHCPMinAddress (str) optional
        - DHCPMaxAddress (str) optional
        - LeaseTime (int) optional
        """
        return await self._auth.post("NMC", "getLANIP", conf)

    async def async_shutdown(self, conf: dict[str, Any] | None = None) -> None:
        """Shutdown livebox.

        Argument:
        - reason (str) optional
        """
        return await self._auth.post("NMC", "shutdown", conf)

    async def async_enable_remote_access(
        self, conf: dict[str, Any] | None = None
    ) -> int:
        """Set  enable remote access.

        Arguments:
        - username (str) optional
        - password (str) optional
        - port (int) optional
        - timeout (int) optional
        - sourcePrefix (str) optional
        - accessType (str) optional
        - secure (bool) optional
        """
        return await self._auth.post("NMC", "enableRemoteAccess", conf)

    async def async_get_remote_access(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get remote access.

        Arguments:
        - username (str) optional
        - usertype (str) optional
        """
        return await self._auth.post("NMC", "getRemoteAccess", conf)

    async def async_disable_remote_access(
        self, conf: dict[str, Any] | None = None
    ) -> int:
        """Get remote access.

        Arguments:
        - accessType (str) optional
        """
        return await self._auth.post("NMC", "disableRemoteAccess", conf)

    async def async_update_versioninfo(self) -> None:
        """Update version info."""
        return await self._auth.post("NMC", "updateVersionInfo")

    async def async_check_upgrade(self) -> bool:
        """Check upgrade version."""
        return await self._auth.post("NMC", "checkForUpgrades")

    async def async_get_voip(self) -> list[dict[str, Any]]:
        """Get VIOP configuration."""
        return await self._auth.post("NMC", "getVoIPConfig")

    # NMC.Error

    async def async_get_error_code(self) -> list[dict[str, Any]]:
        """Get primary error code."""
        return await self._auth.post("NMC.Error", "getPrimaryErrorCode")

    # NMC.IPv6

    async def async_set_IPv6(self, conf: dict[str, Any] | None = None) -> None:
        """Set IPv6 information.

        Arguments:
        - Enable (bool) optional
        - UserRequested (bool) optional
        - IPv4UserRequested (bool) optional
        """
        return await self._auth.post("NMC.IPv6", "set", conf)

    async def async_get_IPv6(self, conf: dict[str, Any] | None = None) -> None:
        """Get IPv6 information.

        Arguments:
        - Enable (bool) optional
        - IPv6Address (str) optional
        """
        return await self._auth.post("NMC.IPv6", "get", conf)

    # NMC.Container

    async def async_set_container(self, conf: dict[str, Any] | None = None) -> None:
        """Set container.

        Arguments:
        - Address (str) optional
        - Netmask (str) optional
        - DHCPEnable (bool) optional
        - DHCPMinAddress (str) optional
        - DHCPMaxAddress (str) optional
        - LeaseTime (int) optional
        """
        return await self._auth.post("NMC.Container", "set", conf)

    async def async_get_container(self, conf: dict[str, Any] | None = None) -> None:
        """Get container.

        Arguments:
        - Status (str) optional
        - Address (str) optional
        - Netmask (str) optional
        - DHCPEnable (bool) optional
        - DHCPMinAddress (str) optional
        - DHCPMaxAddress (str) optional
        - LeaseTime (int) optional
        """
        return await self._auth.post("NMC.Container", "get", conf)

    # NMC.LED

    async def async_get_led_status(self, conf: dict[str, Any] | None = None) -> None:
        """Get led status.

        Arguments:
        - name (str) optional
        - state (str) optional
        - color (str) optional
        """
        return await self._auth.post("NMC.LED", "getLedStatus", conf)

    async def async_set_led(self, conf: dict[str, Any]) -> bool:
        """Set led.

        Arguments:
        - name (str)
        - state (str)
        - color (str)
        """
        return await self._auth.post("NMC.LED", "setLedStatus", conf)

    # NMC.NetworkConfig

    async def async_enable_network_bridge(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Enable bridge.

        Argument:
        - state (bool) optional
        """
        return await self._auth.post("NMC.NetworkConfig", "enableNetworkBR", conf)

    async def async_backup_network(self, conf: dict[str, Any] | None = None) -> None:
        """Backup network config.

        Argument:
        - delay (bool) optional
        """
        return await self._auth.post("NMC.NetworkConfig", "launchNetworkBackup", conf)

    async def async_restore_network(self) -> None:
        """Restore network config."""
        return await self._auth.post("NMC.NetworkConfig", "launchNetworkRestore")

    async def async_get_network(self) -> None:
        """Get network configuration."""
        return await self._auth.post("NMC.NetworkConfig", "get")

    # NMC.NetworkConfig

    async def async_get_iptv_status(self, conf: dict[str, Any] | None = None) -> None:
        """Get iptv status.

        Argument:
        - IPTVStatus (str) optional
        """
        return await self._auth.post("NMC.OrangeTV", "getIPTVStatus", conf)

    async def async_set_iptv_multi_screens(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Get multiscreeens for iptv.

        Argument:
        - Enable (bool) optional
        """
        return await self._auth.post("NMC.OrangeTV", "setIPTVMultiScreens", conf)

    async def async_get_iptv_multi_screens(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Get multiscreeens for iptv.

        Argument:
        - Enable (bool) optional
        """
        return await self._auth.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    async def async_get_iptv_config(self) -> list[Any]:
        """Get iptv information."""
        return await self._auth.post("NMC.OrangeTV", "getIPTVConfig")

    # NMC.Wifi

    async def async_set_wifi_enable(self, conf: dict[str, Any]) -> None:
        """Set enable wifi.

        Arguments:
        - value (bool)
        - temporary (bool) optional
        - source (src) optional
        """
        return await self._auth.post("NMC.Wifi", "setEnable", conf)

    async def async_toggle_wifi_enable(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Toggle enable wifi.

        Arguments:
        - temporary (bool) optional
        - source (str) optional
        """
        return await self._auth.post("NMC.Wifi", "toggleEnable", conf)

    async def async_start_wifi_pairing(self, conf: dict[str, Any]) -> None:
        """Wifi start pairing.

        Arguments:
        - clientPIN (str)
        """
        return await self._auth.post("NMC.Wifi", "startPairing")

    async def async_stop_wifi_pairing(self) -> None:
        """Wifi stop pairing."""
        return await self._auth.post("NMC.Wifi", "stopPairing")

    async def async_start_wifi_autochannel(self) -> None:
        """Wifi select auto channel."""
        return await self._auth.post("NMC.Wifi", "startAutoChannelSelection")

    async def async_get_wifi_stats(self, conf: dict[str, Any] | None = None) -> None:
        """Wifi Statistics.

        Arguments:
        - RxBytes (int) optional
        - TxBytes (int) optional
        """
        return await self._auth.post("NMC.Wifi", "getStats", conf)

    async def async_set_wifi(self, conf: dict[str, Any] | None = None) -> None:
        """Set wifi configuration.

        Arguments:
        - Enable (bool) optional
        - Status (bool) optional
        - ConfigurationMode (bool) optional
        - TriggerAutoChannelSelection (bool) optional
        """
        return await self._auth.post("NMC.Wifi", "set", conf)

    async def async_get_wifi(self) -> dict[str, Any]:
        """Get wifi configuration."""
        return await self._auth.post("NMC.Wifi", "get")

    async def async_set_wifi_interval(self, conf: dict[str, Any] | None = None) -> None:
        """Wifi interval.

        Arguments:
        - EnableTarget (str) optional
        """
        return await self._auth.post("NMC.Wifi", "setInternal", conf)

    async def async_set_wifi_status(self, conf: dict[str, Any] | None = None) -> None:
        """Wifi interval.

        Arguments:
        - Status (bool) optional
        """
        return await self._auth.post("NMC.Wifi", "setStatus", conf)

    async def async_wifi_debug(self) -> None:
        """Debug wifi."""
        return await self._auth.post("NMC.Wifi", "debug")

    # NMC.Wifi.WPS

    async def async_generate_wps_pin(self) -> None:
        """Generate WPS PIN."""
        return await self._auth.post("NMC.Wifi.WPS", "generateSelfPIN")

    # NMC.Reboot

    async def async_flush_reboot(self) -> None:
        """Flush while reboot."""
        return await self._auth.post("NMC.Reboot", "flush")

    # NMC.Autodetect

    async def async_autodetect(self) -> dict[str, Any]:
        """Get autodetect."""
        return await self._auth.post("NMC.Autodetect", "get")

    # NMC.TPPP

    async def async_tppp_force(self) -> bool:
        """Force tppp."""
        return await self._auth.post("NMC.TPPP", "force")

    # NMC.WlanClear

    async def async_wlan_clear(self, conf: dict[str, Any] | None = None) -> bool:
        """Wlan clear.

        Arguments:
        - ID (str) optional
        - state (str) optional
        """
        return await self._auth.post("NMC.WlanClear", "setState", conf)

    # NMC.WlanTimer

    async def async_set_wlan_timer(
        self, timeout: int = 0, interfacename: str = "guest"
    ) -> None:
        """Set WLAN timer.
        Arguments:
        - Timeout (int) 0 == infinite
        - InterfaceName (str) Interface name
        """

        conf = {"Timeout": timeout, "InterfaceName": interfacename}
        return await self._auth.post("NMC.WlanTimer", "setActivationTimer", conf)

    async def async_get_wlan_timer(self, interfacename: str = "guest") -> int:
        """Get WLAN timer.

        Arguments:
        - InterfaceName (str) Interface name
        """
        conf = {"InterfaceName": interfacename}
        return await self._auth.post("NMC.WlanTimer", "getActivationTimer", conf)

    async def async_disable_wlan_timer(self, interfacename: str = "guest") -> bool:
        """Disable WLAN timer.

        Arguments:
        - InterfaceName (str) Interface name
        """
        conf = {"InterfaceName": interfacename}
        return await self._auth.post("NMC.WlanTimer", "disableActivationTimer", conf)

    # NMC.Guest

    async def async_set_guest_wifi(self, enable: bool) -> None:
        """Set guest wifi.

        Arguments:
        - Enable (bool)
        """
        conf = {"Enable": enable is True}
        return await self._auth.post("NMC.Guest", "set", conf)

    async def async_get_guest_wifi(self) -> None:
        """Get wifi configuration."""
        return await self._auth.post("NMC.Guest", "get")

    # Custom method.
    async def async_guest_wifi(
        self, enable: bool, *, timeout: int = 0, interface: str = "guest"
    ) -> None:
        """Set guest wifi and timer.

        Arguments:
        - Enable (bool)
        - Timeout (int) seconds
        - Interface (str) Interface name
        """
        if enable:
            await self.async_set_guest_wifi(enable)
            return await self.async_set_wlan_timer(timeout, interface)
        await self.async_set_guest_wifi(enable)
        return await self.async_disable_wlan_timer(timeout, interface)
