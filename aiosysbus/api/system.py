"""System information."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class System:  # pylint: disable=[too-many-public-methods]
    """System class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_led(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get LED information."""
        return await self._access.post("LED", "get", conf)

    # ############ PnP #############

    async def get_pnp(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Plug&play."""
        return await self._access.post("PnP", "get", conf)

    # ############ REMOTE ACCESS #############

    async def get_remoteaccess(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Remote access information."""
        return await self._access.post("RemoteAccess", "get", conf)

    async def set_remoteaccess(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set Remote access information."""
        return await self._access.post("RemoteAccess", "set", conf)

    async def get_remoteaccess_timeleft(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time left for remote access."""
        return await self._access.post("RemoteAccess", "getTimeLeft", conf)

    async def set_remoteaccess_restarttimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reset timer for remote access."""
        return await self._access.post("RemoteAccess", "restartTimer", conf)

    # ############ IOT #############

    async def get_iot_service(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get IoT Status."""
        return await self._access.post("IoTService", "getStatus", conf)

    # ############ PROBE #############

    async def get_probe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Wifi secure mode status."""
        return await self._access.post("Probe", "getStatus", conf)

    # ############ TIME #############

    async def get_time(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time information."""
        return await self._access.post("Time", "getTime", conf)

    async def get_utctime(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time information."""
        return await self._access.post("Time", "getUTCTime", conf)

    async def get_time_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time information."""
        return await self._access.post("Time", "getStatus", conf)

    async def get_time_ntp(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time information."""
        return await self._access.post("Time", "getNTPServers", conf)

    async def get_time_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get local  zone information."""
        return await self._access.post("Time", "getLocalTimeZoneName", conf)

    async def set_time_localtime_zonename(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set local zone information."""
        return await self._access.post("Time", "setLocalTimeZoneName", conf)

    # ############ NMC #############

    async def get_nmc(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WAN information."""
        return await self._access.post("NMC", "get", conf)

    async def set_nmc(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set WAN information."""
        return await self._access.post("NMC", "set", conf)

    async def get_wanmodelist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WAN status."""
        return await self._access.post("NMC", "getWanModeList", conf)

    async def set_wanmode(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get WAN status."""
        return await self._access.post("NMC", "setWanMode", conf)

    async def get_wanstatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WAN status."""
        return await self._access.post("NMC", "getWANStatus", conf)

    async def reset(self) -> dict[str, Any] | None:
        """Reset livebox."""
        return await self._access.post("NMC", "reset")

    async def reboot(self) -> dict[str, Any] | None:
        """Reboot livebox."""
        return await self._access.post("NMC", "reboot")

    async def disable_remoteaccess(self) -> dict[str, Any] | None:
        """Set disable remote access."""
        return await self._access.post("NMC", "disableRemoteAccess")

    async def enable_remoteaccess(self) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return await self._access.post("NMC", "enableRemoteAccess")

    async def get_versioninfo(self) -> dict[str, Any] | None:
        """Get update version info."""
        return await self._access.post("NMC", "updateVersionInfo")

    async def check_update(self) -> dict[str, Any] | None:
        """Check upgrade version."""
        return await self._access.post("NMC", "checkForUpgrades")

    async def get_datatracking(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get datatracking."""
        return await self._access.post("NMC.DataTracking", "get", conf)

    async def get_guest(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get guest."""
        return await self._access.post("NMC.Guest", "get", conf)

    async def set_guest(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set guest."""
        return await self._access.post("NMC.Guest", "set", conf)

    async def get_led_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get led status."""
        return await self._access.post("NMC.LED", "getLedStatus", conf)

    async def enable_networkconfig_bridge(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Enable bridge."""
        return await self._access.post("NMC.NetworkConfig", "enableNetworkBridge", conf)

    async def export_networkconfig_(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Backup network config."""
        return await self._access.post("NMC.NetworkConfig", "launchNetworkBackup", conf)

    async def import_networkconfig_(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Restore network config."""
        return await self._access.post(
            "NMC.NetworkConfig", "launchNetworkRestore", conf
        )

    async def get_networkconfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get saveset configuration."""
        return await self._access.post("NMC.NetworkConfig", "get", conf)

    async def get_orangetv_IPTVStatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get iptv status."""
        return await self._access.post("NMC.OrangeTV", "getIPTVStatus", conf)

    async def get_orangetv_IPTVConfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get iptv information."""
        return await self._access.post("NMC.OrangeTV", "getIPTVConfig", conf)

    async def get_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get multiscreeens for iptv."""
        return await self._access.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    async def set_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get multiscreeens for iptv."""
        return await self._access.post("NMC.OrangeTV", "setIPTVMultiScreens", conf)

    async def get_profiles(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Profiles."""
        return await self._access.post("NMC.Profiles", "get", conf)

    async def get_autodetect(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Autodetect."""
        return await self._access.post("NMC.Autodetect", "get", conf)

    async def set_tppp(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get username."""
        return await self._access.post("NMC.TPPP", "force", conf)

    async def get_acs(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get ACS."""
        return await self._access.post("NMC.ACS", "get", conf)

    async def get_wlantimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WLAN timer."""
        return await self._access.post("NMC.WlanTimer", "getActivationTimer", conf)

    async def set_wlantimer(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Det WLAN timer."""
        return await self._access.post("NMC.WlanTimer", "setActivationTimer", conf)

    async def disable_wlantimer(self) -> dict[str, Any] | None:
        """Disable WLAN timer."""
        return await self._access.post("NMC.WlanTimer", "disableActivationTimer")

    # ############ HOSTS #############

    async def get_hosts(self) -> dict[str, Any] | None:
        """Get devices."""
        return await self._access.post("Hosts", "getDevices")

    async def set_hosts_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set host name."""
        return await self._access.post("Hosts", "setName", conf)

    async def del_hosts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove hosts."""
        return await self._access.post("Hosts", "delHost", conf)

    async def set_hosts_device(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set host device."""
        return await self._access.post("Hosts", "setDevice", conf)
