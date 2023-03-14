"""Network settings."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Wifi:
    """Wifi setting."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_wifi(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get wifi configuration."""
        return await self._access.post("NMC.Wifi", "get", conf)

    async def set_wifi(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set wifi configuration."""
        return await self._access.post("NMC.Wifi", "set", conf)

    async def get_wifi_Stats(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Wifi Statistics."""
        return await self._access.post("NMC.Wifi", "getStats", conf)

    async def start_wifi_pairing(self) -> dict[str, Any] | None:
        """Wifi start pairing."""
        return await self._access.post("NMC.Wifi", "startPairing")

    async def stop_wifi_pairing(self) -> dict[str, Any] | None:
        """Wifi stop pairing."""
        return await self._access.post("NMC.Wifi", "stopPairing")

    async def start_wifi_autochannel(self) -> dict[str, Any] | None:
        """Wifi select auto channel."""
        return await self._access.post("NMC.Wifi", "startAutoChannelSelection")

    async def get_openmode_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Wifi sharing information."""
        return await self._access.post("Wificom.OpenMode", "getStatus", conf)

    async def get_securemode_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get secure for wifi."""
        return await self._access.post("Wificom.SecureMode", "getStatus", conf)


class Lan:
    """Home Lan."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_lan(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Results for Lan."""
        return await self._access.post("HomeLan", "getResults", conf)

    async def get_lan_interfaces(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Interfaces."""
        return await self._access.post("HomeLan", "getInterfacesName", conf)

    async def get_lan_maxnumber(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Max number of records."""
        return await self._access.post("HomeLan", "getMaxNumberOfRecords", conf)

    async def get_lan_interval(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get reading interval."""
        return await self._access.post("HomeLan", "getReadingInterval", conf)

    async def get_lan_status(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Status."""
        return await self._access.post("HomeLan", "getStatus", conf)

    async def get_devices_results(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Status."""
        return await self._access.post("HomeLan", "getDeviceResults", conf)

    async def import_lan(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Import."""
        return await self._access.post("HomeLan", "import", conf)

    async def export_lan(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Export."""
        return await self._access.post("HomeLan", "export", conf)

    async def get_lan_ip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reboot livebox."""
        return await self._access.post("NMC", "getLANIP", conf)

    async def set_lan_ip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reboot livebox."""
        return await self._access.post("NMC", "setLANIP", conf)

    async def get_IPv6(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get IPv6 information."""
        return await self._access.post("NMC.IPv6", "get", conf)

    async def set_IPv6(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set IPv6 information."""
        return await self._access.post("NMC.IPv6", "set", conf)


class GuestWifi:
    """GuestWifi setting."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def get_guest_wifi(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get wifi configuration."""
        return await self._access.post("NMC.Guest", "get", conf)

    async def set_guest_wifi(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set wifi configuration."""
        return await self._access.post("NMC.Guest", "set", conf)
