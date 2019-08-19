class Wifi:

    def __init__(self, access):
        self._access = access

    async def get_global_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/Wifi:get')

    async def set_global_config(self,conf):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/Wifi:set',conf)

    async def get_stats(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC/Wifi:getStats')

    async def get_openmode_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('Wificom/OpenMode:getStatus')

    async def get_securemode_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('Wificom/SecureMode:getStatus')
