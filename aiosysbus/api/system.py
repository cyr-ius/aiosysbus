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

    def get_led(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get LED information."""
        return self._access.post("LED", "get", conf)

    # ############ PnP #############

    def get_pnp(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get Plug&play."""
        return self._access.post("PnP", "get", conf)

    # ############ REMOTE ACCESS #############

    def get_remoteaccess(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Remote access information."""
        return self._access.post("RemoteAccess", "get", conf)

    def set_remoteaccess(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set Remote access information."""
        return self._access.post("RemoteAccess", "set", conf)

    def get_remoteaccess_timeleft(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time left for remote access."""
        return self._access.post("RemoteAccess", "getTimeLeft", conf)

    def set_remoteaccess_restarttimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reset timer for remote access."""
        return self._access.post("RemoteAccess", "restartTimer", conf)

    # ############ IOT #############

    def get_iot_service(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get IoT Status."""
        return self._access.post("IoTService", "getStatus", conf)

    # ############ PROBE #############

    def get_probe(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get Wifi secure mode status."""
        return self._access.post("Probe", "getStatus", conf)

    # ############ TIME #############

    def get_time(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get time information."""
        return self._access.post("Time", "getTime", conf)

    def get_utctime(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get time information."""
        return self._access.post("Time", "getUTCTime", conf)

    def get_time_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time information."""
        return self._access.post("Time", "getStatus", conf)

    def get_time_ntp(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get time information."""
        return self._access.post("Time", "getNTPServers", conf)

    def get_time_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get local  zone information."""
        return self._access.post("Time", "getLocalTimeZoneName", conf)

    def set_time_localtime_zonename(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set local zone information."""
        return self._access.post("Time", "setLocalTimeZoneName", conf)

    # ############ NMC #############

    def get_nmc(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get WAN information."""
        return self._access.post("NMC", "get", conf)

    def set_nmc(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set WAN information."""
        return self._access.post("NMC", "set", conf)

    def get_wanmodelist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WAN status."""
        return self._access.post("NMC", "getWanModeList", conf)

    def set_wanmode(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get WAN status."""
        return self._access.post("NMC", "setWanMode", conf)

    def get_wanstatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WAN status."""
        return self._access.post("NMC", "getWANStatus", conf)

    def reset(self) -> dict[str, Any] | None:
        """Reset livebox."""
        return self._access.post("NMC", "reset")

    def reboot(self) -> dict[str, Any] | None:
        """Reboot livebox."""
        return self._access.post("NMC", "reboot")

    def disable_remoteaccess(self) -> dict[str, Any] | None:
        """Set disable remote access."""
        return self._access.post("NMC", "disableRemoteAccess")

    def enable_remoteaccess(self) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return self._access.post("NMC", "enableRemoteAccess")

    def get_versioninfo(self) -> dict[str, Any] | None:
        """Get update version info."""
        return self._access.post("NMC", "updateVersionInfo")

    def check_update(self) -> dict[str, Any] | None:
        """Check upgrade version."""
        return self._access.post("NMC", "checkForUpgrades")

    def get_datatracking(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get datatracking."""
        return self._access.post("NMC.DataTracking", "get", conf)

    def get_guest(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get guest."""
        return self._access.post("NMC.Guest", "get", conf)

    def set_guest(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set guest."""
        return self._access.post("NMC.Guest", "set", conf)

    def get_led_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get led status."""
        return self._access.post("NMC.LED", "getLedStatus", conf)

    def enable_networkconfig_bridge(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Enable bridge."""
        return self._access.post("NMC.NetworkConfig", "enableNetworkBridge", conf)

    def export_networkconfig_(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Backup network config."""
        return self._access.post("NMC.NetworkConfig", "launchNetworkBackup", conf)

    def import_networkconfig_(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Restore network config."""
        return self._access.post("NMC.NetworkConfig", "launchNetworkRestore", conf)

    def get_networkconfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get saveset configuration."""
        return self._access.post("NMC.NetworkConfig", "get", conf)

    def get_orangetv_IPTVStatus(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get iptv status."""
        return self._access.post("NMC.OrangeTV", "getIPTVStatus", conf)

    def get_orangetv_IPTVConfig(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get iptv information."""
        return self._access.post("NMC.OrangeTV", "getIPTVConfig", conf)

    def get_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get multiscreeens for iptv."""
        return self._access.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    def set_orangetv_IPTVMultiScreens(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get multiscreeens for iptv."""
        return self._access.post("NMC.OrangeTV", "setIPTVMultiScreens", conf)

    def get_profiles(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get Profiles."""
        return self._access.post("NMC.Profiles", "get", conf)

    def get_autodetect(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Autodetect."""
        return self._access.post("NMC.Autodetect", "get", conf)

    def set_tppp(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get username."""
        return self._access.post("NMC.TPPP", "force", conf)

    def get_acs(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get ACS."""
        return self._access.post("NMC.ACS", "get", conf)

    def get_wlantimer(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get WLAN timer."""
        return self._access.post("NMC.WlanTimer", "getActivationTimer", conf)

    def set_wlantimer(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Det WLAN timer."""
        return self._access.post("NMC.WlanTimer", "setActivationTimer", conf)

    def disable_wlantimer(self) -> dict[str, Any] | None:
        """Disable WLAN timer."""
        return self._access.post("NMC.WlanTimer", "disableActivationTimer")

    # ############ HOSTS #############

    def get_hosts(self) -> dict[str, Any] | None:
        """Get devices."""
        return self._access.post("Hosts", "getDevices")

    def set_hosts_name(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set host name."""
        return self._access.post("Hosts", "setName", conf)

    def del_hosts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove hosts."""
        return self._access.post("Hosts", "delHost", conf)

    def set_hosts_device(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set host device."""
        return self._access.post("Hosts", "setDevice", conf)
