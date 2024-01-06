"""Storage & co."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class HTTPService:
    """HTTPService class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_webdav_authmodes(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get authentication modes."""
        return await self._auth.post("HTTPService", "getAuthenticationModes", conf)

    async def async_add_webdav_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Add user for WebDav."""
        return await self._auth.post(
            "HTTPService.WebDav.DigestManager", "addUser", conf
        )

    async def async_set_webdav_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Change user for WebDav."""
        return await self._auth.post(
            "HTTPService.WebDav.DigestManager", "changeUser", conf
        )

    async def async_set_webdav_password(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Change password for WebDav user."""
        return await self._auth.post(
            "HTTPService.WebDav.DigestManager", "changePassword", conf
        )

    async def async_import_webdav(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Upload to WebDav."""
        return await self._auth.post("HTTPService.WebDav.DigestManager", "Upload", conf)


class StorageService:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth


class USBHosts:
    """USBHosts class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_usb_device(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get USB device."""
        return await self._auth.post("USBHosts", "get", conf)

    async def async_get_usb_devices(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get All USB devices."""
        return await self._auth.post("USBHosts", "getDevices", conf)

    async def async_get_usb_plug(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get USB plugged."""
        return await self._auth.post("USBHosts", "devicePlug", conf)

    async def async_get_usb_unplug(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get USB unplugged."""
        return await self._auth.post("USBHosts", "deviceUnplugged", conf)
