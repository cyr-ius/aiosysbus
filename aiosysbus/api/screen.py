class Screen:
    def __init__(self, access):
        self._access = access

    def get_ShowWifiPassword(self):
        """ Show wifi password (display on box) """
        return self._access.post("Screen", "getShowWifiPassword")
