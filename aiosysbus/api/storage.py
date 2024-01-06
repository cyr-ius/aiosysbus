"""Storage & co."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class HTTPService:
    """HTTPService class."""

    def __init__(self, access: Auth) -> None:
        """Init."""
        self._access = access

    async def async_get_webdav_authmodes(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get authentication modes."""
        return await self._access.post("HTTPService", "getAuthenticationModes", conf)

    async def async_add_webdav_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Add user for WebDav."""
        return await self._access.post(
            "HTTPService.WebDav.DigestManager", "addUser", conf
        )

    async def async_set_webdav_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Change user for WebDav."""
        return await self._access.post(
            "HTTPService.WebDav.DigestManager", "changeUser", conf
        )

    async def async_set_webdav_password(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Change password for WebDav user."""
        return await self._access.post(
            "HTTPService.WebDav.DigestManager", "changePassword", conf
        )

    async def async_import_webdav(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Upload to WebDav."""
        return await self._access.post(
            "HTTPService.WebDav.DigestManager", "Upload", conf
        )


class StorageService:  # pylint: disable=[too-few-public-methods]
    """Locations class."""

    def __init__(self, access: Auth) -> None:
        """Init."""
        self._access = access


class USBHosts:
    """USBHosts class."""

    def __init__(self, access: Auth) -> None:
        """Init."""
        self._access = access

    async def async_get_usb_device(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get USB device."""
        return await self._access.post("USBHosts", "get", conf)

    async def async_get_usb_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get All USB devices."""
        return await self._access.post("USBHosts", "getDevices", conf)

    async def async_get_usb_plug(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get USB plugged."""
        return await self._access.post("USBHosts", "devicePlug", conf)

    async def async_get_usb_unplug(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get USB unplugged."""
        return await self._access.post("USBHosts", "deviceUnplugged", conf)
