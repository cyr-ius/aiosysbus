"""Devices."""

class DeviceInfo:
    """Device information."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_deviceinfo(self, conf=None):
        """Get device information."""
        return self._access.post("DeviceInfo", "get", conf)

    def get_deviceinfo_pairing(self, conf=None):
        """Get device information.

        conf = {"getPairingInfo":""}
        """
        return self._access.post("DeviceInfo", "getPairingInfo", conf)

    def update_deviceinfo(self, conf=None):
        """Get device information."""
        return self._access.post("DeviceInfo", "update", conf)

    def export_deviceinfo(self, conf):
        """Get device information."""
        return self._access.post("DeviceInfo", "export", conf)

    def get_deviceinfo_info(self, conf={"info": ""}):
        """Get device information."""
        info = conf.pop("info")
        return self._access.post(f"DeviceInfo.{info}", "get", conf)

class Devices:
    """Devices information."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def del_devices_device(self, conf):
        """Remove devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "destroyDevice", conf)

    def find_devices(self, conf):
        """Find devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "find", conf)

    def get_devices(self, conf=None):
        """Get devices.

        conf = {"key": 123}
        """
        return self._access.post("Devices", "get", conf)

    def fetch_devices(self, conf=None):
        """Fetch devices."""
        return self._access.post("Devices", "fetchDevice", conf)

    def get_devices_config(self, conf=None):
        """Get config for device.

        conf = {"module":""}
        """
        return self._access.post("Devices.Config", "get", conf)

    def set_devices_config(self, conf):
        """Set config for device."""
        return self._access.post("Devices.Config", "set", conf)

    def export_devices_config(self, conf):
        """Save config for device."""
        return self._access.post("Devices.Config", "save", conf)

    def import_devices_config(self, conf):
        """Load config for device."""
        return self._access.post("Devices.Config", "load", conf)

    def get_devices_config1(self, conf={"key": None}):
        """Get config for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Config.{key}", "get", conf)

    def get_device(self, conf={"key": None}):
        """Get device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "get", conf)

    def set_device(self, conf={"key": None}):
        """Set device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "set", conf)

    def get_device_hastag(self, conf={"key": None}):
        """Has tag for device.

        conf = {"tag": "1"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "hasTag", conf)

    def set_device_tag(self, conf={"key": None}):
        """Set Tag for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setTag", conf)

    def del_device_tag(self, conf={"key": None}):
        """Remove tag for devices."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "clearTag", conf)

    def get_device_first(self, conf={"key": None}):
        """Get parameter for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "getFirstParameter", conf)

    def get_device_params(self, conf={"key": None}):
        """Get parameters for device.

        conf = {"key:"01:02:03:04:05:06","parameter": "Name"}
        """
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "getParameters", conf)

    def get_device_topology(self, conf={"key": None}):
        """Get topology for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "topology", conf)

    def get_device_islinked(self, conf={"key": None}):
        """Is Linked."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "isLinkedTo", conf)

    def set_device_name(self, conf={"key": None}):
        """Set device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setName", conf)

    def add_device_name(self, conf={"key": None}):
        """Add device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "addName", conf)

    def remove_device_name(self, conf={"key": None}):
        """Remove device name."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeName", conf)

    def del_device_name(self, conf={"key": None}):
        """Del name of device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "delName", conf)

    def set_device_type(self, conf={"key": None}):
        """Set device type."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setType", conf)

    def del_device_type(self, conf={"key": None}):
        """Del device type."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeType", conf)

    def set_device_alternative(self, conf={"key": None}):
        """Set Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "setAlternative", conf)

    def del_device_alternative(self, conf={"key": None}):
        """Del Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "removeAlternative", conf)

    def get_device_isalternative(self, conf={"key": None}):
        """Is Alternative for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "isAlternative", conf)

    def set_device_service(self, conf={"key": None}):
        """Add service for device."""
        key = conf.pop("key")
        return self._access.post(f"Devices.Device.{key}", "addService", conf)
