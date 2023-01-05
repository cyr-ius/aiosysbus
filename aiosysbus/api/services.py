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

    def get_profile(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get profile."""
        return self._access.post("Profiles.Profile", "get", conf)

    def get_profile_data(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get data profile."""
        return self._access.post("Profiles.Profile", "getData", conf)

    def set_profile_data(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set data profile."""
        return self._access.post("Profiles.Profile", "setData", conf)

    def get_profile_current(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get current profile."""
        return self._access.post("Profiles.Profile", "getCurrent", conf)

    def get_profile_name(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get profil name."""
        return self._access.post("Profiles.Profile", "getNames", conf)


class Manifests:
    """Manifests class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_manifests(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get manifests."""
        return self._access.post("Manifests", "get", conf)

    def get_manifests_categories(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get categories manifests."""
        return self._access.post("Manifests", "categories", conf)

    def get_manifests_store(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get store manifests."""
        return self._access.post("Manifests", "store", conf)

    def retreive_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Retrieve manifests."""
        return self._access.post("Manifests", "retrieve", conf)

    def export_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Export manifests."""
        return self._access.post("Manifests", "export", conf)

    def import_manifests(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Import manifests."""
        return self._access.post("Manifests", "import", conf)


class DataHub:
    """DataHub class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_datahub(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get DataHub status."""
        return self._access.post("DataHub", "getStatus", conf)

    def set_datahub(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set DataHub status."""
        return self._access.post("DataHub", "setStatus", conf)

    def get_datahub_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DataHub User information."""
        return self._access.post("DataHub", "getUserInfo", conf)

    def add_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add DataHub user."""
        return self._access.post("DataHub", "addUser", conf)

    def del_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Del DataHub user."""
        return self._access.post("DataHub", "removeUser", conf)

    def set_datahub_user(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set DataHub user."""
        return self._access.post("DataHub", "setUserState", conf)

    def set_datahub_password_user(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get DataHub status."""
        return self._access.post("DataHub", "changeUserPassword", conf)

    def get_datahub_users(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get DataHub status."""
        return self._access.post("DataHub", "listUsers", conf)

    def reset_datahub(self) -> dict[str, Any] | None:
        """Get DataHub status."""
        return self._access.post("DataHub", "reset")


class Locations:
    """Locations class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_locations_domain(self, conf: dict[str, Any]) -> dict[str, Any] | None:
        """Get domain location."""
        domain = conf.pop("domain")
        return self._access.post(f"Locations.Location.{domain}", "get", conf)

    def get_locations(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get location."""
        return self._access.post("Locations", "getLocations", conf)

    def add_locations(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add location."""
        return self._access.post("Locations", "addLocation", conf)

    def del_locations(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove location."""
        return self._access.post("Locations", "removeLocation", conf)

    def set_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set location."""
        return self._access.post("Locations", "setSection", conf)

    def del_locations_section(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove section."""
        return self._access.post("Locations", "removeSection", conf)

    def get_locations_composition(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get composition of location."""
        return self._access.post("Locations", "getComposition", conf)


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
