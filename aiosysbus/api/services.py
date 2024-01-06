"""Services and co."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Profiles:
    """Profiles class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_get_profile(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get profile."""
        return await self._access.post("Profiles.Profile", "get", conf)

    async def async_get_profile_data(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get data profile."""
        return await self._access.post("Profiles.Profile", "getData", conf)

    async def async_set_profile_data(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set data profile."""
        return await self._access.post("Profiles.Profile", "setData", conf)

    async def async_get_profile_current(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get current profile."""
        return await self._access.post("Profiles.Profile", "getCurrent", conf)

    async def async_get_profile_name(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get profil name."""
        return await self._access.post("Profiles.Profile", "getNames", conf)


class Manifests:
    """Manifests class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_get_manifests(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get manifests."""
        return await self._access.post("Manifests", "get", conf)

    async def async_get_manifests_categories(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get categories manifests."""
        return await self._access.post("Manifests", "categories", conf)

    async def async_get_manifests_store(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get store manifests."""
        return await self._access.post("Manifests", "store", conf)

    async def async_retreive_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Retrieve manifests."""
        return await self._access.post("Manifests", "retrieve", conf)

    async def async_export_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Export manifests."""
        return await self._access.post("Manifests", "export", conf)

    async def async_import_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Import manifests."""
        return await self._access.post("Manifests", "import", conf)


class DataHub:
    """DataHub class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_get_datahub(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get DataHub status."""
        return await self._access.post("DataHub", "getStatus", conf)

    async def async_set_datahub(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set DataHub status."""
        return await self._access.post("DataHub", "setStatus", conf)

    async def async_get_datahub_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DataHub User information."""
        return await self._access.post("DataHub", "getUserInfo", conf)

    async def async_add_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add DataHub user."""
        return await self._access.post("DataHub", "addUser", conf)

    async def async_del_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Del DataHub user."""
        return await self._access.post("DataHub", "removeUser", conf)

    async def async_set_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set DataHub user."""
        return await self._access.post("DataHub", "setUserState", conf)

    async def async_set_datahub_password_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get DataHub status."""
        return await self._access.post("DataHub", "changeUserPassword", conf)

    async def async_get_datahub_users(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DataHub status."""
        return await self._access.post("DataHub", "listUsers", conf)

    async def async_reset_datahub(self) -> dict[str, Any] | None:
        """Get DataHub status."""
        return await self._access.post("DataHub", "reset")


class Locations:
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_get_locations_domain(self, conf: dict[str, Any]) -> dict[str, Any] | None:
        """Get domain location."""
        domain = conf.pop("domain")
        return await self._access.post(f"Locations.Location.{domain}", "get", conf)

    async def async_get_locations(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get location."""
        return await self._access.post("Locations", "getLocations", conf)

    async def async_add_locations(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add location."""
        return await self._access.post("Locations", "addLocation", conf)

    async def async_del_locations(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove location."""
        return await self._access.post("Locations", "removeLocation", conf)

    async def async_set_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set location."""
        return await self._access.post("Locations", "setSection", conf)

    async def async_del_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove section."""
        return await self._access.post("Locations", "removeSection", conf)

    async def async_get_locations_composition(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get composition of location."""
        return await self._access.post("Locations", "getComposition", conf)


class Domino:  # pylint: disable=[too-few-public-methods]
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access


class Ssw:  # pylint: disable=[too-few-public-methods]
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access


class RuleFactory:  # pylint: disable=[too-few-public-methods]
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access


class RuleEngine:  # pylint: disable=[too-few-public-methods]
    """Rule Engine class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access


class Zwave:  # pylint: disable=[too-few-public-methods]
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access
