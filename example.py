#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This example can be run safely as it won't change anything in your box configuration
'''

import asyncio
import logging

from aiosysbus import Sysbus

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

async def demo():
    # Instantiate Livebox class 
    lvbx = Sysbus()

    # Connect to the livebox
    # Be ready to authorize the application on the Livebox if you use this
    # example for the first time
    await lvbx.open(host='192.168.1.1', port=80, password='xxxxxx')

    await lvbx.system.get_deviceinfo()
    await lvbx.connection.get_data_MIBS()
    await lvbx.connection.get_dsl0_MIBS()
    await lvbx.system.get_guest()

    lip=(await lvbx.connection.get_lan_luckyAddrAddress())['status']
    wip=(await lvbx.connection.get_data_luckyAddrAddress())['status']
    
    logger.info('LAN IP Address: %s',str(lip))
    logger.info('WAN IP Address: %s',str(wip))
    
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
