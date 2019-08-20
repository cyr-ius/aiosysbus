class Wifi:

    def __init__(self, access):
        self._access = access

    async def get_wifi(self):
        ''' Get wifi configuration '''
        return await self._access.post('NMC/Wifi:get')

    async def set_wifi(self,conf):
        ''' Set wifi configuration '''
        return await self._access.post('NMC/Wifi:set',conf)

    async def get_wifi_Stats(self):
        ''' Wifi Statistics '''
        return await self._access.post('NMC/Wifi:getStats')

    async def get_openmode_Status(self):
        ''' Get Wifi sharing information '''
        return await self._access.post('Wificom/OpenMode:getStatus')

    async def get_securemode_Status(self):
        ''' Get secure for wifi '''
        return await self._access.post('Wificom/SecureMode:getStatus')
