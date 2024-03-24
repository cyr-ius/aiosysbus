"""Storage & co."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class StorageService:
    """Storage service class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_logical_volume(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get logical volume.

        Argument:
        - uri (str)
        """
        return await self._auth.post("StorageService", "getLogicalVolume", conf)

    async def async_get_physical_mediums(self) -> list[Any]:
        """Get physical mediums."""
        return await self._auth.post("StorageService", "getPhysicalMediums")

    async def async_eject_logical_volume(self, conf: dict[str, Any]) -> bool:
        """Eject logical volume.

        Argument:
        - uri (str)
        """
        return await self._auth.post("StorageService", "ejectLogicalVolume", conf)

    async def async_get_disk_uri(self, conf: dict[str, Any] | None = None) -> bool:
        """Get disk uri.

        Argument:
        - uri (str) optional
        """
        return await self._auth.post("StorageService", "getDiskUri", conf)

    async def async_get_disk_info(self, conf: dict[str, Any] | None = None) -> bool:
        """Get disk info.

        Argument:
        - uri (str) optional
        - diskinfo (dict) optional
        """
        return await self._auth.post("StorageService", "getDiskInfo", conf)


class USBHosts:
    """USBHosts class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_usb_devices(
        self, conf: dict[str, Any] | None = None
    ) -> list[Any]:
        """Get All USB devices.

        Argument:
        - deviceClass (list) optional
        """
        return await self._auth.post("USBHosts", "getDevices", conf)

    async def async_enable_usb3(self, conf: dict[str, Any]) -> bool:
        """Get All USB devices.

        Argument:
        - enable (bool)
        """
        return await self._auth.post("USBHosts", "enableUSB3", conf)

    async def async_import(self) -> None:
        """Import usb host."""
        return await self._auth.post("USBHosts", "import")

    async def async_export(self) -> None:
        """Export usb host."""
        return await self._auth.post("USBHosts", "export")
