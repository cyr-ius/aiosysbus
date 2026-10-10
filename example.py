#!/usr/bin/env python3
"""This example can be run safely as it won't change anything in your box configuration."""

import asyncio
import logging
from typing import Any

import yaml  # type: ignore

from aiosysbus import AIOSysbus
from aiosysbus.exceptions import (
    AiosysbusException,
    AuthenticationFailed,
    HttpRequestFailed,
    TimeoutExceededError,
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

# Fill out the secrets in secrets.yaml, you can find an example
# _secrets.yaml file, which has to be renamed after filling out the secrets.
with open("./secrets.yaml", encoding="UTF-8") as file:
    secrets: dict[str, Any] = yaml.safe_load(file)


# mypy: disable-error-code="attr-defined"
async def async_main() -> None:
    """Main function."""

    try:
        api = AIOSysbus(secrets["USERNAME"], secrets["PASSWORD"], host=secrets["HOST"])
        await api.async_connect()
        permissions = await api.async_get_permissions()
        logger.info(permissions)
        gdr = {"NumberOfReadings": 1, "InterfaceName": ["eth0"]}
        logger.debug(await api.lan.async_get_lan(gdr))
        logger.debug(await api.lan.async_get_devices_results(gdr))
        # parameters = {"parameters":{"expression":{"wifi":"wifi && (edev || hnid) and .IPAddress!=\"\" and .Active==true","eth":"eth && (edev || hnid) and .IPAddress!=\"\" and .Active==true"}}}
        # parameters = {"parameters":{"expression":{"wifi":"wifi && (edev || hnid) and .IPAddress!=\"\" and .Active==true and .Name=\"cam1\""}}}
        # parameters = {"parameters":{"expression":{"wifi":"wifi && (edev || hnid) and .IPAddress!=\"\" and .Active==true"}}}
        parameters = {"parameters": {"expression": {"wifi": "wifi && .Active==False"}}}
        # parameters = {"parameters":{"expression": {"eth": "eth && .Active==True"}}}
        devices = await api.devices.async_get_devices(parameters)
        for device in devices["status"]:
            logger.debug("============")
            logger.debug(device.get("InterfaceName"))
            logger.debug(device)
        # for device in devices["status"]:
        #     if not device.get("Active") and device.get("DeviceType") == "Computer":
        #         await api.system.async_del_devices_device({"key": device.get("PhysAddress")})
        devices = await api.devices.async_get_devices(parameters)
        for device in devices["status"]:
            logger.debug(device["Name"])
        # parameters = {
        #     "expression": {
        #         "eth": 'eth and .IPAddress!="" and .DeviceType!="" and .Active==true',
        #         "wifi": 'wifi and .IPAddress!="" and .Active==true',
        #     }
        # }
        # parameters = {"parameters": {"expression": ".Master==\"\""}}
        parameters = {"parameters": {"expression": {"eth": "eth"}}}
        # parameters = {"parameters": {"expression": {"wifi": "wifi"}}}
        hosts = await api.devices.async_get_devices(parameters)
        for device in hosts["status"]["eth"]:
            logger.info(
                "Key:{} - IP:{} - Name:{}".format(
                    device["Key"],
                    device.get("IPAddress", ""),
                    device.get("Name", "unknown"),
                )
            )

        # Exception:
        #   Traceback (most recent call last):
        #     File "/home/bn8/dev/aiosysbus/example.py", line 167, in <module>
        #       loop.run_until_complete(async_main())
        #     File "/usr/lib/python3.11/asyncio/base_events.py", line 653, in run_until_complete
        #       return future.result()
        #              ^^^^^^^^^^^^^^^
        #     File "/home/bn8/dev/aiosysbus/example.py", line 75, in async_main
        #       for device in hosts["status"]["wifi"]:
        #                     ~~~~~~~~~~~~~~~^^^^^^^^
        #   TypeError: list indices must be integers or slices, not str
        # for device in hosts["status"]["wifi"]:
        #     logger.info(
        #         "Key:{} - IP:{} - Name:{}".format(
        #             device["Key"],
        #             device.get("IPAddress", ""),
        #             device.get("Name", "unknown"),
        #         )
        #     )
        # => je n'arrive pas à voir sur quoi tu voulais iterer

        logger.info(await api.system.async_get_guest())
        info = await api.deviceinfo.async_get_deviceinfo()
        logger.info(info["status"]["SerialNumber"])
        await api.system.async_get_wanstatus()
        await api.connection.async_get_data_MIBS()

        # Error:
        #   2024-01-08 16:39:16,558 - aiosysbus.auth - DEBUG - METHOD:post URL:http://192.168.8.254:80/ws
        #   2024-01-08 16:39:16,558 - aiosysbus.auth - DEBUG - DATA:{'service': 'NeMo.Intf.dsl0', 'method': 'getMIBs', 'parameters': None}
        #   2024-01-08 16:39:16,713 - root - ERROR - [{'error': 196618, 'description': 'Object or parameter not found', 'info': 'NeMo.Intf.dsl0'}]
        # await api.connection.async_get_dsl0_MIBS()
        # => cette méthode ne semble pas exister.

        await api.system.async_get_guest()
        await api.system.async_get_nmc()
        await api.wifi.async_get_wifi()
        await api.call.async_get_voip()
        await api.call.async_get_voiceapplication_listHandsets()
        await api.call.async_get_voiceapplication_listTrunks()
        calllist = await api.call.async_get_voiceapplication_calllist()
        for call in calllist["status"]:
            logger.debug(
                "RemoteNumber {} - Terminale {} - Heure {} - Type {} - Durée {}".format(
                    call["remoteNumber"],
                    call["terminal"],
                    call["startTime"],
                    call["callType"],
                    call["duration"],
                )
            )
        await api.dhcp.async_get_dhcp_config()
        lip = (await api.connection.async_get_lan_luckyAddrAddress())["status"]
        wip = (await api.connection.async_get_data_luckyAddrAddress())["status"]
        logger.info("LAN IP Address: %s", str(lip))
        logger.info("WAN IP Address: %s", str(wip))
        # ~ parameters={"parameters":{"description":"FTP","persistent":"true","enable":"true","protocol":"6","destinationIPAddress":"192.168.1.250","internalPort":"21","externalPort":"21","origin":"webui","sourceInterface":"data","sourcePrefix":"","id":"FTP"}}
        # await api.nat.async_set_firewall_PortForwarding(parameters)
        await api.nat.async_get_firewall_PortForwarding()
        await api.userinterface.async_getLanguage()
        await api.userinterface.async_getState()
        await api.system.async_get_pnp()
        await api.event.async_get_events()
        await api.phonebook.async_get_contacts()

        # Error:
        #   2024-01-08 16:42:11,404 - aiosysbus.auth - DEBUG - METHOD:post URL:http://192.168.8.254:80/ws
        #   2024-01-08 16:42:11,404 - aiosysbus.auth - DEBUG - DATA:{'service': 'Scheduler', 'method': 'getSchedules', 'parameters': None}
        #   2024-01-08 16:42:11,438 - root - ERROR - [{'error': 196640, 'description': 'Missing mandatory argument', 'info': 'type'}]
        # await api.schedule.async_get_schedules()
        # => il faut passer un type de schedule en paramètre à minima
        scheduletypes = await api.schedule.async_get_scheduletypes()
        print(scheduletypes)
        await api.schedule.async_get_schedules(
            {"type": scheduletypes["data"]["types"][0]}
        )

        # Error:
        #   2024-01-08 16:59:13,058 - aiosysbus.auth - DEBUG - METHOD:post URL:http://192.168.8.254:80/ws
        #   2024-01-08 16:59:13,059 - aiosysbus.auth - DEBUG - DATA:{'service': 'USBHosts', 'method': 'get', 'parameters': None}
        #   2024-01-08 16:59:13,093 - root - ERROR - [{'error': 13, 'description': 'Permission denied', 'info': 'USBHosts'}]
        # await api.usbhosts.async_get_usb_device()
        # await api.usbhosts.async_get_usb_devices()

        # await api.system.async_enable_remoteaccess()

        # Error:
        # await api.system.async_get_devicemanager()
        # => méthode inexistante et introuvable ailleurs

        # await api.system.async_set_devicemanager_notification()
        await api.wifi.async_get_wifi()
        await api.wifi.async_get_openmode_status()
        await api.wifi.async_get_securemode_status()
        await api.system.async_get_time_status()

        # Error:
        #   2024-01-08 17:02:34,995 - aiosysbus.auth - DEBUG - METHOD:post URL:http://192.168.8.254:80/ws
        #   2024-01-08 17:02:34,995 - aiosysbus.auth - DEBUG - DATA:{'service': 'Devices.Config', 'method': 'get', 'parameters': None}
        #   2024-01-08 17:02:35,030 - root - ERROR - [{'error': 196640, 'description': 'Missing mandatory argument', 'info': 'module'}, {'error': 196640, 'description': 'Missing mandatory argument', 'info': 'option'}]
        # await api.devices.async_get_devices_config({"module": ?, "option": ?})

        # await api.system.async_get_device_topology({"key":"00:08:9B:CF:37:DE"})

        await api.devices.async_get_devices()

        # await api.system.async_get_device({"key": "10:61:FE:87:65:0F"})
        # await api.system.async_del_devices_device({"key": "10:61:FE:87:65:0F"})
        await api.dhcp.async_get_dhcp_staticleases()
        # await api.dhcp.async_set_dhcp_staticlease({"pool":"default", "MACAddress":"01:02:03:04:05:06","IPAddress":"192.168.1.55"})

        # await api.dhcp.async_del_dhcp_staticlease({"pool":"default", "MACAddress":"01:02:03:04:05:06"})
        # await api.dhcp.async_get_dhcp_stats()
        # await api.system.async_set_topodiags_build()
        # await api.system.async_get_deviceinfo_pairing()
        await api.lan.async_get_lan_interfaces()
        await api.lan.async_get_lan_ip()
        await api.lan.async_get_lan_status()
        await api.lan.async_get_IPv6()
        await api.connection.async_get_data_luckyAddrAddress()
        # Reboot
        # ~ await api.system.reboot()

    except HttpRequestFailed as e:
        logger.error(e)
    except AuthenticationFailed as e:
        logger.error(e)
    except TimeoutExceededError as e:
        logger.error(e)
    except AiosysbusException as e:
        logger.error(e)
    finally:
        await api.async_close()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(async_main())
