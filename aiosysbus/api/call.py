"""DECT, VoiceService and Phone book."""

class Call:
    """Call class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def get_voip(self, conf=None):
        """Get VIOP configuration."""
        return self._access.post("NMC", "getVoIPConfig", conf)

    def get_voiceapplication_listHandsets(self, conf=None):
        """Get Handsets."""
        return self._access.post("VoiceService.VoiceApplication", "listHandsets", conf)

    def get_voiceapplication_listTrunks(self, conf=None):
        """Get Trunks."""
        return self._access.post("VoiceService.VoiceApplication", "listTrunks", conf)

    def get_voiceapplication_calllist(self, conf=None):
        """Get Calls."""
        return self._access.post("VoiceService.VoiceApplication", "getCallList", conf)

    def get_voiceapplication_clearlist(self, conf=None):
        """Clear Call list.

        conf = {"callId":"xx"} or empty for all
        """
        return self._access.post("VoiceService.VoiceApplication", "clearCallList", conf)
    
    def set_voiceapplication_ring(self, conf=None):
        """Set Ring."""
        return self._access.post("VoiceService.VoiceApplication", "ring", conf)

    def set_dect_startPairing(self, conf):
        """Appairing DECT."""
        return self._access.post("DECT", "startPairing", conf)

    def get_dect_pin(self):
        """Get Pin code for DECT."""
        return self._access.post("DECT", "getPIN")

    def set_dect_pin(self, conf):
        """Set Pin code for DECT."""
        return self._access.post("DECT", "setPIN", conf)

    def get_dect_version(self):
        """Get DECT version."""
        return self._access.post("DECT", "getVersion")

    def get_dect_standardversion(self):
        """Get standard version."""
        return self._access.post("DECT", "getStandardVersion")

    def get_dect_rfpi(self):
        """Get RFPI."""
        return self._access.post("DECT", "getRFPI")


class Phonebook:
    """contacts book."""

    def __init__(self, access):
        """Init."""
        self._access = access

    def add_contact_uuid(self, conf):
        """Add contact and generate UUID."""
        return self._access.post("Phonebook", "addContactAndGenUUID", conf)

    def add_contact(self, conf):
        """Add contact."""
        return self._access.post("Phonebook", "addContact", conf)

    def add_contacts(self, conf):
        """All multiple contacts."""
        return self._access.post("Phonebook", "addContacts", conf)

    def del_contact_uid(self, conf):
        """Remove contact by UID."""
        return self._access.post("Phonebook", "removeContactByUniqueID", conf)

    def del_contact_name(self, conf):
        """Remove contact by name."""
        return self._access.post("Phonebook", "removeContactByFormattedName", conf)

    def del_contact(self, conf):
        """Remove contact."""
        return self._access.post("Phonebook", "removeContact", conf)

    def del_contacts(self, conf):
        """Remove all contacts."""
        return self._access.post("Phonebook", "removeAllContacts", conf)

    def get_contact_uid(self, conf):
        """Get contact by UID."""
        return self._access.post("Phonebook", "getContactByUniqueID", conf)

    def get_contact_name(self, conf):
        """Get contact by name."""
        return self._access.post("Phonebook", "getContactByFormattedName", conf)

    def get_contact(self, conf):
        """Get contact."""
        return self._access.post("Phonebook", "getContact", conf)

    def get_contact_number(self, conf):
        """Get contact by number."""
        return self._access.post("Phonebook", "getContactByNumber", conf)

    def get_contact_username(self, conf):
        """Get contact by username."""
        return self._access.post("Phonebook", "getContactByUsername", conf)

    def get_contacts(self):
        """Get all contacts."""
        return self._access.post("Phonebook", "getAllContacts")

    def get_count(self):
        """Count contacts."""
        return self._access.post("Phonebook", "getNumberOfContacts")

    def get_maxnumber(self):
        """Max number of contacts."""
        return self._access.post("Phonebook", "getMaxNumberOfContacts")

    def set_contact_uid(self, conf):
        """Set contact by uid."""
        return self._access.post("Phonebook", "modifyContactByUniqueID", conf)

    def set_contact_name(self, conf):
        """Set contact by name."""
        return self._access.post("Phonebook", "modifyContactByFormattedName", conf)

    def set_contact(self, conf):
        """Set contact."""
        return self._access.post("Phonebook", "modifyContact", conf)
