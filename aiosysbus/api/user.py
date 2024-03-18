"""Users."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class UserManagement:
    """User Management class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_user(self, conf: dict[str, Any] | None = None) -> bool:
        """Add user.

        Arguments:
        - name (str) optional
        - password (str) optional
        - groups (list) optional
        - enable (bool) optional
        - usertype (str) optional
        - salt (str) optional
        - uid (int) optional
        - linux_user (str) optional
        - friendlyname (str) optional
        """
        return await self._auth.post("UserManagement", "addUser", conf)

    async def async_set_user(self, conf: dict[str, Any] | None = None) -> bool:
        """Add user.

        Arguments:
        - name (str) optional
        - password (str) optional
        - groups (list) optional
        - enable (bool) optional
        - usertype (str) optional
        - friendlyname (str) optional
        """
        return await self._auth.post("UserManagement", "changeUser", conf)

    async def async_set_password(self, conf: dict[str, Any] | None = None) -> bool:
        """Change password for a user.

        Arguments:
        - name (str) optional
        - password (str) optional
        """
        return await self._auth.post("UserManagement", "changePassword", conf)

    async def async_set_passwordsec(self, conf: dict[str, Any] | None = None) -> bool:
        """Change password for a user.

        Arguments:
        - name (str) optional
        - password (str) optional
        - old_password (str) optional
        """
        return await self._auth.post("UserManagement", "changePasswordSec", conf)

    async def async_delete_user(self, conf: dict[str, Any] | None = None) -> bool:
        """Del user.

        Arguments:
        - name (str) optional
        """
        return await self._auth.post("UserManagement", "removeUser", conf)

    async def async_delete_users(self, conf: dict[str, Any] | None = None) -> bool:
        """Del users.

        Arguments:
        - name (str) optional
        - type (str) optional
        """
        return await self._auth.post("UserManagement", "removeUsers", conf)

    async def async_add_group(self, conf: dict[str, Any] | None = None) -> bool:
        """Add groups.

        Arguments:
        - name (str) optional
        - enable (bool) optional
        - linux_group (bool) optional
        """
        return await self._auth.post("UserManagement", "addGroup", conf)

    async def async_set_group(self, conf: dict[str, Any] | None = None) -> bool:
        """Set group.

        Arguments:
        - name (str) optional
        - enable (bool) optional
        """
        return await self._auth.post("UserManagement", "changeGroup", conf)

    async def async_delete_group(self, conf: dict[str, Any] | None = None) -> bool:
        """Delete group.

        Arguments:
        - name (str) optional
        """
        return await self._auth.post("UserManagement", "removeGroup", conf)

    async def async_get_users(self) -> list[Any]:
        """Get users."""
        return await self._auth.post("UserManagement", "getUsers")

    async def async_get_groups(self) -> list[Any]:
        """Get groups."""
        return await self._auth.post("UserManagement", "getGroups")

    async def async_get_group(self, conf: dict[str, Any] | None = None) -> list[Any]:
        """Get group.

        Arguments:
        - name (str) optional
        """
        return await self._auth.post("UserManagement", "getGroup", conf)

    async def async_get_users_groups(self, conf: dict[str, Any] | None = None) -> bool:
        """Get users and groups.

        Arguments:
        - users (list) optional
        - groups (list) optional
        """
        return await self._auth.post("UserManagement", "getUsersAndGroups", conf)

    async def async_get_user(self, conf: dict[str, Any]) -> list[Any]:
        """Get user.

        Arguments:
        - name (str)
        """
        return await self._auth.post("UserManagement", "getUser", conf)

    async def async_add_user_groups(self, conf: dict[str, Any] | None = None) -> bool:
        """Get users and groups.

        Arguments:
        - name (list) optional
        - groups (list) optional
        """
        return await self._auth.post("UserManagement", "addUserToGroups", conf)

    async def async_remove_user_groups(
        self, conf: dict[str, Any] | None = None
    ) -> bool:
        """Remove user from groups.

        Arguments:
        - name (list) optional
        - groups (list) optional
        """
        return await self._auth.post("UserManagement", "removeUserFromGroups", conf)

    async def async_authenticate(self, conf: dict[str, Any]) -> bool:
        """Authentication.

        Arguments:
        - name (str)
        - password (str)
        - groupName (str) optional
        """
        return await self._auth.post("UserManagement", "authenticate", conf)
