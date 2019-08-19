class Screen:

    def __init__(self, access):
        self._access = access

    def get_global_config(self):
        '''
        Get system configuration:
        '''
        return await self._access.post('Screen:getShowWifiPassword')  
