class System:

    def __init__(self, access):
        self._access = access

    async def get_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DeviceInfo:get')

    async def get_devices(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('Devices:get')

    
    async def get_led_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('LED?_restDepth=-1')
        
    
    async def get_users_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('UserManagement:getUsers')

    async def reboot(self):
        '''
        Reboot livebox
        '''
        await self._access.post('NMC:reboot')
    
    async def reset(self):
        '''
        Reset livebox
        '''
        await self._access.post('NMC:reset')

    async def get_guest_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/Guest:get')

    async def get_iptv_status(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/OrangeTV:getIPTVStatus')
        
    async def get_iptv_MultiScreens(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/OrangeTV:getIPTVMultiScreens')

        
    async def get_iptv_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/OrangeTV:getIPTVConfig')
        

    async def get_nmc_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:get')
        
    async def get_networkconfig_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/NetworkConfig:get')
        
    async def set_networkconfig_restore(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/NetworkConfig:enableNetworkBR',{"parameters":{"state":"true"}})
        
    async def set_check_ForUpgrades(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:checkForUpgrades')

    async def get_LanIP(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:getLANIP')
    
    async def get_ipv6_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/IPv6:get')
        
    async def get_remote_TimeLeft(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('RemoteAccess:getTimeLeft')

    async def get_remote_TimeLeft(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('RemoteAccess?_restDepth=1')

    async def set_remote_enable(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:enableRemoteAccess')

    async def set_remote_disable(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:disableRemoteAccess')

    async def get_usb_devices(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('USBHosts:getDevices')

    async def get_time_LocalTimeZoneName(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Time:getLocalTimeZoneName') 

    async def set_time_LocalTimeZoneName(self,conf):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Time:setLocalTimeZoneName',conf)

    async def get_time(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Time:getTime')

    async def set_WanMode(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"WanMode":"WanMode","Username":"pnp/orange2","Password":"orange"}}
        '''
        return await self._access.post('NMC:setWanMode',conf)
        
    async def get_nmc_autodetect(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('NMC/Autodetect:get')

    async def get_username(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('NMC:Username')
