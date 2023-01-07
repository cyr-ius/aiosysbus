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

    def add_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Add user."""
        return self._access.post("UserManagement", "addUser", conf)

    def set_user_password(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Change password for a user."""
        return self._access.post("UserManagement", "changePassword", conf)

    def del_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Del user."""
        return self._access.post("UserManagement", "removeUsers", conf)

    def get_users(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get users."""
        return self._access.post("UserManagement", "getUsers", conf)

    def get_groups(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get groups."""
        return self._access.post("UserManagement", "getGroups", conf)

    def authenticate(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Authentification."""
        return self._access.post("UserManagement", "authenticate", conf)

    def add_authenticationlog(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Add authentification log."""
        return self._access.post("UserManagement", "addAuthenticationLog", conf)

    def get_userlog(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get user log."""
        return self._access.post("UserManagement", "getUserLog", conf)

    def get_user_lastlogininfo(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Last login info."""
        return self._access.post("UserManagement", "getLastLoginInfo", conf)

    def get_group(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get group."""
        return self._access.post("UserManagement.Group", "get", conf)

    def get_group_info(
        self, conf: dict[str, Any] = {"group": None}
    ) -> dict[str, Any] | None:
        """Get informations for a group."""
        group = conf.pop("group")
        return self._access.post(f"UserManagement.Group.{group}", "get", conf)

    def get_user(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get user."""
        return self._access.post("UserManagement.User", "get", conf)

    def get_user_info(
        self, conf: dict[str, Any] = {"user": None}
    ) -> dict[str, Any] | None:
        """Get user information for user."""
        user = conf.pop("user")
        return self._access.post(f"UserManagement.User.{user}", "get", conf)

    def get_loginattempt(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get Login attempts."""
        return self._access.post("UserManagement.LoginAttempt", "get", conf)

    def get_loginattempt_info(
        self, conf: dict[str, Any] = {"id": None}
    ) -> dict[str, Any] | None:
        """Get login attempt for id."""
        userid = conf.pop("id")
        return self._access.post(f"UserManagement.LoginAttempt.{userid}", "get", conf)

    def get_logincounters(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get login counters."""
        return self._access.post("UserManagement.LoginCounters", "get", conf)
