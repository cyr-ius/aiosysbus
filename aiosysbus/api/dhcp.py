class Dhcp:
    def __init__(self, access):
        self._access = access

    def set_dhcp_config(self, conf):
        """
        Set DHCP configuration
        conf = {"parameters":{"Address":"80:A5:89:0F:EA:6B","Netmask":"192.168.1.55","DHCPEnable":"","DHCPMinAddress":"","DHCPMaxAddress":""}}
        """
        return self._access.post("NMC", "setLANIP", conf)

    def get_dhcp_config(self, conf=None):
        """ Get DHCP configuration """
        return self._access.post("NMC", "getLANIP", conf)

    def get_dhcp_poolconfig(self, conf=None):
        """ Get Pool configuration """
        return self._access.post("DHCPv4/Server/Pool/default:get", conf)

    def get_dhcp_StaticLeases(self, conf=None):
        """ Get Leases """
        return self._access.post("DHCPv4/Server/Pool/default:getStaticLeases", conf)

    def set_dhcp_StaticLease(self, conf):
        """
        Set static lease
        conf = {"parameters":{"MACAddress":"80:A5:89:0F:EA:6B","IPAddress":"192.168.1.55"}}
        """
        return self._access.post("DHCPv4/Server/Pool/default:addStaticLease", conf)

    def del_dhcp_StaticLease(self, conf):
        """
        Remove static lease
        conf = {"parameters":{"MACAddress":"80:a5:89:0f:ea:6b"}}
        """
        return self._access.post("DHCPv4/Server/Pool/default:deleteStaticLease", conf)
