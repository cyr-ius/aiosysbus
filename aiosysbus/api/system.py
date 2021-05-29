"""System information."""

class System:
    """System class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_led(self, conf=None):
        """Get LED information."""
        return self._access.post("LED", "get", conf)

    # ############ PnP #############

    def get_pnp(self, conf=None):
        """Get Plug&play."""
        return self._access.post("PnP", "get", conf)

    # ############ REMOTE ACCESS #############

    def get_remoteaccess(self, conf=None):
        """Get Remote access information."""
        return self._access.post("RemoteAccess", "get", conf)

    def set_remoteaccess(self, conf=None):
        """Set Remote access information."""
        return self._access.post("RemoteAccess", "set", conf)

    def get_remoteaccess_timeleft(self, conf=None):
        """Get time left for remote access."""
        return self._access.post("RemoteAccess", "getTimeLeft", conf)

    def set_remoteaccess_restarttimer(self, conf=None):
        """Reset timer for remote access."""
        return self._access.post("RemoteAccess", "restartTimer", conf)

    # ############ IOT #############

    def get_iot_service(self, conf=None):
        """Get IoT Status."""
        return self._access.post("IoTService", "getStatus", conf)

    # ############ PROBE #############

    def get_probe(self, conf=None):
        """Get Wifi secure mode status."""
        return self._access.post("Probe", "getStatus", conf)

    # ############ TIME #############

    def get_time(self, conf=None):
        """Get time information."""
        return self._access.post("Time", "getTime", conf)

    def get_utctime(self, conf=None):
        """Get time information."""
        return self._access.post("Time", "getUTCTime", conf)

    def get_time_status(self, conf=None):
        """Get time information."""
        return self._access.post("Time", "getStatus", conf)

    def get_time_ntp(self, conf=None):
        """Get time information."""
        return self._access.post("Time", "getNTPServers", conf)

    def get_time_localtime_zonename(self, conf=None):
        """Get local  zone information."""
        return self._access.post("Time", "getLocalTimeZoneName", conf)

    def set_time_localtime_zonename(self, conf):
        """Set local zone information."""
        return self._access.post("Time", "setLocalTimeZoneName", conf)

    # ############ NMC #############

    def get_nmc(self, conf=None):
        """Get WAN information."""
        return self._access.post("NMC", "get", conf)

    def set_nmc(self, conf):
        """Set WAN information."""
        return self._access.post("NMC", "set", conf)

    def get_wanmodelist(self, conf=None):
        """Get WAN status."""
        return self._access.post("NMC", "getWanModeList", conf)

    def set_wanmode(self, conf):
        """Get WAN status."""
        return self._access.post("NMC", "setWanMode", conf)

    def get_wanstatus(self, conf=None):
        """Get WAN status."""
        return self._access.post("NMC", "getWANStatus", conf)

    def reset(self):
        """Reset livebox."""
        return self._access.post("NMC", "reset")

    def reboot(self):
        """Reboot livebox."""
        return self._access.post("NMC", "reboot")

    # def get_lan_ip(self, conf=None):
    #     """Reboot livebox."""
    #     return self._access.post("NMC", "getLANIP", conf)

    # def set_lan_ip(self, conf=None):
    #     """Reboot livebox."""
    #     return self._access.post("NMC", "setLANIP", conf)

    # def get_remoteaccess(self):
    #     """Set disable remote access."""
    #     return self._access.post("NMC", "getRemoteAccess")

    def disable_remoteaccess(self):
        """Set disable remote access."""
        return self._access.post("NMC", "disableRemoteAccess")

    def enable_remoteaccess(self):
        """Set  enable remote access."""
        return self._access.post("NMC", "enableRemoteAccess")

    def get_versioninfo(self):
        """Get update version info."""
        return self._access.post("NMC", "updateVersionInfo")

    def check_update(self):
        """Check upgrade version."""
        return self._access.post("NMC", "checkForUpgrades")

    def get_datatracking(self, conf=None):
        """Get datatracking."""
        return self._access.post("NMC.DataTracking", "get", conf)

    # def get_IPv6(self, conf=None):
    #     """Get IPv6 information."""
    #     return self._access.post("NMC.IPv6", "get", conf)

    # def set_IPv6(self, conf):
    #     """Set IPv6 information."""
    #     return self._access.post("NMC.IPv6", "set", conf)

    def get_guest(self, conf=None):
        """Get guest."""
        return self._access.post("NMC.Guest", "get", conf)

    def set_guest(self, conf):
        """Set guest."""
        return self._access.post("NMC.Guest", "set", conf)

    def get_led_status(self, conf=None):
        """Get led status."""
        return self._access.post("NMC.LED", "getLedStatus", conf)

    def enable_networkconfig_bridge(self, conf=None):
        """Enable bridge."""
        return self._access.post("NMC.NetworkConfig", "enableNetworkBridge", conf)

    def export_networkconfig_(self, conf=None):
        """Backup network config."""
        return self._access.post("NMC.NetworkConfig", "launchNetworkBackup", conf)

    def import_networkconfig_(self, conf):
        """Restore network config."""
        return self._access.post("NMC.NetworkConfig", "launchNetworkRestore", conf)

    def get_networkconfig(self, conf=None):
        """Get saveset configuration."""
        return self._access.post("NMC.NetworkConfig", "get", conf)

    # def set_networkconfig_NetworkBR(self, conf={"parameters": {"state": "true"}}):
    #     """Save configuration."""
    #     return self._access.post("NMC.NetworkConfig", "enableNetworkBR", conf)

    def get_orangetv_IPTVStatus(self, conf=None):
        """Get iptv status."""
        return self._access.post("NMC.OrangeTV", "getIPTVStatus", conf)

    def get_orangetv_IPTVConfig(self, conf=None):
        """Get iptv information."""
        return self._access.post("NMC.OrangeTV", "getIPTVConfig", conf)

    def get_orangetv_IPTVMultiScreens(self, conf=None):
        """Get multiscreeens for iptv."""
        return self._access.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    def set_orangetv_IPTVMultiScreens(self, conf=None):
        """Get multiscreeens for iptv."""
        return self._access.post("NMC.OrangeTV", "setIPTVMultiScreens", conf)

    def get_profiles(self, conf=None):
        """Get Profiles."""
        return self._access.post("NMC.Profiles", "get", conf)

    def get_autodetect(self, conf=None):
        """Autodetect."""
        return self._access.post("NMC.Autodetect", "get", conf)

    def set_tppp(self, conf):
        """Get username."""
        return self._access.post("NMC.TPPP", "force", conf)

    def get_acs(self, conf=None):
        """Get ACS."""
        return self._access.post("NMC.ACS", "get", conf)

    def get_wlantimer(self, conf=None):
        """Get WLAN timer."""
        return self._access.post("NMC.WlanTimer", "getActivationTimer", conf)

    def set_wlantimer(self, conf):
        """Det WLAN timer."""
        return self._access.post("NMC.WlanTimer", "setActivationTimer", conf)

    def disable_wlantimer(self):
        """Disable WLAN timer."""
        return self._access.post("NMC.WlanTimer", "disableActivationTimer")

    # def start_wifi_pairing(self):
    #     """Wifi start pairing."""
    #     return self._access.post("NMC.Wifi", "startPairing")

    # def stop_wifi_pairing(self):
    #     """Wifi stop pairing."""
    #     return self._access.post("NMC.Wifi", "stopPairing")

    # def start_wifi_autochannel(self):
    #     """Wifi select auto channel."""
    #     return self._access.post("NMC.Wifi", "startAutoChannelSelection")

    # def get_wifi(self, conf=None):
    #     """Get Wifi."""
    #     return self._access.post("NMC.Wifi", "get", conf)

    # def set_wifi(self, conf):
    #     """Set Wifi."""
    #     return self._access.post("NMC.Wifi", "set", conf)

    # ############ HOSTS #############

    def get_hosts(self=None):
        """Get devices."""
        return self._access.post("Hosts", "getDevices")

    def set_hosts_name(self, conf):
        """Set host name."""
        return self._access.post("Hosts", "setName", conf)

    def del_hosts(self, conf):
        """Remove hosts."""
        return self._access.post("Hosts", "delHost", conf)

    def set_hosts_device(self, conf):
        """Set host device."""
        return self._access.post("Hosts", "setDevice", conf)
