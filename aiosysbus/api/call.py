"""DECT, VoiceService and Phone book."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class VoiceService:
    """Voice service class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_list_handsets(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get handsets list."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "listHandsets", conf
        )

    async def async_get_list_trunks(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get trunks list."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "listTrunks", conf
        )

    async def async_get_calllist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get calls.list."""
        return await self._auth.post(
            "VoiceService.VoiceApplication", "getCallList", conf
        )

    async def async_clear_calllist(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Clear Call list.

        Argument:
        - callId (str) optional
        """
        return await self._auth.post(
            "VoiceService.VoiceApplication", "clearCallList", conf
        )

    async def async_ring(self, conf: dict[str, Any] | None = None) -> dict[str, Any]:
        """Ring."""
        return await self._auth.post("VoiceService.VoiceApplication", "ring", conf)


class Dect:
    """DECT class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_dect_pairing(self) -> str:
        """Get pairing status."""
        return await self._auth.post("DECT", "getPairingStatus")

    async def async_start_dect_pairing(self) -> None:
        """Start pairing DECT."""
        return await self._auth.post("DECT", "startPairing")

    async def async_stop_dect_pairing(self) -> None:
        """Stop pairing DECT."""
        return await self._auth.post("DECT", "stopPairing")

    async def async_reset_dect_pairing(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Reset pairing DECT.

        Argument:
        - reboot (bool) optional
        """
        return await self._auth.post("DECT", "reset", conf)

    async def async_get_RFPI(self) -> str:
        """Get RFPI."""
        return await self._auth.post("DECT", "getRFPI")

    async def async_get_dect_standardversion(self) -> str:
        """Get standard version."""
        return await self._auth.post("DECT", "getStandardVersion")

    async def async_get_dect_pin(self) -> str:
        """Get Pin code for DECT."""
        return await self._auth.post("DECT", "getPIN")

    async def async_set_dect_pin(self, conf: dict[str, Any]) -> None:
        """Set Pin code for DECT.

        Argument:
        - pin (str)
        """
        return await self._auth.post("DECT", "setPIN", conf)

    async def async_get_dect_version(self) -> str:
        """Get DECT version."""
        return await self._auth.post("DECT", "getVersion")

    async def async_get_dect_name(self) -> str:
        """Get DECT name."""
        return await self._auth.post("DECT", "getName")

    async def async_get_dect_radio_state(self) -> bool:
        """Get Radio state name."""
        return await self._auth.post("DECT", "getRadioState")

    async def async_set_dect_radio_state(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Set Radio state name.

        Argument:
        - state (bool) optional
        """
        return await self._auth.post("DECT", "setRadioState", conf)

    async def async_get_dect_RSSI(self, conf: dict[str, Any] | None = None) -> int:
        """Set Radio state name.

        Argument:
        - name (str) optional
        - synchronous (bool) optional
        """
        return await self._auth.post("DECT", "getRSSI", conf)

    async def async_set_handset_debug_mode(
        self, conf: dict[str, Any] | None = None
    ) -> None:
        """Set Radio state name.

        Argument:
        - enable (bool) optional
        """
        return await self._auth.post("DECT", "setHandsetDebugMode", conf)

    # DECT.Repeater

    async def async_get_dect_repeaters(self) -> None:
        """Get DECT name."""
        return await self._auth.post("DECT.Repeater", "getRepeaters")

    async def async_delete_dect_repeaters(self) -> None:
        """Get Radio state name."""
        return await self._auth.post("DECT.Repeater", "removeAllRepeaters")

    # DECT.Repeater.Device

    async def async_deregister_dect(self) -> None:
        """Deregister."""
        return await self._auth.post("DECT.Repeater.Device", "deregister")


class Phonebook:
    """contacts book."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_contact_uuid(self, conf: dict[str, Any]) -> str:
        """Add contact and generate UUID.

        Argument:
        - contact (contact_t)
        """
        return await self._auth.post("Phonebook", "addContactAndGenUUID", conf)

    async def async_add_contact(self, conf: dict[str, Any]) -> bool:
        """Add contact.

        Argument:
        - contact (contact_t)
        """
        return await self._auth.post("Phonebook", "addContact", conf)

    async def async_add_contacts(self, conf: dict[str, Any]) -> bool:
        """All multiple contacts.

        Arguments:
        - contacts (list)
        - result (list) optional
        """
        return await self._auth.post("Phonebook", "addContacts", conf)

    async def async_del_contact_uid(self, conf: dict[str, Any]) -> bool:
        """Remove contact by UID.

        Argument:
        - uniqueID (str)
        """
        return await self._auth.post("Phonebook", "removeContactByUniqueID", conf)

    async def async_del_contact_vref(self, conf: dict[str, Any]) -> bool:
        """Remove contact by vref.

        Argument:
        - vref (str)
        """
        return await self._auth.post("Phonebook", "removeContactByVref", conf)

    async def async_del_contact_name(self, conf: dict[str, Any]) -> bool:
        """Remove contact by name.

        Argument:
        - formattedName (str)
        """
        return await self._auth.post("Phonebook", "removeContactByFormattedName", conf)

    async def async_del_contact(self, conf: dict[str, Any]) -> bool:
        """Remove contact.

        Argument:
        - formattedName (str)
        """
        return await self._auth.post("Phonebook", "removeContact", conf)

    async def async_del_contacts(self) -> bool:
        """Remove all contacts."""
        return await self._auth.post("Phonebook", "removeAllContacts")

    async def async_get_contact_uid(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact by UID.

        Argument:
        - uniqueID (str)
        """
        return await self._auth.post("Phonebook", "getContactByUniqueID", conf)

    async def async_get_contact_name(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact by name.

        Argument:
        - formattedName (str)
        """
        return await self._auth.post("Phonebook", "getContactByFormattedName", conf)

    async def async_get_contact_vref(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact by vref.

        Argument:
        - vref (str)
        """
        return await self._auth.post("Phonebook", "getContactByVref", conf)

    async def async_get_contact(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact.

        Argument:
        - formattedName (str)
        """
        return await self._auth.post("Phonebook", "getContact", conf)

    async def async_get_contact_number(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact by number.

        Argument:
        - number (str)
        """
        return await self._auth.post("Phonebook", "getContactByNumber", conf)

    async def async_get_contact_username(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Get contact by username.

        Argument:
        - username (str)
        """
        return await self._auth.post("Phonebook", "getContactByUsername", conf)

    async def async_get_contacts(self) -> list[dict[str, Any]]:
        """Get all contacts."""
        return await self._auth.post("Phonebook", "getAllContacts")

    async def async_get_count(self) -> int:
        """Count contacts."""
        return await self._auth.post("Phonebook", "getNumberOfContacts")

    async def async_get_available_number_contacts(self) -> int:
        """Get available number of contacts."""
        return await self._auth.post("Phonebook", "getAvailableNumberOfContacts")

    async def async_get_maxnumber(self) -> int:
        """Max number of contacts."""
        return await self._auth.post("Phonebook", "getMaxNumberOfContacts")

    async def async_is_contact_uid(self, conf: dict[str, Any]) -> bool:
        """Check contact exists with UniqueID.

        Argument:
        - uniqueID (str)
        """
        return await self._auth.post(
            "Phonebook", "checkContactExistsWithUniqueID", conf
        )

    async def async_set_contact_uid(self, conf: dict[str, Any]) -> bool:
        """Set contact by uid.

        Arguments:
        - uniqueID (str)
        - contact (contact_t)
        """
        return await self._auth.post("Phonebook", "modifyContactByUniqueID", conf)

    async def async_set_contact_name(self, conf: dict[str, Any]) -> bool:
        """Set contact by name.

        Arguments:
        - formattedName (str)
        - contact (contact_t)
        """
        return await self._auth.post("Phonebook", "modifyContactByFormattedName", conf)

    async def async_set_contact(self, conf: dict[str, Any]) -> bool:
        """Set contact.

        Arguments:
        - formattedName (str)
        - contact (contact_t)
        """
        return await self._auth.post("Phonebook", "modifyContact", conf)

    async def async_disable_cardav(self) -> bool:
        """Disable carddav and cleanup entries."""
        return await self._auth.post("Phonebook", "disableCardDavAndCleanupEntries")
