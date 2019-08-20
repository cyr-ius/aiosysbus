#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''

import asyncio
from aiosysbus import Sysbus


async def demo():
    # Instantiate Livebox class 
    lvbx = Sysbus()

    # Connect to the livebox
    # Be ready to authorize the application on the Livebox if you use this
    # example for the first time
    await lvbx.open(host='192.168.1.1', port=80, password='xxxxxx')

    print(await lvbx.system.get_deviceinfo())
    print(await lvbx.connection.get_data_MIBS())
    print(await lvbx.connection.get_dsl0_MIBS())
    print(await lvbx.system.get_guest_config())
    
    print('LAN IP Address: '+(await lvbx.connection.get_lan_luckyAddrAddress())['status'])
    print('WAN IP Address: '+(await lvbx.connection.get_data_luckyAddrAddress())['status'])
    
    #~ parameters={"parameters":{"description":"FTP","persistent":"true","enable":"true","protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21","externalPort":"21","origin":"webui","sourceInterface":"data","sourcePrefix":"","id":"FTP"}}
    #~ await lvbx.nat.set_firewall_PortForwarding(parameters)
    #~ await lvbx.nat.get_firewall_PortForwarding()

    # Reboot
    #~ await lvbx.system.reboot()
    
    # Close the livebox session
    await lvbx.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(demo())
loop.close()
