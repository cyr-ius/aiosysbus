class System:
    def __init__(self, access):
        self._access = access

    def get_deviceinfo(self, conf=None):
        """ Get device information """
        return self._access.post("DeviceInfo", "get", conf)

    def get_devices(self, conf=None):
        """ Get devices """
        return self._access.post("Devices", "get", conf)

    def get_led(self, conf=None):
        """ Get LED information """
        return self._access.post("LED", "get", conf)

    def get_usbhosts(self, conf=None):
        """ Get USB Hosts """
        return self._access.post("USBHosts", "get", conf)

    def checkForUpgrades(self):
        """ Check upgrade version """
        return self._access.post("NMC", "checkForUpgrades")

    def disableRemoteAccess(self):
        """ Set disable remote access """
        return self._access.post("NMC", "disableRemoteAccess")

    def enableRemoteAccess(self):
        """ Set  enable remote acess """
        return self._access.post("NMC", "enableRemoteAccess")

    def get_nmc(self, conf=None):
        """ Get WAN information """
        return self._access.post("NMC", "get", conf)

    def get_WANStatus(self, conf=None):
        """ Get WAN status """
        return self._access.post("NMC", "getWANStatus", conf)

    def reboot(self):
        """ Reboot livebox """
        return self._access.post("NMC", "reboot")

    def reset(self):
        """ Reset livebox """
        return self._access.post("NMC", "reset")

    def set_WanMode(self, conf):
        """
        Set WAN Mode
        {"parameters":{"WanMode":"WanMode","Username":"pnp/orange2","Password":"orange"}}
        """
        return self._access.post("NMC", "setWanMode", conf)

    def username(self):
        """ Get username """
        return self._access.post("NMC", "Username")

    def get_remoteaccess(self, conf=None):
        """ Get Remote access information """
        return self._access.post("RemoteAccess", "get", conf)

    def get_usermanagement(self, conf=None):
        """ Get users information """
        return self._access.post("UserManagement", "getUsers", conf)

    def get_guest(self, conf=None):
        """ Get guests """
        return self._access.post("NMC.Guest", "get", conf)

    def get_orangetv_IPTVStatus(self, conf=None):
        """ Get iptv status """
        return self._access.post("NMC.OrangeTV", "getIPTVStatus", conf)

    def get_orangetv_IPTVMultiScreens(self, conf=None):
        """ Get multiscreeens for iptv """
        return self._access.post("NMC.OrangeTV", "getIPTVMultiScreens", conf)

    def get_orangetv_IPTVConfig(self, conf=None):
        """ Get iptv information """
        return self._access.post("NMC.OrangeTV", "getIPTVConfig", conf)

    def get_networkconfig(self, conf=None):
        """ Get saveset configuration """
        return self._access.post("NMC.NetworkConfig:get", conf)

    def set_networkconfig_NetworkBR(self, conf={"parameters": {"state": "true"}}):
        """ Save configuration """
        return self._access.post("NMC.NetworkConfig", "enableNetworkBR", conf)

    def get_IPv6(self, conf=None):
        """ Get IPv6 information """
        return self._access.post("NMC.IPv6", "get", conf)

    def get_autodetect(self):
        """ Autodetect """
        return self._access.post("NMC.Autodetect", "get")

    def get_remoteaccess_TimeLeft(self, conf=None):
        """ Get timeleft for remote access """
        return self._access.post("RemoteAccess", "getTimeLeft", conf)

    def get_usbhosts_Devices(self, conf=None):
        """ Get usb devices """
        return self._access.post("USBHosts", "getDevices", conf)

    def get_time_LocalTimeZoneName(self, conf=None):
        """ Get local  zone information """
        return self._access.post("Time", "getLocalTimeZoneName", conf)

    def set_time_LocalTimeZoneName(self, conf):
        """ Set local zone information """
        return self._access.post("Time", "setLocalTimeZoneName", conf)

    def get_time_Time(self, conf=None):
        """ Get time information """
        return self._access.post("Time", "getTime", conf)
