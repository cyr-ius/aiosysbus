class Schedule:
    """Scheduler for device."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_schedule(self, conf=None):
        """Get schedule information.

        conf = {"parameters":{"type":"ToD","ID":"01:02:03:04:05:06"}}
        """
        return self._access("Scheduler", "getSchedule", conf)

    def add_schedule(self, conf=None):
        """Add schedule.

        Enable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"override":"","base":"Weekly","def":"Enable","schedule":[]}}}
        Disable MAC Address
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"override":"Disable","base":"Weekly","def":"Enable","schedule":[]}}}
        Enable range week (seconds)
        conf = {"parameters":{"type":"ToD","info":{"ID":"01:02:03:04:05:06","enable":true,"base":"Weekly","def":"Enable","override":"","value":"Enable","schedule":[{"begin":0,"end":3600,"state":"Disable"},{"begin":601200,"end":604800,"state":"Disable"}]}}}
        """
        return self._access("Scheduler", "addSchedule", conf)