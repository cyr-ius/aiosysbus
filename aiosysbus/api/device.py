"""Devices."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class DeviceInfo:
    """Device information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_deviceinfo(self) -> dict[str, Any]:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "get")

    async def async_get_deviceinfo_pairing(self) -> dict[str, Any]:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "getPairingInfo")

    async def async_update_deviceinfo(self) -> bool:
        """Get device information."""
        return await self._auth.post("DeviceInfo", "update")

    async def async_get_debuginfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get debug information.

        Argument:
        - filedesc (str) optional
        - options (debug_options_t) optional
        """
        return await self._auth.post("DeviceInfo", "getDebugInformation", conf)

    async def async_export_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get device information.

        Argument:
        - fileName (str) optional
        """
        return await self._auth.post("DeviceInfo", "export", conf)

    # DeviceInfo.VendorConfigFile
    async def async_restore_vendorconfigfile(
        self, conf: dict[str, Any]
    ) -> dict[str, Any]:
        """Restore vendor config file.

        Argument:
        - URL (str)
        - Username (str) optional
        - Password (str) optional
        - FileSize (int) optional
        - TargetFileName (str) optional
        - CheckSumAlgorithm (str) optional
        - CheckSum (str) optional
        """
        return await self._auth.post("DeviceInfo.VendorConfigFile", "Restore", conf)

    async def async_restore_extended_vendorconfigfile(
        self, conf: dict[str, Any]
    ) -> dict[str, Any]:
        """Restore vendor config file.

        Argument:
        - URL (str)
        - Username (str) optional
        - Password (str) optional
        - CACert (str) optional
        - ClientCert (str) optional
        - PrivateKey (str) optional
        - FileSize (int) optional
        - TargetFileName (str) optional
        - CheckSumAlgorithm (str) optional
        - CheckSum (str) optional
        """
        return await self._auth.post(
            "DeviceInfo.VendorConfigFile", "RestoreExtended", conf
        )


