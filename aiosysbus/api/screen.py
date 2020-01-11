class Screen:

    def __init__(self, access):
        self._access = access

    async def get_ShowWifiPassword(self):
        ''' Show wifi password (display on box) '''
        return await self._access.post('Screen','getShowWifiPassword')
