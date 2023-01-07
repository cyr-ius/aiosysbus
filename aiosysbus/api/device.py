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

    def get_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return self._access.post("DeviceInfo", "get", conf)

    def get_deviceinfo_pairing(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information.

        conf = {"getPairingInfo":""}
        """
        return self._access.post("DeviceInfo", "getPairingInfo", conf)

    def update_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get device information."""
        return self._access.post("DeviceInfo", "update", conf)

    def export_deviceinfo(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get device information."""
        return self._access.post("DeviceInfo", "export", conf)

    def get_deviceinfo_info(
        self, conf: dict[str, Any] = {"info": ""}
    ) -> dict[str, Any] | None:
        """Get device information."""
        info = conf.pop("info")
        return self._access.post(f"DeviceInfo.{info}", "get", conf)


class Devices:  # pylint: disable=[too-many-public-methods]
    """Devices information."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def del_devices_device(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "destroyDevice", conf)

    def find_devices(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Find devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "find", conf)

    def get_devices(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "get", conf)

    def fetch_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Fetch devices."""
        return self._access.post("Devices", "fetchDevice", conf)

    def get_devices_config(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get config for device.

        conf = {"module":""}
        """
        return self._access.post("Devices.Config", "get", conf)

    def set_devices_config(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set config for device."""
        return self._access.post("Devices.Config", "set", conf)

    def export_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Save config for device."""
        return self._access.post("Devices.Config", "save", conf)

    def import_devices_config(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Load config for device."""
        return self._access.post("Devices.Config", "load", conf)

    def get_devices_config1(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get config for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Config.{key}", "get", conf)

    def get_device(self, conf: dict[str, Any] = {"key": None}) -> dict[str, Any] | None:
        """Get device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "get", conf)

    def set_device(self, conf: dict[str, Any] = {"key": None}) -> dict[str, Any] | None:
        """Set device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "set", conf)

    def get_device_hastag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Has tag for device.

        conf = {"tag": "1"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "hasTag", conf)

    def set_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Tag for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setTag", conf)

    def del_device_tag(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove tag for devices."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "clearTag", conf)

    def get_device_first(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameter for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "getFirstParameter", conf)

    def get_device_params(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get parameters for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "getParameters", conf)

    def get_device_topology(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Get topology for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "topology", conf)

    def get_device_islinked(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Linked."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "isLinkedTo", conf)

    def set_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setName", conf)

    def add_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "addName", conf)

    def remove_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Remove device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeName", conf)

    def del_device_name(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del name of device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "delName", conf)

    def set_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set device type."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setType", conf)

    def del_device_type(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del device type."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeType", conf)

    def set_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Set Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setAlternative", conf)

    def del_device_alternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Del Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeAlternative", conf)

    def get_device_isalternative(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Is Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "isAlternative", conf)

    def set_device_service(
        self, conf: dict[str, Any] = {"key": None}
    ) -> dict[str, Any] | None:
        """Add service for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "addService", conf)