class DeviceManager:
    """DeviceManager information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_deviceinfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get device information.

        Arguments:
        - sources (str) optional
        - types (str) optional
        """
        return await self._auth.post("DeviceManager", "getDevices", conf)

    async def async_enable_notif(self) -> bool:
        """Enable notification."""
        return await self._auth.post(
            "DeviceManager.Connectivity", "enableNotifications"
        )

    # DeviceManager.Connectivity
    async def async_get_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get status.

        Arguments:
        - sources (str) optional
        """
        return await self._auth.post("DeviceManager", "getStatus", conf)

    async def async_enable_connectnotif(self) -> bool:
        """Enable notification."""
        return await self._auth.post(
            "DeviceManager.Connectivity", "enableNotifications"
        )


class Devices:
    """Devices information."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_del_devices_device(self, conf: dict[str, Any]) -> bool:
        """Remove devices.

        Argument:
        - key (str)
        """
        return await self._auth.post("Devices", "destroyDevice", conf)

    async def async_find_devices(self, conf: dict[str, Any] | None = None) -> list[Any]:
        """Find devices.

        Argument:
        - expression (dict) optional
        - flags (str) optional
        """
        return await self._auth.post("Devices", "find", conf)

    async def async_get_devices(self, conf: dict[str, Any] | None = None) -> list[Any]:
        """Get devices.

        Argument:
        - expression (dict) optional
        - flags (str) optional
        """
        return await self._auth.post("Devices", "get", conf)

    async def async_find_devices_by_ipaddress(self, conf: dict[str, Any]) -> list[Any]:
        """Find devices by ip.

        Arguments:
        - ipaddress (str)
        - ipstatus (str) optional
        - flags (str) optional
        """
        return await self._auth.post("Devices", "findByIPAddress", conf)

    async def async_fetch_devices(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Fetch devices.

        Arguments:
        - key (str)
        - flags (str) optional
        """
        return await self._auth.post("Devices", "fetchDevice", conf)

    # Devices.Config

    async def async_set_devices_config(self, conf: dict[str, Any]) -> None:
        """Set config for device.

        Arguments:
        - module (str)
        - option (str)
        - value (dict)
        """
        return await self._auth.post("Devices.Config", "set", conf)

    async def async_get_devices_config(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get config for device.

        Arguments:
        - module (str)
        - option (str)
        """
        return await self._auth.post("Devices.Config", "get", conf)

    async def async_export_devices_config(self, conf: dict[str, Any]) -> bool:
        """Save config for device.

        Arguments:
        - module (str)
        """
        return await self._auth.post("Devices.Config", "save", conf)

    async def async_import_devices_config(self, conf: dict[str, Any]) -> bool:
        """Load config for device.

        Arguments:
        - module (str)
        """
        return await self._auth.post("Devices.Config", "load", conf)

    # Devices.Device

    async def async_get_device(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get config for device.

        Arguments:
        - flags (str)
        """
        return await self._auth.post("Devices.Device", "get", conf)

    async def async_set_device(self, conf: dict[str, Any]) -> bool:
        """Set device.

        Arguments:
        - parameters (str)
        """
        return await self._auth.post("Devices.Device", "set", conf)

    async def async_remove_device(self, conf: dict[str, Any]) -> bool:
        """Remove device.

        Arguments:
        - path (str)
        """
        return await self._auth.post("Devices.Device", "remove", conf)

    async def async_get_device_hastag(self, conf: dict[str, Any]) -> bool:
        """ "Has tag for device.

        Arguments:
        - tag (str)
        - expression (str) optional
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "hasTag", conf)

    async def async_set_device_tag(self, conf: dict[str, Any]) -> None:
        """Set tag device.

        Arguments:
        - tag (str)
        - expression (str) optional
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "setTag", conf)

    async def async_delete_device_tag(self, conf: dict[str, Any]) -> None:
        """clear tag device.

        Arguments:
        - tag (str)
        - expression (str) optional
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "clearTag", conf)

    async def async_get_first_parameter(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get first parameter.

        Arguments:
        - parameter (str)
        - expression (str) optional
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "getFirstParameter", conf)

    async def async_get_parameters(self, conf: dict[str, Any]) -> list[Any]:
        """Get parameters.

        Arguments:
        - parameter (str)
        - expression (str) optional
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "getParameters", conf)

    async def async_topology(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get parameters.

        Arguments:
        - expression (str) optional
        - traverse (str) optional
        - flags (str) optional
        """
        return await self._auth.post("Devices.Device", "topology", conf)

    async def async_islinkedTo(self, conf: dict[str, Any]) -> bool:
        """Is linked.

        Arguments:
        - device (str)
        - traverse (str) optional
        """
        return await self._auth.post("Devices.Device", "isLinkedTo", conf)

    async def async_set_name(self, conf: dict[str, Any]) -> bool:
        """Set name.

        Arguments:
        - name (str)
        - source (str) optional
        """
        return await self._auth.post("Devices.Device", "setName", conf)

    async def async_add_name(self, conf: dict[str, Any]) -> bool:
        """Add name.

        Arguments:
        - name (str)
        - source (str) optional
        """
        return await self._auth.post("Devices.Device", "addName", conf)

    async def async_remove_name(self, conf: dict[str, Any]) -> bool:
        """Delete name.

        Arguments:
        - source (str)
        """
        return await self._auth.post("Devices.Device", "removeName", conf)

    async def async_delete_name(self, conf: dict[str, Any]) -> bool:
        """Delete name.

        Arguments:
        - name (str)
        - source (str) optional
        """
        return await self._auth.post("Devices.Device", "delName", conf)

    async def async_set_type(self, conf: dict[str, Any]) -> bool:
        """Set type.

        Arguments:
        - type (str)
        - source (str) optional
        """
        return await self._auth.post("Devices.Device", "setType", conf)

    async def async_remove_type(self, conf: dict[str, Any]) -> bool:
        """Remove type.

        Arguments:
        - source (str)
        """
        return await self._auth.post("Devices.Device", "removeType", conf)

    async def async_isImplemented(self, conf: dict[str, Any]) -> bool:
        """Is Implemented.

        Arguments:
        - function (str)
        - subObject (str) optional
        """
        return await self._auth.post("Devices.Device", "isImplemented", conf)

    async def async_set_alternative(self, conf: dict[str, Any]) -> bool:
        """Set alternative.

        Arguments:
        - alternative (str)
        """
        return await self._auth.post("Devices.Device", "setAlternative", conf)

    async def async_remove_alternative(self, conf: dict[str, Any]) -> bool:
        """Remove alternative.

        Arguments:
        - alternative (str)
        """
        return await self._auth.post("Devices.Device", "removeAlternative", conf)

    async def async_isAlternative(self, conf: dict[str, Any]) -> bool:
        """Is alternative.

        Arguments:
        - alternative (str)
        """
        return await self._auth.post("Devices.Device", "isAlternative", conf)

    async def async_set_alternative_rules(self, conf: dict[str, Any]) -> bool:
        """Set alternative rules.

        Arguments:
        - rules (list)
        """
        return await self._auth.post("Devices.Device", "setAlternativeRules", conf)

    async def async_remove_alternative_rules(self) -> bool:
        """Remove alternative rules."""
        return await self._auth.post("Devices.Device", "removeAlternativeRules")
