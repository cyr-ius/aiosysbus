"""Scheduler for Internet Access."""

class Schedule:
    """Scheduler class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_schedule(self, conf=None):
        """Get schedule information.

        conf = {"parameters":{"type":"ToD","ID":"01:02:03:04:05:06"}}
        """
        return self._access("Scheduler", "getSchedule", conf)

    def add_schedule(self, conf):
        """Add schedule.

        Enable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"override":"","base":"Weekly","def":"Enable","schedule":[]}}}
        Disable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"override":"Disable","base":"Weekly","def":"Enable","schedule":[]}}}
        Enable range week (seconds)
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"base":"Weekly","def":"Enable","override":"","value":"Enable","schedule":[{"begin":0,"end":3600,"state":"Disable"},{"begin":601200,"end":604800,"state":"Disable"}]}}}
        """
        return self._access("Scheduler", "addSchedule", conf)

    def enable_schedule(self, conf):
        """Get schedule information."""
        return self._access("Scheduler", "enableSchedule", conf)

    def set_schedule(self, conf):
        """Get schedule information."""
        return self._access("Scheduler", "overridedSchedule", conf)

    def set_state(self, conf):
        """Get schedule information."""
        return self._access("Scheduler", "overrideState", conf)

    def remove_schedule(self, conf):
        """Get schedule information."""
        return self._access("Scheduler", "removeSchedule", conf)

    def get_scheduletypes(self, conf=None):
        """Get schedule information."""
        return self._access("Scheduler", "getScheduleTypes", conf)

    def get_schedules(self, conf=None):
        """Get schedule information."""
        return self._access("Scheduler", "getSchedules", conf)

    def get_completeschedules(self, conf=None):
        """Get schedule information."""
        return self._access("Scheduler", "getCompleteSchedules", conf)

    def set_wlanscheduler_state(self, conf=None):
        """Get schedule information."""
        return self._access("WLanScheduler", "setState", conf)
