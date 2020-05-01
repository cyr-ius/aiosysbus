"""Exceptions for livebox."""


class LiveboxException(Exception):
    """General exception."""


class NotOpenError(LiveboxException):
    """Not open url."""


class AuthorizationError(LiveboxException):
    """Authentification error."""


class HttpRequestError(LiveboxException):
    """Requests error."""


class InsufficientPermissionsError(HttpRequestError):
    """Insufficient Permissions."""


class TimeoutExceededError(LiveboxException):
    """Timeout exceeded."""
