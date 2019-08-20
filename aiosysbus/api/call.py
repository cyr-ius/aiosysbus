class Call:

    def __init__(self, access):
        self._access = access

    async def get_voip(self):
        ''' Get VIOP configuration '''
        return await self._access.post('NMC:getVoIPConfig')

    async def get_voiceapplication_listHandsets(self):
        ''' Get Handsets '''
        return await self._access.post('VoiceService/VoiceApplication:listHandsets')

    async def get_voiceapplication_listTrunks(self):
        ''' Get Trunks '''
        return await self._access.post('VoiceService/VoiceApplication:listTrunks')

    async def set_dect_startPairing(self):
        ''' Appairing DECT '''
        return await self._access.post('DECT:startPairing')

    async def get_dect_Pin(self):
        ''' Get Pin code for DECT '''
        return await self._access.post('DECT:getPIN')

    async def set_dect_Pin(self,conf):
        ''' Set Pin code for DECT '''
        return await self._access.post('DECT:setPIN',conf)

    async def get_dect_Version(self):
        ''' Get DECT version '''
        return await self._access.post('DECT:getVersion')

    async def get_dect_StandardVersion(self):
        ''' Get standard version '''
        return await self._access.post('DECT:getStandardVersion')

    async def get_dect_RFPI(self):
        ''' Get RFPI '''
        return await self._access.post('DECT:getRFPI')
