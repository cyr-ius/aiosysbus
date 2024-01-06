"""System information."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class System:
    """System class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_led(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get LED information."""
        return await self._auth.post("LED", "get", conf)

    # ############ PnP #############

    async def async_get_pnp(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get Plug&play."""
        return await self._auth.post("PnP", "get", conf)

    # ############ REMOTE auth #############

    async def async_get_remoteauth(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Remote auth information."""
        return await self._auth.post("Remoteauth", "get", conf)

    async def async_set_remoteauth(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set Remote auth information."""
        return await self._auth.post("Remoteauth", "set", conf)

    async def async_get_remoteauth_timeleft(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get time left for remote auth."""
        return await self._auth.post("Remoteauth", "getTimeLeft", conf)

    async def async_set_remoteauth_restarttimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Reset timer for remote auth."""
        return await self._auth.post("Remoteauth", "restartTimer", conf)

    # ############ IOT #############

    async def async_get_iot_service(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get IoT Status."""
        return await self._auth.post("IoTService", "getStatus", conf)

    # ############ PROBE #############

    async def async_get_probe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Wifi secure mode status."""
        return await self._auth.post("Probe", "getStatus", conf)

    # ############ TIME #############

    async def async_get_time(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get time information."""
        return await self._auth.post("Time", "getTime", conf)

    async def async_get_utctime(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get time information."""
        return await self._auth.post("Time", "getUTCTime", conf)

    async def async_get_time_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get time information."""
        return await self._auth.post("Time", "getStatus", conf)

    async def async_get_time_ntp(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get time information."""
        return await self._auth.post("Time", "getNTPServers", conf)

    async def async_get_time_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get local  zone information."""
        return await self._auth.post("Time", "getLocalTimeZoneName", conf)

    async def async_set_time_localtime_zonename(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set local zone information."""
        return await self._auth.post("Time", "setLocalTimeZoneName", conf)

    # ############ NMC #############

    async def async_get_nmc(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get WAN information."""
        return await self._auth.post("NMC", "get", conf)

    async def async_set_nmc(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set WAN information."""
        return await self._auth.post("NMC", "set", conf)

    async def async_get_wanmodelist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get WAN status."""
        return await self._auth.post("NMC", "getWanModeList", conf)

    async def async_set_wanmode(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Get WAN status."""
        return await self._auth.post("NMC", "setWanMode", conf)

    async def async_get_wanstatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get WAN status."""
        return await self._auth.post("NMC", "getWANStatus", conf)

    async def async_reset(self) -> dict[str, Any]:
        """Reset livebox."""
        return await self._auth.post("NMC", "reset")

    async def async_reboot(self) -> dict[str, Any]:
        """Reboot livebox."""
        return await self._auth.post("NMC", "reboot")

    async def async_disable_remoteauth(self) -> dict[str, Any]:
        """Set disable remote auth."""
        return await self._auth.post("NMC", "disableRemoteauth")

    async def async_enable_remoteauth(self) -> dict[str, Any]:
        """Set  enable remote auth."""
        return await self._auth.post("NMC", "enableRemoteauth")

    async def async_get_versioninfo(self) -> dict[str, Any]:
        """Get update version info."""
        return await self._auth.post("NMC", "updateVersionInfo")

    async def async_check_update(self) -> dict[str, Any]:
        """Check upgrade version."""
        return await self._auth.post("NMC", "checkForUpgrades")

    async def async_get_datatracking(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get datatracking."""
        return await self._auth.post("NMC.DataTracking", "get", conf)

    async def async_get_guest(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get guest."""
        return await self._auth.post("NMC.Guest", "get", conf)

    async def async_set_guest(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set guest."""
        return await self._auth.post("NMC.Guest", "set", conf)

    async def async_get_led_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get led status."""
        return await self._auth.post("NMC.LED", "getLedStatus", conf)

    async def async_enable_networkconfig_bridge(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Enable bridge."""
        return await self._auth.post("NMC.NetworkConfig", "enableNetworkBridge", conf)

    async def async_export_networkconfig_(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Backup network config."""
        return await self._auth.post("NMC.NetworkConfig", "launchNetworkBackup", conf)

    async def async_import_networkconfig_(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Restore network config."""
        return await self._auth.post("NMC.NetworkConfig", "launchNetworkRestore", conf)

    async def async_get_networkconfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get saveset configuration."""
        return await self._auth.post("NMC.NetworkConfig", "get", conf)

    async def async_get_orangetv_IPTVStatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get iptv status."""
        return await self._auth.post("NMC.OrangeTV", "getIPTVStatus", conf)

    async def async_get_orangetv_IPTVConfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get iptv information."""
        return await self._auth.post("NMC.OrangeTV", "getIPTVConfig", conf)

    async def async_get_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get multiscreeens for iptv."""
        return await self._auth.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    async def async_set_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get multiscreeens for iptv."""
        return await self._auth.post("NMC.OrangeTV", "setIPTVMultiScreens", conf)

    async def async_get_profiles(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Profiles."""
        return await self._auth.post("NMC.Profiles", "get", conf)

    async def async_get_autodetect(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Autodetect."""
        return await self._auth.post("NMC.Autodetect", "get", conf)

    async def async_set_tppp(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Get username."""
        return await self._auth.post("NMC.TPPP", "force", conf)

    async def async_get_acs(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get ACS."""
        return await self._auth.post("NMC.ACS", "get", conf)

    async def async_get_wlantimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get WLAN timer."""
        return await self._auth.post("NMC.WlanTimer", "getActivationTimer", conf)

    async def async_set_wlantimer(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Det WLAN timer."""
        return await self._auth.post("NMC.WlanTimer", "setActivationTimer", conf)

    async def async_disable_wlantimer(self) -> dict[str, Any]:
        """Disable WLAN timer."""
        return await self._auth.post("NMC.WlanTimer", "disableActivationTimer")

    # ############ HOSTS #############

    async def async_get_hosts(self) -> dict[str, Any]:
        """Get devices."""
        return await self._auth.post("Hosts", "getDevices")

    async def async_set_hosts_name(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set host name."""
        return await self._auth.post("Hosts", "setName", conf)

    async def async_del_hosts(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Remove hosts."""
        return await self._auth.post("Hosts", "delHost", conf)

    async def async_set_hosts_device(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set host device."""
        return await self._auth.post("Hosts", "setDevice", conf)
