class Dhcp:

    def __init__(self, access):
        self._access = access

    async def get_config(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('DHCPv4/Server/Pool/default:get')

    async def set_dhcp_config(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"Address":"80:A5:89:0F:EA:6B","Netmask":"192.168.1.55","DHCPEnable":"","DHCPMinAddress":"","DHCPMaxAddress":""}}
        '''
        return await self._access.post('NMC:setLANIP',conf)

    async def get_dhcp_StaticLease(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('DHCPv4/Server/Pool/default:getStaticLeases')
              

    async def set_dhcp_StaticLease(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"MACAddress":"80:A5:89:0F:EA:6B","IPAddress":"192.168.1.55"}}
        '''
        return await self._access.post('DHCPv4/Server/Pool/default:addStaticLease',conf)
              

    async def del_dhcp_StaticLease(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"MACAddress":"80:a5:89:0f:ea:6b"}}
        '''
        return await self._access.post('DHCPv4/Server/Pool/default:deleteStaticLease',conf)
