"""Power Management."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class PowerManagement:
    """PowerManagement class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_supported_modes(self) -> dict[str, Any]:
        """Get supported modes."""
        return await self._auth.post("PowerManagement", "getSupportedModes")

    async def async_get_supported_triggers(self) -> dict[str, Any]:
        """Get supported triggers."""
        return await self._auth.post("PowerManagement", "getSupportedTriggers")

    async def async_set_profiles(
        self, profiles: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Set profiles.

        Argument:
        - profiles (list)
        """
        return await self._auth.post(
            "PowerManagement", "setProfiles", {"profiles": profiles}
        )

    async def async_set_scheduled_profiles(
        self, profiles: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Set scheduled profiles.

        Argument:
        - profiles (list)
        """
        return await self._auth.post(
            "PowerManagement", "setScheduledProfiles", {"profiles": profiles}
        )

    async def async_set_scheduled_profiles_override(
        self, overrides: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Set scheduled profiles override.

        Argument:
        - overrides (list)
        """
        return await self._auth.post(
            "PowerManagement", "setScheduledProfilesOverride", {"overrides": overrides}
        )

    async def async_set_triggered_profiles(
        self, profiles: list[dict[str, Any]]
    ) -> dict[str, Any]:
        """Set triggered profiles.

        Argument:
        - profiles (list)
        """
        return await self._auth.post(
            "PowerManagement", "setTriggeredProfiles", {"profiles": profiles}
        )

    async def async_get_profiles(
        self, conf: list[dict[str, Any]] | None = None
    ) -> dict[str, Any]:
        """Get profiles.

        Argument:
        - profiles (list)
        """
        return await self._auth.post("PowerManagement", "getProfiles", conf)

    async def async_delete_profiles(
        self, conf: list[dict[str, Any]] | None = None
    ) -> None:
        """Remove profiles.

        Argument:
        - profiles (list)
        """
        await self._auth.post("PowerManagement", "removeProfiles", conf)

    async def async_set_state(self, id: str, state: str) -> None:
        """Remove profiles.

        Argument:
        - ID (str)
        - state (str)
        """
        await self._auth.post("PowerManagement", "setState", {"ID": id, "state": state})

    async def async_import(self) -> bool:
        """Import."""
        return await self._auth.post("PowerManagement", "import")

    async def async_export(self) -> bool:
        """Export."""
        return await self._auth.post("PowerManagement", "export")
