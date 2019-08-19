class Connection:

    def __init__(self, access):
        self._access = access

    async def get_lan_luckyAddrAddress(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/lan:luckyAddrAddress')

    async def get_data_luckyAddrAddress(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/data:luckyAddrAddress')

    async def get_WANStatus(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NMC:getWANStatus')

    async def get_lo_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/lo:getDHCPOption')

    async def get_dsl0_DSLStats(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/dsl0:getDSLStats')

    async def get_dsl0_MIBS(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/dsl0:getMIBs')

    async def get_data_MIBS(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/data:getMIBs')

    async def get_lan_MIBS(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('NeMo/Intf/lan:getMIBs')
