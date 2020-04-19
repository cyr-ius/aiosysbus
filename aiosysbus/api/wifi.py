class Wifi:
    def __init__(self, access):
        self._access = access

    def get_wifi(self, conf=None):
        """ Get wifi configuration """
        return self._access.post("NMC.Wifi", "get", conf)

    def set_wifi(self, conf):
        """ Set wifi configuration """
        return self._access.post("NMC.Wifi", "set", conf)

    def get_wifi_Stats(self, conf=None):
        """ Wifi Statistics """
        return self._access.post("NMC.Wifi", "getStats", conf)

    def get_openmode_Status(self, conf=None):
        """ Get Wifi sharing information """
        return self._access.post("Wificom.OpenMode", "getStatus", conf)

    def get_securemode_Status(self, conf=None):
        """ Get secure for wifi """
        return self._access.post("Wificom.SecureMode", "getStatus", conf)
