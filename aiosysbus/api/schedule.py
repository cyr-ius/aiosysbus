"""Scheduler for Internet access."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class Schedule:
    """Scheduler class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_schedule(self, conf: dict[str, Any]) -> bool:
        """Add schedule.

        Arguments:
        - type (str)
        - info (schedule_t)

        Enable MAC Address
        {"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"override":"","base":"Weekly","def":"Enable",
        "schedule":[]}}

        Disable MAC Address
        {"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"override":"Disable","base":"Weekly","def":"Enable",
        "schedule":[]}}

        Enable range week (seconds)
        {"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"base":"Weekly","def":"Enable","override":"","value":"Enable",
        "schedule":[{"begin":0,"end":3600,"state":"Disable"},
        {"begin":601200,"end":604800,"state":"Disable"}]}}
        """
        return await self._auth.post("Scheduler", "addSchedule", conf)

    async def async_update_schedule(self, conf: dict[str, Any]) -> bool:
        """Add schedule.

        Arguments:
        - type (str)
        - ID (str)
        - entries (list)
        - device (str) optional
        """
        return await self._auth.post("Scheduler", "updateScheduleEntries", conf)

    async def async_enable_schedule(self, conf: dict[str, Any]) -> bool:
        """Get schedule information.

        Arguments:
        - type (str)
        - ID (str)
        - enable (bool) optional
        - device (str) optional
        """
        return await self._auth.post("Scheduler", "enableSchedule", conf)

    async def async_enable_all(self, conf: dict[str, Any]) -> bool:
        """Get schedule information.

        Arguments:
        - type (str)
        - enable (bool)
        """
        return await self._auth.post("Scheduler", "enableAllSchedule", conf)

    async def async_set_schedule(self, conf: dict[str, Any]) -> bool:
        """Set override schedule.

        Arguments:
        - type (str)
        - ID (str)
        - override (str)
        - device (str) optional
        """
        return await self._auth.post("Scheduler", "overrideSchedule", conf)

    async def async_override_state(self, conf: dict[str, Any]) -> bool:
        """Set override schedule.

        Arguments:
        - type (str)
        - ID (str)
        - state (str)
        - device (str) optional
        """
        return await self._auth.post("Scheduler", "overrideState", conf)

    async def async_remove_schedules(self, conf: dict[str, Any]) -> bool:
        """Get schedule information.

        Arguments:
        - type (str)
        - ID (list) optional
        - device (list) optional
        """
        return await self._auth.post("Scheduler", "removeSchedules", conf)

    async def async_get_scheduletypes(self, conf: dict[str, Any] | None = None) -> bool:
        """Get schedule types.

        Arguments:
        - types (list) optional
        """
        return await self._auth.post("Scheduler", "getScheduleTypes", conf)

    async def async_get_schedules(self, conf: dict[str, Any]) -> bool:
        """Get schedules.

        Arguments:
        - type (str)
        - scheduleInfo (list) optional
        - target (list) optional
        """
        return await self._auth.post("Scheduler", "getSchedules", conf)

    async def async_get_completeschedules(self, conf: dict[str, Any]) -> bool:
        """Get schedule information.

        Arguments:
        - type (str)
        - scheduleInfo (list) optional
        - target (list) optional
        """
        return await self._auth.post("Scheduler", "getCompleteSchedules", conf)

    async def async_get_schedule(self, conf: dict[str, Any]) -> bool:
        """Get schedule information.

        Arguments:
        - type (str)
        - ID (str)
        - info (schedule_t) optional
        - device (str) optional
        """
        return await self._auth.post("Scheduler", "getSchedule", conf)

    # WLanScheduler

    async def async_set_wlan_scheduler_state(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Get schedule information.

        Arguments:
        - ID (str) optional
        - state (str) optional
        """
        return await self._auth.post("WLanScheduler", "setState", conf)
