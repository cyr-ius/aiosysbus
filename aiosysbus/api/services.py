"""Services and co."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class Profiles:
    """Profiles class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_profile(self) -> dict[str, Any]:
        """Get profile."""
        return await self._auth.post("Profiles.Profile", "get")

    async def async_get_profile_data(self) -> dict[str, Any]:
        """Get data profile."""
        return await self._auth.post("Profiles.Profile", "getData")

    async def async_set_profile_data(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Set data profile.

        Arguments:
        - data (dict)
        - profileName (str) optional
        """
        return await self._auth.post("Profiles.Profile", "setData", conf)

    async def async_set_current(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set current profile.

        Arguments:
        - profileName (str) optional
        """
        return await self._auth.post("Profiles.Profile", "setCurrent", conf)

    async def async_get_profile_names(self) -> list[Any]:
        """Get profil names."""
        return await self._auth.post("Profiles.Profile", "getNames")


class Manifests:
    """Manifests class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_manifests(
        self, conf: dict[str, Any] | None = None
    ) -> list[Any]:
        """Get manifests.

        Argument:
        - user (str) optional
        """
        return await self._auth.post("Manifests", "get", conf)

    async def async_get_manifests_categories(self) -> list[Any]:
        """Get categories manifests."""
        return await self._auth.post("Manifests", "categories")

    async def async_get_manifests_store(self, conf: dict[str, Any]) -> None:
        """Get store manifests.

        Arguments:
        - user (str)
        - option (str)
        - data (dict)
        """
        return await self._auth.post("Manifests", "store", conf)

    async def async_retreive_manifests(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Retrieve manifests.

        Arguments:
        - user (str)
        - option (str)
        """
        return await self._auth.post("Manifests", "retrieve", conf)

    async def async_export_manifests(self) -> bool:
        """Export manifests."""
        return await self._auth.post("Manifests", "export")

    async def async_import_manifests(self) -> bool:
        """Import manifests."""
        return await self._auth.post("Manifests", "import")


class Locations:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get location.

        Argument:
        - flags (str) optional
        """
        return await self._auth.post("Locations", "get", conf)

    async def async_add_locations(self, conf: dict[str, Any]) -> None:
        """Add location.

        Arguments:
        - key (str)
        - name (str)
        - description (str) optional
        """
        return await self._auth.post("Locations", "addLocation", conf)

    async def async_del_locations(self, conf: dict[str, Any]) -> None:
        """Remove location.

        Argument:
        - key (str)
        """
        return await self._auth.post("Locations", "removeLocation", conf)

    async def async_set_locations_section(self, conf: dict[str, Any]) -> None:
        """Set location.

        Arguments:
        - location (str)
        - section (str)
        """
        return await self._auth.post("Locations", "setSection", conf)

    async def async_del_locations_section(self, conf: dict[str, Any]) -> None:
        """Remove section.

        Arguments:
        - location (str)
        - section (str)
        """
        return await self._auth.post("Locations", "removeSection", conf)

    async def async_get_locations_composition(self, conf: dict[str, Any]) -> list[Any]:
        """Get composition of location.

        Arguments:
        - location (str)
        - flags (str) optional
        """
        return await self._auth.post("Locations", "getComposition", conf)

    async def async_get_locations(self, conf: dict[str, Any]) -> list[Any]:
        """Get locations.

        Argument:
        - location (str)
        """
        return await self._auth.post("Locations", "getLocations", conf)

    # Locations.Location

    async def async_get_location(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get composition of location.

        Arguments:
        - flags (str) optional
        """
        return await self._auth.post("Locations.Location", "get", conf)


class Ssw:
    """Locations class."""

    # SSW.Steering
    # - void getNodeBackhaul((string MAC))
    # - void getUplinkInfo((string MAC))
    # - void getRoamInfo((string MAC))
    # - stationInfo getStationStats((string MAC))
    # - void getAllStationsCompactInfo()
    # - void getStationAssocLog((string MAC))
    # - list getAllStations((string ap))
    # - stationsStandards getAllStationsStandards((string ap))
    # - bool deleteStationInfo((string MAC))
    # - void setModeConfig((string mode), (string targetBroker))
    # - void getTopologyScoreInfo()

    # SSW.Steering.ExceptionList
    # - void createGmapAutoException(string query, (string target), (string type), (bool persistent), (string key))
    # - void deleteGmapAutoExceptionByKey(string key)
    # - void deleteGmapAutoExceptionByQuery(string query)
    # - void createException((string MAC), (uint8 mask), (string target), (string type))
    # - void deleteException((string MAC), (uint8 mask))

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_start_eventing(self, conf: dict[str, Any] | None = None) -> None:
        """Start eventing.

        Argument:
        - MAC (str) optional
        """
        return await self._auth.post("SSW.FeatureConfig", "startEventing", conf)

    async def async_stop_eventing(self, conf: dict[str, Any] | None = None) -> None:
        """Stop eventing.

        Argument:
        - MAC (str) optional
        """
        return await self._auth.post("SSW.FeatureConfig", "startEventing", conf)

    # SSW.FeatureConfig.MultiBackhaul
    async def async_debug_multi_blackhaul(self) -> None:
        """Debug multi backhaul."""
        return await self._auth.post(
            "SSW.FeatureConfig.MultiBackhaul", "debugMultiBackhaul"
        )

    # SSW.FeatureConfig.EnergySaving
    async def async_get_stats(self) -> None:
        """Get stats."""
        return await self._auth.post("SSW.FeatureConfig.EnergySaving", "getStats")

    # SSW.FeatureConfig.BackhaulRecovery
    async def async_provision_mac(self, conf: dict[str, Any] | None = None) -> None:
        """Provision MAC.

        Argument:
        - MAC (str) optional
        """
        return await self._auth.post(
            "SSW.FeatureConfig.BackhaulRecovery", "provisionMAC", conf
        )

    # SSW.FeatureConfig.LongStats
    async def async_get_longstats(self) -> None:
        """Get long stats."""
        return await self._auth.post(
            "SSW.FeatureConfig.LongStats", "getLongHistoryStats"
        )

    async def async_start_auto_pairing(self, conf: dict[str, Any]) -> None:
        """Start auto pairing.

        Argument:
        - MAC (str)
        - channel (int)
        """
        return await self._auth.post("SSW.FeatureConfig", "startAutoPairing", conf)


class SpeedTest:
    """Speed Test class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_wan_results(self) -> None:
        """Get wan results."""
        return await self._auth.post("SpeedTest", "getWANResults")

    async def async_get_link_info(self, conf: dict[str, Any] | None = None) -> None:
        """Get link info.

        Argument:
        - iface (str) optional
        """
        return await self._auth.post("SpeedTest", "getLinkInfo", conf)


class OrangeServices:
    """Orange Services class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_subscriptions_status(self, conf: dict[str, Any]) -> str:
        """Get subscriptions status.

        Argument:
        - refresh(bool)
        """
        return await self._auth.post("OrangeServices", "getSubscriptionStatus", conf)


class HTTPService:
    """HTTPService class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_authentication_mode(self) -> bool:
        """Get authentication modes."""
        return await self._auth.post("HTTPService", "getAuthenticationModes")

    async def async_get_current_user(self) -> bool:
        """Get current user."""
        return await self._auth.post("HTTPService", "getCurrentUser")

    # HTTPService.WebDav.DigestManager

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


class IoTService:
    """IoTService class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_status(self, conf: dict[str, Any] | None = None) -> int:
        """Get IoT Status.

        Argument:
        - status (status_t) optional
        """
        return await self._auth.post("IoTService", "getStatus", conf)

    async def async_set_status(self, conf: dict[str, Any]) -> int:
        """Get IoT Status.

        Argument:
        - status (str) optional
        """
        return await self._auth.post("IoTService", "setStatus", conf)

    async def async_get_uuid(self, conf: dict[str, Any] | None = None) -> int:
        """Get UUID.

        Argument:
        - uniqueIdentifier (str) optional
        """
        return await self._auth.post("IoTService", "getUUID", conf)
