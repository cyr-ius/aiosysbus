"""Scheduler for Internet Access."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Schedule:
    """Scheduler class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_schedule(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get schedule information.

        conf = {"parameters":{"type":"ToD","ID":"01:02:03:04:05:06"}}
        """
        return self._access.post("Scheduler", "getSchedule", conf)

    def add_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
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
        return self._access.post("Scheduler", "addSchedule", conf)

    def enable_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "enableSchedule", conf)

    def set_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "overridedSchedule", conf)

    def set_state(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "overrideState", conf)

    def remove_schedule(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "removeSchedule", conf)

    def get_scheduletypes(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "getScheduleTypes", conf)

    def get_schedules(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "getSchedules", conf)

    def get_completeschedules(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("Scheduler", "getCompleteSchedules", conf)

    def set_wlanscheduler_state(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get schedule information."""
        return self._access.post("WLanScheduler", "setState", conf)
