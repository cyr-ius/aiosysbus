class Call:
    def __init__(self, access):
        self._access = access

    def get_voip(self, conf=None):
        """ Get VIOP configuration """
        return self._access.post("NMC", "getVoIPConfig", conf)

    def get_voiceapplication_listHandsets(self, conf=None):
        """ Get Handsets """
        return self._access.post("VoiceService.VoiceApplication", "listHandsets", conf)

    def get_voiceapplication_listTrunks(self, conf=None):
        """ Get Trunks """
        return self._access.post("VoiceService.VoiceApplication", "listTrunks", conf)

    def set_dect_startPairing(self):
        """ Appairing DECT """
        return self._access.post("DECT", "startPairing")

    def get_dect_Pin(self, conf=None):
        """ Get Pin code for DECT """
        return self._access.post("DECT", "getPIN", conf)

    def set_dect_Pin(self, conf):
        """ Set Pin code for DECT """
        return self._access.post("DECT", "setPIN", conf)

    def get_dect_Version(self, conf=None):
        """ Get DECT version """
        return self._access.post("DECT", "getVersion", conf)

    def get_dect_StandardVersion(self, conf=None):
        """ Get standard version """
        return self._access.post("DECT", "getStandardVersion", conf)

    def get_dect_RFPI(self, conf=None):
        """ Get RFPI """
        return self._access.post("DECT", "getRFPI", conf)
