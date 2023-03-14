"""Devices."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class DeviceInfo:
    """Device information."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._access.post("DeviceInfo", "get", conf)

    async def get_deviceinfo_pairing(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information.

        conf = {"getPairingInfo":""}
        """
        return await self._access.post("DeviceInfo", "getPairingInfo", conf)

    async def update_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._access.post("DeviceInfo", "update", conf)

    async def export_deviceinfo(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._access.post("DeviceInfo", "export", conf)

    async def get_deviceinfo_info(
        self, conf: dict[str, Any] = {"info": ""}
    ) -> dict[str, Any] | None:
        """Get device information."""
        info = conf.pop("info")
        return await self._access.post(f"DeviceInfo.{info}", "get", conf)


class Devices:  # pylint: disable=[too-many-public-methods]
    """Devices information."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def del_devices_device(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove devices.

        conf = {"key": 123}
        """
        return await self._access.post("Devices", "destroyDevice", conf)

    async def find_devices(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Find devices.

        conf = {"key": 123}
        """
        return await self._access.post("Devices", "find", conf)

    async def get_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get devices.

        conf = {"key": 123}
        """
        return await self._access.post("Devices", "get", conf)

    async def fetch_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Fetch devices."""
        return await self._access.post("Devices", "fetchDevice", conf)

    async def get_devices_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get config for device.

        conf = {"module":""}
        """
        return await self._access.post("Devices.Config", "get", conf)

    async def set_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set config for device."""
        return await self._access.post("Devices.Config", "set", conf)

    async def export_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Save config for device."""
        return await self._access.post("Devices.Config", "save", conf)

    async def import_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Load config for device."""
        return await self._access.post("Devices.Config", "load", conf)

    async def get_devices_config1(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get config for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Config.{key}", "get", conf)

    async def get_device(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "get", conf)

    async def set_device(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "set", conf)

    async def get_device_hastag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Has tag for device.

        conf = {"tag": "1"}
        """
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "hasTag", conf)

    async def set_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Tag for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "setTag", conf)

    async def del_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove tag for devices."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "clearTag", conf)

    async def get_device_first(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameter for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return await self._access.post(
            f"Devices.Device.{key}", "getFirstParameter", conf
        )

    async def get_device_params(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameters for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "getParameters", conf)

    async def get_device_topology(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get topology for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "topology", conf)

    async def get_device_islinked(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Linked."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "isLinkedTo", conf)

    async def set_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device name."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "setName", conf)

    async def add_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add device name."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "addName", conf)

    async def remove_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove device name."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "removeName", conf)

    async def del_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del name of device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "delName", conf)

    async def set_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device type."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "setType", conf)

    async def del_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del device type."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "removeType", conf)

    async def set_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Alternative for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "setAlternative", conf)

    async def del_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del Alternative for device."""
        key = conf.pop("key")
        return await self._access.post(
            f"Devices.Device.{key}", "removeAlternative", conf
        )

    async def get_device_isalternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Alternative for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "isAlternative", conf)

    async def set_device_service(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add service for device."""
        key = conf.pop("key")
        return await self._access.post(f"Devices.Device.{key}", "addService", conf)
