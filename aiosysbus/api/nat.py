class Nat:

    def __init__(self, access):
        self._access = access
    
    async def get_firewall_PortForwardingWebUI(self,conf={"parameters":{"origin":"webui"}}):
        '''
        Get DHCP configuration
        {"parameters":{"MACAddress":"80:a5:89:0f:ea:6b"}}
        '''
        return await self._access.post('Firewall:getPortForwarding',conf)

    async def get_firewall_PortForwardingWebUPNP(self,conf={"parameters":{"origin":"upnp"}}):
        '''
        Get DHCP configuration
        {"parameters":{"MACAddress":"80:a5:89:0f:ea:6b"}}
        '''
        return await self._access.post('Firewall:getPortForwarding',conf)        

    async def set_firewall_PortForwarding(self,conf):
        '''
        Get DHCP configuration
       {"parameters":{"description":"FTP","persistent":true,"enable":true,"protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21","externalPort":"21","origin":"webui","sourceInterface":"data","sourcePrefix":"","id":"FTP"}}
        '''
        return await self._access.post('Firewall:setPortForwarding',conf)

    async def get_firewall_DMZ(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Firewall:getDMZ')

    async def set_firewall_DMZ(self,conf):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Firewall:setDMZ',conf)

    async def set_firewall_IPv6Level(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"level":"Low"}}
        '''
        return await self._access.post('Firewall:setFirewallIPv6Level',conf)

    async def set_firewall_Level(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"level":"Low"}}
        '''
        return await self._access.post('Firewall:setFirewallLevel',conf)

    async def set_firewall_Commit(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('Firewall:commit')

    async def set_dns_name(self,conf):
        '''
        Get DHCP configuration
        {"parameters":{"name":"nestor","source":"dns"}}
        '''
        return await self._access.post('Devices/Device/00:08:9B:CF:37:DE:setName',conf)

    async def get_upnp_devices(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('UPnP-IGD?_restDepth=0')

    async def set_upnp_config(self,conf):
        '''
        Get DHCP configuration
       {"Enable":"1"}
        '''
        return await self._access.post('UPnP-IGD?_restAction=put',conf)

    async def get_upnp_Pinhole(self):
        '''
        Get DHCP configuration
        {"parameters":{"origin":"upnp"}}
        '''
        return await self._access.post('Firewall:getPinhole',{"parameters":{"origin":"upnp"}})

    async def get_dyndns_Hosts(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('DynDNS:getHosts')

    async def get_dyndns_Services(self):
        '''
        Get DHCP configuration
        '''
        return await self._access.post('DynDNS:getServices')
