class Wifi:

    def __init__(self, access):
        self._access = access

    async def get_wifi(self,conf=None):
        ''' Get wifi configuration '''
        return await self._access.post('NMC.Wifi','get',conf)

    async def set_wifi(self,conf):
        ''' Set wifi configuration '''
        return await self._access.post('NMC.Wifi','set',conf)

    async def get_wifi_Stats(self,conf=None):
        ''' Wifi Statistics '''
        return await self._access.post('NMC.Wifi','getStats',conf)

    async def get_openmode_Status(self,conf=None):
        ''' Get Wifi sharing information '''
        return await self._access.post('Wificom.OpenMode','getStatus',conf)

    async def get_securemode_Status(self,conf=None):
        ''' Get secure for wifi '''
        return await self._access.post('Wificom.SecureMode','getStatus',conf)
