"""System information."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class PnP:
    """System class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self) -> list[Any]:
        """Get Plug&play."""
        return await self._auth.post("PnP", "get")


class Wol:
    """WOL class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_send_wol(self, conf: dict[str, Any]) -> None:
        """Send wake on lan.

        Argument:
        - hostID (str)
        - intf (str) optional
        - password (str) optional
        - broadcast (str) optional
        - retries (int) optional
        - interval (int) optional
        """
        return await self._auth.post("WOL", "sendWakeOnLan", conf)


class Probe:
    """Probe class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_log_events(self, events: Any) -> None:
        """Get log events.

        Argument:
        - events (plib_event_list_t)
        """
        return await self._auth.post("Probe", "logEvents", {"events": events})

    async def async_add_probe_tag(self, conf: dict[str, Any]) -> bool:
        """Add tag.

        Argument:
        - tag (str)
        """
        return await self._auth.post("Probe", "addTag", conf)

    async def async_delete_probe_tag(self, conf: dict[str, Any]) -> bool:
        """Remove tag.

        Argument:
        - tag (str)
        """
        return await self._auth.post("Probe", "removeTag", conf)

    async def async_clear_probe_tags(self) -> bool:
        """Clear all tags."""
        return await self._auth.post("Probe", "clearTags")

    # Probe.Configuration
    # - void setConfiguration(string type, string name, uint32 id, uint32 interval)
    # - list getConfiguration(string type)
    # - list getConfigurations()
    # - void removeConfiguration(string type)

    # ############ HOSTS #############

    async def async_get_hosts(self) -> dict[str, Any]:
        """Get devices."""
        return await self._auth.post("Hosts", "getDevices")

    async def async_set_hosts_name(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Set host name."""
        return await self._auth.post("Hosts", "setName", conf)

    async def async_del_hosts(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Remove hosts."""
        return await self._auth.post("Hosts", "delHost", conf)

    async def async_set_hosts_device(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Set host device."""
        return await self._auth.post("Hosts", "setDevice", conf)


class Time:
    """Time class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_time(self, conf: dict[str, Any] | None = None) -> bool:
        """Get time.

        Argument:
        - time (str) optional
        """
        return await self._auth.post("Time", "getTime", conf)

    async def async_get_utctime(self, conf: dict[str, Any] | None = None) -> None:
        """Get UTC time.

        Argument:
        - time (str) optional
        """
        return await self._auth.post("Time", "getUTCTime", conf)

    async def async_get_status(self, conf: dict[str, Any] | None = None) -> None:
        """Get status.

        Argument:
        - status (str) optional
        """
        return await self._auth.post("Time", "getStatus", conf)

    async def async_get_ntp(self, conf: dict[str, Any] | None = None) -> None:
        """Get ntp servers.

        Argument:
        - servers (dict) optional
        """
        return await self._auth.post("Time", "getNTPServers", conf)

    async def async_get_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Get local zone.

        Argument:
        - timezone (dict) optional
        """
        return await self._auth.post("Time", "getLocalTimeZoneName", conf)

    async def async_set_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Set local zone.

        Argument:
        - timezone (dict) optional
        """
        return await self._auth.post("Time", "setLocalTimeZoneName", conf)

    async def async_list_localtime_zonename(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """List local zone.

        Argument:
        - timezones (list) optional
        """
        return await self._auth.post("Time", "listLocalTimeZoneNames", conf)


class PasswordRecovery:
    """Password Recovery class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_start(self) -> None:
        """Recovery password start."""
        return await self._auth.post("PasswordRecovery", "start")

    async def async_stop(self) -> None:
        """Recovery password stop."""
        return await self._auth.post("PasswordRecovery", "stop")

    async def async_set_password(self, conf: dict[str, Any] | None = None) -> int:
        """Set password.

        Argument:
        - password (str)
        """
        return await self._auth.post("PasswordRecovery", "setPassword", conf)


class RemoteAccess:
    """Remote access class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get(self) -> dict[str, Any]:
        """Get."""
        return await self._auth.post("RemoteAccess", "get")

    async def async_set(self, parameters: dict[str, Any] | None = None) -> bool:
        """Set.

        Argument:
        - parameters (dict)
        """
        return await self._auth.post("RemoteAccess", "set", {"parameters": parameters})

    async def async_enable(self, conf: dict[str, Any] | None = None) -> int:
        """Enable.

        Argument:
        - port (int)
        - secure (bool)
        - timeout (int)
        - sourcePrefix (str)
        """
        return await self._auth.post("RemoteAccess", "enable", conf)

    async def async_disable(self) -> bool:
        """Disable."""
        return await self._auth.post("RemoteAccess", "disable")

    async def async_get_time_left(self) -> int:
        """Get time left."""
        return await self._auth.post("RemoteAccess", "getTimeLeft")

    async def async_restart_timer(self) -> bool:
        """Restart timer."""
        return await self._auth.post("RemoteAccess", "restartTimer")


class OrangeRemoteAccess:
    """Orange remote access class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_user(self, conf: dict[str, Any]) -> None:
        """Get wan results.

        Argument:
        - username (str)
        - cookie (str)
        """
        return await self._auth.post("OrangeRemoteAccess", "addUser", conf)

    async def async_delete_user(self, conf: dict[str, Any]) -> None:
        """Get wan results.

        Argument:
        - username (str)
        """
        return await self._auth.post("OrangeRemoteAccess", "removeUser", conf)

    async def async_list_users(self, conf: dict[str, Any] | None = None) -> None:
        """Get wan results.

        Argument:
        - listOfUsers (list) optional
        """
        return await self._auth.post("OrangeRemoteAccess", "listUsers", conf)

    async def async_get(self) -> dict[str, Any]:
        """Get Orange remote access."""
        return await self._auth.post("OrangeRemoteAccess", "get")

    async def async_set(self, conf: dict[str, Any] | None = None) -> bool:
        """Set Orange remote access.

        Argument:
        - parameters (dict) optional
        """
        return await self._auth.post("OrangeRemoteAccess", "set", conf)

    # OrangeRemoteAccess.OnDemand

    async def async_get_ondemand(self) -> dict[str, Any]:
        """Get Orange remote access on demand."""
        return await self._auth.post("OrangeRemoteAccess.OnDemand", "get")

    async def async_set_ondemand(self, conf: dict[str, Any] | None = None) -> bool:
        """Set Orange remote access on demand.

        Argument:
        - parameters (dict) optional
        """
        return await self._auth.post("OrangeRemoteAccess.OnDemand", "set", conf)


class Screen:
    """Screen."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_set_anonymous_display(self) -> None:
        """Set Anonymous display."""
        return await self._auth.post("Screen", "setAnonymousDisplay")

    async def async_set_show_wifi_password(self, conf: dict[str, Any]) -> None:
        """Set wifi password (display on box).

        Argument:
        - Enable (bool)
        """
        return await self._auth.post("Screen", "setShowWifiPassword", conf)

    async def async_get_show_wifi_password(self) -> bool:
        """Show status display wifi password (display on box)."""
        return await self._auth.post("Screen", "getShowWifiPassword")


class UserInterface:
    """User interface."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_language(self, conf: dict[str, Any] | None = None) -> str:
        """Get language.

        Arguments:
        - availableLanguages (str) optional
        """
        return await self._auth.post("UserInterface", "getLanguage", conf)

    async def async_set_language(self, conf: dict[str, Any]) -> bool:
        """Set language.

        Arguments:
        - currentLanguage (str)
        """
        return await self._auth.post("UserInterface", "setLanguage", conf)

    async def async_set_state(self, conf: dict[str, Any]) -> str:
        """Set state.

        Arguments:
        - currentState (str)
        """
        return await self._auth.post("UserInterface", "setState", conf)

    async def async_get_state(self) -> str:
        """Get state."""
        return await self._auth.post("UserInterface", "getState")

    async def async_export(self, conf: dict[str, Any] | None = None) -> bool:
        """Export.

        Arguments:
        - fileName (str) optional
        """
        return await self._auth.post("UserInterface", "export", conf)

    async def async_import(self, conf: dict[str, Any] | None = None) -> bool:
        """Import.

        Arguments:
        - fileName (str) optional
        """
        return await self._auth.post("UserInterface", "import", conf)

    async def async_get_debuginfo(self) -> dict[str, Any]:
        """Get debug information."""
        return await self._auth.post("UserInterface", "getDebugInformation")


class Event:
    """Event class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_events(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get all events."""
        return await self._auth.post("eventmanager", "get_events", conf)

    async def async_open_channel(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Open channel."""
        return await self._auth.post("eventmanager", "open_channel", conf)

    async def async_subscribe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Subscribe Event."""
        return await self._auth.post("eventmanager", "subscribe", conf)

    async def async_unsubscribe(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Unsubscribe Event."""
        return await self._auth.post("eventmanager", "unsubscribe", conf)


class History:
    """History"""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_updateHistory(self) -> None:
        """Update backup history."""
        await self._auth.post("History.Backup", "updateHistory")

    async def async_cleanHistory(self) -> None:
        """Clean backup history."""
        await self._auth.post("History.Backup", "cleanHistory")

    async def async_getSimpleHistory(self) -> None:
        """Get backup history."""
        await self._auth.post("History.Backup", "getSimpleHistory")

    async def async_rotate(self, conf: dict[str, Any] | None = None) -> None:
        """Rotate backup history.

        Arguments:
        - source (str) optional
        """
        await self._auth.post("History.Backup", "rotate", conf)
