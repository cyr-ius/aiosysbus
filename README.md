# aiosysbus

Manage your Livebox in Python

Easily manage your Livebox in Python.
Check your config, configure your dhcp, disable your wifi, monitor your LAN activity and many others, on LAN or remotely.

aiosysbus is a python library implementing fir the Livebox v3.

This project is based on stilllman/aiofreepybox, which provides the same features as aiofreepybox in a synchronous manner.

## WARNING

**Version 1.0.0 and above** makes all these calls asynchronously.
It breaks the compatibility of previous codes

## Install

Use the PIP package manager

```bash
$ pip install aiosysbus
```

Or manually download and install the last version from github

```bash
$ git clone https://github.com/cyr-ius/aiosysbus.git
$ python setup.py install
```

## Get started

aiosysbus < 1.0.0

```python
# Import the aiosysbus package.
from aiosysbus import AIOSysbus

async def reboot()
    # Instantiate the Sysbus class using default options.
    lvbx = AIOSysbus('192.168.1.1','80','xxxxxx')

    # Connect to the livebox with default options.
    lvbx.connect()

    # Do something useful, rebooting your livebox for example.
    lvbx.system.reboot()

    # Properly close the session.
    lvbx.close()
```

aiosysbus >= 1.0.0

```python
import asyncio
import logging

async def async_main() -> None:
    # Instantiate the Sysbus class using default options.
    api = AIOSysbus(username=xxxx, password=xxxx, host=HOST)
    # Connect to the livebox.
    await api.async_connect()
    # Query example
    parameters = {"parameters": {"expression": {"wifi": "wifi && .Active==False"}}}
    devices = await api.devices.async_get_devices(parameters)

    await api.async_close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
```

Have a look at the [example.py](https://github.com/cyr-ius/aiosysbus/blob/master/example.py) for a more complete overview.

## Notes on HTTPS

Not implemented
