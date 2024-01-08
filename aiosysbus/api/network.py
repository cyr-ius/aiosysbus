"""Network settings."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Wifi:
    """Wifi setting."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_wifi(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get wifi configuration."""
        return await self._auth.post("NMC.Wifi", "get", conf)

    async def async_set_wifi(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set wifi configuration."""
        return await self._auth.post("NMC.Wifi", "set", conf)

    async def async_get_wifi_Stats(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Wifi Statistics."""
        return await self._auth.post("NMC.Wifi", "getStats", conf)

    async def async_start_wifi_pairing(self) -> dict[str, Any]:
        """Wifi start pairing."""
        return await self._auth.post("NMC.Wifi", "startPairing")

    async def async_stop_wifi_pairing(self) -> dict[str, Any]:
        """Wifi stop pairing."""
        return await self._auth.post("NMC.Wifi", "stopPairing")

    async def async_start_wifi_autochannel(self) -> dict[str, Any]:
        """Wifi select auto channel."""
        return await self._auth.post("NMC.Wifi", "startAutoChannelSelection")

    async def async_get_openmode_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Wifi sharing information."""
        return await self._auth.post("Wificom.OpenMode", "getStatus", conf)

    async def async_get_securemode_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get secure for wifi."""
        return await self._auth.post("Wificom.SecureMode", "getStatus", conf)


class Lan:
    """Home Lan."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_lan(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Results for Lan."""
        return await self._auth.post("HomeLan", "getResults", conf)

    async def async_get_lan_interfaces(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Interfaces."""
        return await self._auth.post("HomeLan", "getInterfacesNames", conf)

    async def async_get_lan_maxnumber(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Max number of records."""
        return await self._auth.post("HomeLan", "getMaxNumberOfRecords", conf)

    async def async_get_lan_interval(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get reading interval."""
        return await self._auth.post("HomeLan", "getReadingInterval", conf)

    async def async_get_lan_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Status."""
        return await self._auth.post("HomeLan", "getStatus", conf)

    async def async_get_devices_results(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Status."""
        return await self._auth.post("HomeLan", "getDeviceResults", conf)

    async def async_import_lan(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Import."""
        return await self._auth.post("HomeLan", "import", conf)

    async def async_export_lan(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Export."""
        return await self._auth.post("HomeLan", "export", conf)

    async def async_get_lan_ip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Reboot livebox."""
        return await self._auth.post("NMC", "getLANIP", conf)

    async def async_set_lan_ip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Reboot livebox."""
        return await self._auth.post("NMC", "setLANIP", conf)

    async def async_get_IPv6(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get IPv6 information."""
        return await self._auth.post("NMC.IPv6", "get", conf)

    async def async_set_IPv6(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set IPv6 information."""
        return await self._auth.post("NMC.IPv6", "set", conf)


class GuestWifi:
    """GuestWifi setting."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_guest_wifi(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get wifi configuration."""
        return await self._auth.post("NMC.Guest", "get", conf)

    async def async_set_guest_wifi(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set wifi configuration."""
        return await self._auth.post("NMC.Guest", "set", conf)
