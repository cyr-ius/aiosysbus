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

    async def get_voip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get VIOP configuration."""
        return await self._access.post("NMC", "getVoIPConfig", conf)

    async def get_voiceapplication_listHandsets(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Handsets."""
        return await self._access.post(
            "VoiceService.VoiceApplication", "listHandsets", conf
        )

    async def get_voiceapplication_listTrunks(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Trunks."""
        return await self._access.post(
            "VoiceService.VoiceApplication", "listTrunks", conf
        )

    async def get_voiceapplication_calllist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Calls."""
        return await self._access.post(
            "VoiceService.VoiceApplication", "getCallList", conf
        )

    async def get_voiceapplication_clearlist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Clear Call list.

        conf = {"callId":"xx"} or empty for all
        """
        return await self._access.post(
            "VoiceService.VoiceApplication", "clearCallList", conf
        )

    async def set_voiceapplication_ring(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set Ring."""
        return await self._access.post("VoiceService.VoiceApplication", "ring", conf)

    async def set_dect_startPairing(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Appairing DECT."""
        return await self._access.post("DECT", "startPairing", conf)

    async def get_dect_pin(self) -> dict[str, Any] | None:
        """Get Pin code for DECT."""
        return await self._access.post("DECT", "getPIN")

    async def set_dect_pin(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set Pin code for DECT."""
        return await self._access.post("DECT", "setPIN", conf)

    async def get_dect_version(self) -> dict[str, Any] | None:
        """Get DECT version."""
        return await self._access.post("DECT", "getVersion")

    async def get_dect_standardversion(self) -> dict[str, Any] | None:
        """Get standard version."""
        return await self._access.post("DECT", "getStandardVersion")

    async def get_dect_rfpi(self) -> dict[str, Any] | None:
        """Get RFPI."""
        return await self._access.post("DECT", "getRFPI")


class Phonebook:
    """contacts book."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def add_contact_uuid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Add contact and generate UUID."""
        return await self._access.post("Phonebook", "addContactAndGenUUID", conf)

    async def add_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Add contact."""
        return await self._access.post("Phonebook", "addContact", conf)

    async def add_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """All multiple contacts."""
        return await self._access.post("Phonebook", "addContacts", conf)

    async def del_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove contact by UID."""
        return await self._access.post("Phonebook", "removeContactByUniqueID", conf)

    async def del_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Remove contact by name."""
        return await self._access.post(
            "Phonebook", "removeContactByFormattedName", conf
        )

    async def del_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove contact."""
        return await self._access.post("Phonebook", "removeContact", conf)

    async def del_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Remove all contacts."""
        return await self._access.post("Phonebook", "removeAllContacts", conf)

    async def get_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get contact by UID."""
        return await self._access.post("Phonebook", "getContactByUniqueID", conf)

    async def get_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get contact by name."""
        return await self._access.post("Phonebook", "getContactByFormattedName", conf)

    async def get_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get contact."""
        return await self._access.post("Phonebook", "getContact", conf)

    async def get_contact_number(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get contact by number."""
        return await self._access.post("Phonebook", "getContactByNumber", conf)

    async def get_contact_username(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Get contact by username."""
        return await self._access.post("Phonebook", "getContactByUsername", conf)

    async def get_contacts(self) -> dict[str, Any] | None:
        """Get all contacts."""
        return await self._access.post("Phonebook", "getAllContacts")

    async def get_count(self) -> dict[str, Any] | None:
        """Count contacts."""
        return await self._access.post("Phonebook", "getNumberOfContacts")

    async def get_maxnumber(self) -> dict[str, Any] | None:
        """Max number of contacts."""
        return await self._access.post("Phonebook", "getMaxNumberOfContacts")

    async def set_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set contact by uid."""
        return await self._access.post("Phonebook", "modifyContactByUniqueID", conf)

    async def set_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set contact by name."""
        return await self._access.post(
            "Phonebook", "modifyContactByFormattedName", conf
        )

    async def set_contact(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set contact."""
        return await self._access.post("Phonebook", "modifyContact", conf)
