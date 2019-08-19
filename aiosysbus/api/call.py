class Call:

    def __init__(self, access):
        self._access = access

    async def get_global_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:getVoIPConfig')

    async def get_voiceservice_Handsets(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('VoiceService/VoiceApplication:listHandsets')

    async def get_voiceservice_Trunks(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('VoiceService/VoiceApplication:listTrunks')

    async def set_dect_startPairing(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:startPairing')

    async def get_dect_Pin(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:getPIN')

    async def set_dect_Pin(self,conf):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:setPIN',conf)

    async def get_dect_Version(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:getVersion')

    async def get_dect_StandardVersion(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:getStandardVersion')

    async def get_dect_RFPI(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('DECT:getRFPI')
