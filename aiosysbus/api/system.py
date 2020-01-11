class System:

    def __init__(self, access):
        self._access = access

    async def get_deviceinfo(self,conf=None):
        ''' Get device information '''
        return await self._access.post('DeviceInfo','get',conf)

    async def get_devices(self,conf=None):
        ''' Get devices '''
        return await self._access.post('Devices','get',conf)

    async def get_led(self,conf=None):
        ''' Get LED information '''
        return await self._access.post('LED','get',conf)

    async def get_usbhosts(self,conf=None):
        ''' Get USB Hosts '''
        return await self._access.post('USBHosts','get',conf)

    async def checkForUpgrades(self):
        ''' Check upgrade version '''
        return await self._access.post('NMC','checkForUpgrades')

    async def disableRemoteAccess(self):
        ''' Set disable remote access '''
        return await self._access.post('NMC','disableRemoteAccess')

    async def enableRemoteAccess(self):
        ''' Set  enable remote acess '''
        return await self._access.post('NMC','enableRemoteAccess')

    async def get_nmc(self,conf=None):
        ''' Get WAN information '''
        return await self._access.post('NMC','get',conf)

    async def get_WANStatus(self,conf=None):
        ''' Get WAN status '''
        return await self._access.post('NMC','getWANStatus',conf)

    async def reboot(self):
        ''' Reboot livebox '''
        return await self._access.post('NMC','reboot')

    async def reset(self):
        ''' Reset livebox '''
        return await self._access.post('NMC','reset')

    async def set_WanMode(self,conf):
        '''
        Set WAN Mode
        {"parameters":{"WanMode":"WanMode","Username":"pnp/orange2","Password":"orange"}}
        '''
        return await self._access.post('NMC','setWanMode',conf)

    async def username(self):
        ''' Get username '''
        return await self._access.post('NMC','Username')

    async def get_remoteaccess(self,conf=None):
        ''' Get Remote access information '''
        return await self._access.post('RemoteAccess','get',conf)

    async def get_usermanagement(self,conf=None):
        ''' Get users information '''
        return await self._access.post('UserManagement','getUsers',conf)

    async def get_guest(self,conf=None):
        ''' Get guests '''
        return await self._access.post('NMC.Guest','get',conf)

    async def get_orangetv_IPTVStatus(self,conf=None):
        ''' Get iptv status '''
        return await self._access.post('NMC.OrangeTV','getIPTVStatus',conf)

    async def get_orangetv_IPTVMultiScreens(self,conf=None):
        ''' Get multiscreeens for iptv '''
        return await self._access.post('NMC.OrangeTV','getIPTVMultiScreens',conf)

    async def get_orangetv_IPTVConfig(self,conf=None):
        ''' Get iptv information '''
        return await self._access.post('NMC.OrangeTV','getIPTVConfig',conf)

    async def get_networkconfig(self,conf=None):
        ''' Get saveset configuration '''
        return await self._access.post('NMC.NetworkConfig:get',conf)

    async def set_networkconfig_NetworkBR(self,conf={"parameters":{"state":"true"}}):
        ''' Save configuration '''
        return await self._access.post('NMC.NetworkConfig','enableNetworkBR',conf)

    async def get_IPv6(self,conf=None):
        ''' Get IPv6 information '''
        return await self._access.post('NMC.IPv6','get',conf)

    async def get_autodetect(self):
        ''' Autodetect '''
        return await self._access.post('NMC.Autodetect','get')

    async def get_remoteaccess_TimeLeft(self,conf=None):
        ''' Get timeleft for remote access '''
        return await self._access.post('RemoteAccess','getTimeLeft',conf)

    async def get_usbhosts_Devices(self,conf=None):
        ''' Get usb devices '''
        return await self._access.post('USBHosts','getDevices',conf)

    async def get_time_LocalTimeZoneName(self,conf=None):
        ''' Get local  zone information '''
        return await self._access.post('Time','getLocalTimeZoneName',conf)

    async def set_time_LocalTimeZoneName(self,conf):
        ''' Set local zone information '''
        return await self._access.post('Time','setLocalTimeZoneName',conf)

    async def get_time_Time(self,conf=None):
        ''' Get time information '''
        return await self._access.post('Time','getTime',conf=None)
