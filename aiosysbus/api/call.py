"""DECT, VoiceService and Phone book."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Call:
    """Call class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def get_voip(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get VIOP configuration."""
        return self._access.post("NMC", "getVoIPConfig", conf)

    def get_voiceapplication_listHandsets(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Handsets."""
        return self._access.post("VoiceService.VoiceApplication", "listHandsets", conf)

    def get_voiceapplication_listTrunks(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Trunks."""
        return self._access.post("VoiceService.VoiceApplication", "listTrunks", conf)

    def get_voiceapplication_calllist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Calls."""
        return self._access.post("VoiceService.VoiceApplication", "getCallList", conf)

    def get_voiceapplication_clearlist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Clear Call list.

        conf = {"callId":"xx"} or empty for all
        """
        return self._access.post("VoiceService.VoiceApplication", "clearCallList", conf)

    def set_voiceapplication_ring(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set Ring."""
        return self._access.post("VoiceService.VoiceApplication", "ring", conf)

    def set_dect_startPairing(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Appairing DECT."""
        return self._access.post("DECT", "startPairing", conf)

    def get_dect_pin(self) -> dict[str, Any] | None:
        """Get Pin code for DECT."""
        return self._access.post("DECT", "getPIN")

    def set_dect_pin(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set Pin code for DECT."""
        return self._access.post("DECT", "setPIN", conf)

    def get_dect_version(self) -> dict[str, Any] | None:
        """Get DECT version."""
        return self._access.post("DECT", "getVersion")

    def get_dect_standardversion(self) -> dict[str, Any] | None:
        """Get standard version."""
        return self._access.post("DECT", "getStandardVersion")

    def get_dect_rfpi(self) -> dict[str, Any] | None:
        """Get RFPI."""
        return self._access.post("DECT", "getRFPI")


class Phonebook:
    """contacts book."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    def add_contact_uuid(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add contact and generate UUID."""
        return self._access.post("Phonebook", "addContactAndGenUUID", conf)

    def add_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add contact."""
        return self._access.post("Phonebook", "addContact", conf)

    def add_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """All multiple contacts."""
        return self._access.post("Phonebook", "addContacts", conf)

    def del_contact_uid(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove contact by UID."""
        return self._access.post("Phonebook", "removeContactByUniqueID", conf)

    def del_contact_name(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove contact by name."""
        return self._access.post("Phonebook", "removeContactByFormattedName", conf)

    def del_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove contact."""
        return self._access.post("Phonebook", "removeContact", conf)

    def del_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove all contacts."""
        return self._access.post("Phonebook", "removeAllContacts", conf)

    def get_contact_uid(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get contact by UID."""
        return self._access.post("Phonebook", "getContactByUniqueID", conf)

    def get_contact_name(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get contact by name."""
        return self._access.post("Phonebook", "getContactByFormattedName", conf)

    def get_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get contact."""
        return self._access.post("Phonebook", "getContact", conf)

    def get_contact_number(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get contact by number."""
        return self._access.post("Phonebook", "getContactByNumber", conf)

    def get_contact_username(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get contact by username."""
        return self._access.post("Phonebook", "getContactByUsername", conf)

    def get_contacts(self) -> dict[str, Any] | None:
        """Get all contacts."""
        return self._access.post("Phonebook", "getAllContacts")

    def get_count(self) -> dict[str, Any] | None:
        """Count contacts."""
        return self._access.post("Phonebook", "getNumberOfContacts")

    def get_maxnumber(self) -> dict[str, Any] | None:
        """Max number of contacts."""
        return self._access.post("Phonebook", "getMaxNumberOfContacts")

    def set_contact_uid(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set contact by uid."""
        return self._access.post("Phonebook", "modifyContactByUniqueID", conf)

    def set_contact_name(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set contact by name."""
        return self._access.post("Phonebook", "modifyContactByFormattedName", conf)

    def set_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set contact."""
        return self._access.post("Phonebook", "modifyContact", conf)
