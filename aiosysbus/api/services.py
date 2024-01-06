"""Services and co."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Profiles:
    """Profiles class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_profile(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get profile."""
        return await self._auth.post("Profiles.Profile", "get", conf)

    async def async_get_profile_data(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get data profile."""
        return await self._auth.post("Profiles.Profile", "getData", conf)

    async def async_set_profile_data(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set data profile."""
        return await self._auth.post("Profiles.Profile", "setData", conf)

    async def async_get_profile_current(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get current profile."""
        return await self._auth.post("Profiles.Profile", "getCurrent", conf)

    async def async_get_profile_name(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get profil name."""
        return await self._auth.post("Profiles.Profile", "getNames", conf)


class Manifests:
    """Manifests class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_manifests(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get manifests."""
        return await self._auth.post("Manifests", "get", conf)

    async def async_get_manifests_categories(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get categories manifests."""
        return await self._auth.post("Manifests", "categories", conf)

    async def async_get_manifests_store(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get store manifests."""
        return await self._auth.post("Manifests", "store", conf)

    async def async_retreive_manifests(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Retrieve manifests."""
        return await self._auth.post("Manifests", "retrieve", conf)

    async def async_export_manifests(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Export manifests."""
        return await self._auth.post("Manifests", "export", conf)

    async def async_import_manifests(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Import manifests."""
        return await self._auth.post("Manifests", "import", conf)


class DataHub:
    """DataHub class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_datahub(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DataHub status."""
        return await self._auth.post("DataHub", "getStatus", conf)

    async def async_set_datahub(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set DataHub status."""
        return await self._auth.post("DataHub", "setStatus", conf)

    async def async_get_datahub_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DataHub User information."""
        return await self._auth.post("DataHub", "getUserInfo", conf)

    async def async_add_datahub_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Add DataHub user."""
        return await self._auth.post("DataHub", "addUser", conf)

    async def async_del_datahub_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Del DataHub user."""
        return await self._auth.post("DataHub", "removeUser", conf)

    async def async_set_datahub_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set DataHub user."""
        return await self._auth.post("DataHub", "setUserState", conf)

    async def async_set_datahub_password_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get DataHub status."""
        return await self._auth.post("DataHub", "changeUserPassword", conf)

    async def async_get_datahub_users(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DataHub status."""
        return await self._auth.post("DataHub", "listUsers", conf)

    async def async_reset_datahub(self) -> dict[str, Any]:
        """Get DataHub status."""
        return await self._auth.post("DataHub", "reset")


class Locations:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_locations_domain(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get domain location."""
        domain = conf.pop("domain")
        return await self._auth.post(f"Locations.Location.{domain}", "get", conf)

    async def async_get_locations(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get location."""
        return await self._auth.post("Locations", "getLocations", conf)

    async def async_add_locations(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Add location."""
        return await self._auth.post("Locations", "addLocation", conf)

    async def async_del_locations(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Remove location."""
        return await self._auth.post("Locations", "removeLocation", conf)

    async def async_set_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set location."""
        return await self._auth.post("Locations", "setSection", conf)

    async def async_del_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Remove section."""
        return await self._auth.post("Locations", "removeSection", conf)

    async def async_get_locations_composition(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get composition of location."""
        return await self._auth.post("Locations", "getComposition", conf)


class Domino:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth


class Ssw:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth


class RuleFactory:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth


class RuleEngine:
    """Rule Engine class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth


class Zwave:
    """Locations class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth
