"""Users."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth


class UserManagement:
    """User Management class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_add_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Add user."""
        return await self._auth.post("UserManagement", "addUser", conf)

    async def async_set_user_password(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Change password for a user."""
        return await self._auth.post("UserManagement", "changePassword", conf)

    async def async_del_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Del user."""
        return await self._auth.post("UserManagement", "removeUsers", conf)

    async def async_get_users(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get users."""
        return await self._auth.post("UserManagement", "getUsers", conf)

    async def async_get_groups(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get groups."""
        return await self._auth.post("UserManagement", "getGroups", conf)

    async def async_authenticate(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Authentication."""
        return await self._auth.post("UserManagement", "authenticate", conf)

    async def async_add_authenticationlog(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Add authentication log."""
        return await self._auth.post("UserManagement", "addAuthenticationLog", conf)

    async def async_get_userlog(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get user log."""
        return await self._auth.post("UserManagement", "getUserLog", conf)

    async def async_get_user_lastlogininfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Last login info."""
        return await self._auth.post("UserManagement", "getLastLoginInfo", conf)

    async def async_get_group(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get group."""
        return await self._auth.post("UserManagement.Group", "get", conf)

    async def async_get_group_info(
        self, conf: dict[str, Any] = {"group": None}
    ) -> dict[str, Any]:
        """Get information for a group."""
        group = conf.pop("group")
        return await self._auth.post(f"UserManagement.Group.{group}", "get", conf)

    async def async_get_user(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get user."""
        return await self._auth.post("UserManagement.User", "get", conf)

    async def async_get_user_info(
        self, conf: dict[str, Any] = {"user": None}
    ) -> dict[str, Any]:
        """Get user information for user."""
        user = conf.pop("user")
        return await self._auth.post(f"UserManagement.User.{user}", "get", conf)

    async def async_get_loginattempt(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get Login attempts."""
        return await self._auth.post("UserManagement.LoginAttempt", "get", conf)

    async def async_get_loginattempt_info(
        self, conf: dict[str, Any] = {"id": None}
    ) -> dict[str, Any]:
        """Get login attempt for id."""
        userid = conf.pop("id")
        return await self._auth.post(
            f"UserManagement.LoginAttempt.{userid}", "get", conf
        )

    async def async_get_logincounters(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get login counters."""
        return await self._auth.post("UserManagement.LoginCounters", "get", conf)
