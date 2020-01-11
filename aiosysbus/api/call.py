class Call:

    def __init__(self, access):
        self._access = access

    async def get_voip(self,conf=None):
        ''' Get VIOP configuration '''
        return await self._access.post('NMC','getVoIPConfig',conf)

    async def get_voiceapplication_listHandsets(self,conf=None):
        ''' Get Handsets '''
        return await self._access.post('VoiceService.VoiceApplication','listHandsets',conf)

    async def get_voiceapplication_listTrunks(self,conf=None):
        ''' Get Trunks '''
        return await self._access.post('VoiceService.VoiceApplication','listTrunks',conf)

    async def set_dect_startPairing(self):
        ''' Appairing DECT '''
        return await self._access.post('DECT','startPairing')

    async def get_dect_Pin(self,conf=None):
        ''' Get Pin code for DECT '''
        return await self._access.post('DECT','getPIN',conf)

    async def set_dect_Pin(self,conf):
        ''' Set Pin code for DECT '''
        return await self._access.post('DECT','setPIN',conf)

    async def get_dect_Version(self,conf=None):
        ''' Get DECT version '''
        return await self._access.post('DECT','getVersion',conf)

    async def get_dect_StandardVersion(self,conf=None):
        ''' Get standard version '''
        return await self._access.post('DECT','getStandardVersion',conf)

    async def get_dect_RFPI(self,conf=None):
        ''' Get RFPI '''
        return await self._access.post('DECT','getRFPI',conf)
