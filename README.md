# aiosysbus
Manage your Livebox in Python


Easily manage your Livebox in Python.
Check your config, configure your dhcp, disable your wifi, monitor your LAN activity and many others, on LAN or remotely.

aiosysbus is a python library implementing fir the Livebox v3.

This project is based on stilllman/aiofreepybox, which provides the same features as aiofreepybox in a synchronous manner.

Install
-------
Use the PIP package manager
```bash
$ pip install aiosysbus
```

Or manually download and install the last version from github
```bash
$ git clone https://github.com/cyr-ius/aiosysbus.git
$ python setup.py install
```
Get started
-----------
```python
# Import the aiosysbus package.
from aiosysbus import Sysbus

async def reboot()
    # Instantiate the Sysbus class using default options.
    fbx = Sysbus()

    # Connect to the livebox with default options. 
    # Be ready to authorize the application on the Livebox.
    await lvbx.open('192.168.1.1')

    # Do something useful, rebooting your livebx for example.
    await lvbx.system.reboot()

    # Properly close the session.
	await lvbx.close()
```
Have a look at the [example.py](https://github.com/cyr-ius/aiosysbus/blob/aiosysbus/example.py) for a more complete overview.

Notes on HTTPS
--------------
Not implemented
