"""Users."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class UserManagement:
    """User Management class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    async def async_add_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Add user."""
        return await self._access.post("UserManagement", "addUser", conf)

    async def async_set_user_password(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Change password for a user."""
        return await self._access.post("UserManagement", "changePassword", conf)

    async def async_del_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Del user."""
        return await self._access.post("UserManagement", "removeUsers", conf)

    async def async_get_users(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get users."""
        return await self._access.post("UserManagement", "getUsers", conf)

    async def async_get_groups(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get groups."""
        return await self._access.post("UserManagement", "getGroups", conf)

    async def async_authenticate(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Authentication."""
        return await self._access.post("UserManagement", "authenticate", conf)

    async def async_add_authenticationlog(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Add authentication log."""
        return await self._access.post("UserManagement", "addAuthenticationLog", conf)

    async def async_get_userlog(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get user log."""
        return await self._access.post("UserManagement", "getUserLog", conf)

    async def async_get_user_lastlogininfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Last login info."""
        return await self._access.post("UserManagement", "getLastLoginInfo", conf)

    async def async_get_group(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get group."""
        return await self._access.post("UserManagement.Group", "get", conf)

    async def async_get_group_info(
        self, conf: dict[str, Any] = {"group": None}
    ) -> dict[str, Any] | None:
        """Get information for a group."""
        group = conf.pop("group")
        return await self._access.post(f"UserManagement.Group.{group}", "get", conf)

    async def async_get_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get user."""
        return await self._access.post("UserManagement.User", "get", conf)

    async def async_get_user_info(
        self, conf: dict[str, Any] = {"user": None}
    ) -> dict[str, Any] | None:
        """Get user information for user."""
        user = conf.pop("user")
        return await self._access.post(f"UserManagement.User.{user}", "get", conf)

    async def async_get_loginattempt(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Login attempts."""
        return await self._access.post("UserManagement.LoginAttempt", "get", conf)

    async def async_get_loginattempt_info(
        self, conf: dict[str, Any] = {"id": None}
    ) -> dict[str, Any] | None:
        """Get login attempt for id."""
        userid = conf.pop("id")
        return await self._access.post(f"UserManagement.LoginAttempt.{userid}", "get", conf)

    async def async_get_logincounters(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get login counters."""
        return await self._access.post("UserManagement.LoginCounters", "get", conf)
