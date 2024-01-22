"""Exceptions for livebox."""


class AiosysbusException(Exception):
    """General exception."""


class AuthenticationFailed(AiosysbusException):
    """Authentication error."""


class TimeoutExceededError(AiosysbusException):
    """Timeout exceeded."""


class HttpRequestFailed(AiosysbusException):
    """Requests error."""


class InsufficientPermissionsError(HttpRequestFailed):
    """Insufficient Permissions."""


class RetrieveFailed(HttpRequestFailed):
    """Retrieve exception."""


class UnexpectedResponse(HttpRequestFailed):
    """Unexpected response."""
