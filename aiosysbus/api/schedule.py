"""Scheduler for Internet access."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Schedule:
    """Scheduler class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_schedule(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get schedule information.

        conf = {"parameters":{"type":"ToD","ID":"01:02:03:04:05:06"}}
        """
        return await self._auth.post("Scheduler", "getSchedule", conf)

    async def async_add_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Add schedule.

        Enable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"override":"","base":"Weekly","def":"Enable",
        "schedule":[]}}}

        Disable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"override":"Disable","base":"Weekly","def":"Enable",
        "schedule":[]}}}

        Enable range week (seconds)
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06",
        "enable":true,"base":"Weekly","def":"Enable","override":"","value":"Enable",
        "schedule":[{"begin":0,"end":3600,"state":"Disable"},
        {"begin":601200,"end":604800,"state":"Disable"}]}}}
        """
        return await self._auth.post("Scheduler", "addSchedule", conf)

    async def async_enable_schedule(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "enableSchedule", conf)

    async def async_set_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "overrideSchedule", conf)

    async def async_set_state(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "overrideState", conf)

    async def async_remove_schedule(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "removeSchedule", conf)

    async def async_get_scheduletypes(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "getScheduleTypes", conf)

    async def async_get_schedules(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "getSchedules", conf)

    async def async_get_completeschedules(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("Scheduler", "getCompleteSchedules", conf)

    async def async_set_wlanscheduler_state(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get schedule information."""
        return await self._auth.post("WLanScheduler", "setState", conf)
