"""Devices."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class DeviceInfo:
    """Device information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "get", conf)

    async def async_get_deviceinfo_pairing(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information.

        conf = {"getPairingInfo":""}
        """
        return await self._auth.post("DeviceInfo", "getPairingInfo", conf)

    async def async_update_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "update", conf)

    async def async_export_deviceinfo(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "export", conf)

    async def async_get_deviceinfo_info(
        self, conf: dict[str, Any] = {"info": ""}
    ) -> dict[str, Any] | None:
        """Get device information."""
        info = conf.pop("info")
        return await self._auth.post(f"DeviceInfo.{info}", "get", conf)


class Devices:  # pylint: disable=[too-many-public-methods]
    """Devices information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_del_devices_device(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove devices.

        conf = {"key": 123}
        """
        return await self._auth.post("Devices", "destroyDevice", conf)

    async def async_find_devices(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Find devices.

        conf = {"key": 123}
        """
        return await self._auth.post("Devices", "find", conf)

    async def async_get_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get devices.

        conf = {"key": 123}
        """
        return await self._auth.post("Devices", "get", conf)

    async def async_fetch_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Fetch devices."""
        return await self._auth.post("Devices", "fetchDevice", conf)

    async def async_get_devices_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get config for device.

        conf = {"module":""}
        """
        return await self._auth.post("Devices.Config", "get", conf)

    async def async_set_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set config for device."""
        return await self._auth.post("Devices.Config", "set", conf)

    async def async_export_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Save config for device."""
        return await self._auth.post("Devices.Config", "save", conf)

    async def async_import_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Load config for device."""
        return await self._auth.post("Devices.Config", "load", conf)

    async def async_get_devices_config1(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get config for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Config.{key}", "get", conf)

    async def async_get_device(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "get", conf)

    async def async_set_device(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "set", conf)

    async def async_get_device_hastag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Has tag for device.

        conf = {"tag": "1"}
        """
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "hasTag", conf)

    async def async_set_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Tag for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "setTag", conf)

    async def async_del_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove tag for devices."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "clearTag", conf)

    async def async_get_device_first(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameter for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "getFirstParameter", conf)

    async def async_get_device_params(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameters for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "getParameters", conf)

    async def async_get_device_topology(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get topology for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "topology", conf)

    async def async_get_device_islinked(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Linked."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "isLinkedTo", conf)

    async def async_set_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device name."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "setName", conf)

    async def async_add_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add device name."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "addName", conf)

    async def async_remove_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove device name."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "removeName", conf)

    async def async_del_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del name of device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "delName", conf)

    async def async_set_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device type."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "setType", conf)

    async def async_del_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del device type."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "removeType", conf)

    async def async_set_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Alternative for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "setAlternative", conf)

    async def async_del_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del Alternative for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "removeAlternative", conf)

    async def async_get_device_isalternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Alternative for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "isAlternative", conf)

    async def async_set_device_service(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add service for device."""
        key = conf.pop("key")
        return await self._auth.post(f"Devices.Device.{key}", "addService", conf)
