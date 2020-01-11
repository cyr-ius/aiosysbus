class Nat:

    def __init__(self, access):
        self._access = access

    async def get_firewall_PortForwarding(self,conf=None):
        '''
        Get port forwarding configuration
        conf = {"parameters":{"origin":"webui"}}
        '''
        return await self._access.post('Firewall','getPortForwarding',conf)

    async def set_firewall_PortForwarding(self,conf):
        '''
        Set port forwarding configuration
       conf = {"parameters":{"description":"FTP","persistent":true,"enable":true,"protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21","externalPort":"21","origin":"webui","sourceInterface":"data","sourcePrefix":"","id":"FTP"}}
        '''
        return await self._access.post('Firewall','setPortForwarding',conf)

    async def get_firewall_DMZ(self,conf=None):
        ''' Get DMZ configuration '''
        return await self._access.post('Firewall','getDMZ',conf)

    async def set_firewall_DMZ(self,conf):
        ''' Set DMZ configuration '''
        return await self._access.post('Firewall','setDMZ',conf)

    async def set_firewall_IPv6Level(self,conf):
        '''
        Set level for IPv6 Firewall
        conf = {"parameters":{"level":"Low"}}
        '''
        return await self._access.post('Firewall','setFirewallIPv6Level',conf)

    async def set_firewall_Level(self,conf):
        '''
        Set level for IPv4 Firewall
        conf = {"parameters":{"level":"Low"}}
        '''
        return await self._access.post('Firewall','setFirewallLevel',conf)

    async def set_firewall_Commit(self):
        ''' Commit rules '''
        return await self._access.post('Firewall','commit')

    async def get_upnp_Pinhole(self,conf=None):
        '''
        Upnp configuration
        conf = {"parameters":{"origin":"upnp"}}
        '''
        return await self._access.post('Firewall','getPinhole',conf)

    async def get_dyndns_Hosts(self,conf=None):
        ''' Get Dynamic DNS Hosts configuration '''
        return await self._access.post('DynDNS','getHosts',conf)

    async def get_dyndns_Services(self,conf=None):
        ''' Get Dynamic DNS services configuration '''
        return await self._access.post('DynDNS','getServices',conf)

    async def set_dns_name(self,mac,conf):
        '''
        Set DNS name
        mac = '00:01:2B:3C:4D:5E'
        conf = {"parameters":{"name":"nestor","source":"dns"}}
        '''
        return await self._access.post('Devices/Device/'+mac+':setName',conf)

    async def get_upnp_devices(self,conf=None):
        ''' Get Upnp configuration '''
        return await self._access.post('UPnP-IGD','get',conf)

    async def set_upnp_config(self,conf):
        '''
        Set Upnp configuration
        conf = {"Enable":"1"}
        '''
        return await self._access.post('UPnP-IGD?_restAction=put',conf)
