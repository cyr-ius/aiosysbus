"""DECT, VoiceService and Phone book."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class Call:
    """Call class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_voip(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get VIOP configuration."""
        return await self._auth.post("NMC", "getVoIPConfig", conf)

    async def async_get_voiceapplication_listHandsets(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Handsets."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "listHandsets", conf
        )

    async def async_get_voiceapplication_listTrunks(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Trunks."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "listTrunks", conf
        )

    async def async_get_voiceapplication_calllist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Calls."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "getCallList", conf
        )

    async def async_get_voiceapplication_clearlist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Clear Call list.

        conf = {"callId":"xx"} or empty for all
        """
        return await self._auth.post(
            "VoiceService.VoiceApplication", "clearCallList", conf
        )

    async def async_set_voiceapplication_ring(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Set Ring."""
        return await self._auth.post("VoiceService.VoiceApplication", "ring", conf)

    async def async_set_dect_startPairing(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Appairing DECT."""
        return await self._auth.post("DECT", "startPairing", conf)

    async def async_get_dect_pin(self) -> dict[str, Any]:
        """Get Pin code for DECT."""
        return await self._auth.post("DECT", "getPIN")

    async def async_set_dect_pin(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set Pin code for DECT."""
        return await self._auth.post("DECT", "setPIN", conf)

    async def async_get_dect_version(self) -> dict[str, Any]:
        """Get DECT version."""
        return await self._auth.post("DECT", "getVersion")

    async def async_get_dect_standardversion(self) -> dict[str, Any]:
        """Get standard version."""
        return await self._auth.post("DECT", "getStandardVersion")

    async def async_get_dect_rfpi(self) -> dict[str, Any]:
        """Get RFPI."""
        return await self._auth.post("DECT", "getRFPI")


class Phonebook:
    """contacts book."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_contact_uuid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Add contact and generate UUID."""
        return await self._auth.post("Phonebook", "addContactAndGenUUID", conf)

    async def async_add_contact(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Add contact."""
        return await self._auth.post("Phonebook", "addContact", conf)

    async def async_add_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """All multiple contacts."""
        return await self._auth.post("Phonebook", "addContacts", conf)

    async def async_del_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Remove contact by UID."""
        return await self._auth.post("Phonebook", "removeContactByUniqueID", conf)

    async def async_del_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Remove contact by name."""
        return await self._auth.post("Phonebook", "removeContactByFormattedName", conf)

    async def async_del_contact(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Remove contact."""
        return await self._auth.post("Phonebook", "removeContact", conf)

    async def async_del_contacts(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Remove all contacts."""
        return await self._auth.post("Phonebook", "removeAllContacts", conf)

    async def async_get_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get contact by UID."""
        return await self._auth.post("Phonebook", "getContactByUniqueID", conf)

    async def async_get_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get contact by name."""
        return await self._auth.post("Phonebook", "getContactByFormattedName", conf)

    async def async_get_contact(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Get contact."""
        return await self._auth.post("Phonebook", "getContact", conf)

    async def async_get_contact_number(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get contact by number."""
        return await self._auth.post("Phonebook", "getContactByNumber", conf)

    async def async_get_contact_username(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Get contact by username."""
        return await self._auth.post("Phonebook", "getContactByUsername", conf)

    async def async_get_contacts(self) -> dict[str, Any]:
        """Get all contacts."""
        return await self._auth.post("Phonebook", "getAllContacts")

    async def async_get_count(self) -> dict[str, Any]:
        """Count contacts."""
        return await self._auth.post("Phonebook", "getNumberOfContacts")

    async def async_get_maxnumber(self) -> dict[str, Any]:
        """Max number of contacts."""
        return await self._auth.post("Phonebook", "getMaxNumberOfContacts")

    async def async_set_contact_uid(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set contact by uid."""
        return await self._auth.post("Phonebook", "modifyContactByUniqueID", conf)

    async def async_set_contact_name(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any]:
        """Set contact by name."""
        return await self._auth.post("Phonebook", "modifyContactByFormattedName", conf)

    async def async_set_contact(self, conf: dict[str, Any] | None) -> dict[str, Any]:
        """Set contact."""
        return await self._auth.post("Phonebook", "modifyContact", conf)
