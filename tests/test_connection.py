"""Tests connection."""

from __future__ import annotations

import asyncio
import logging
from unittest.mock import AsyncMock, patch

import aiohttp
from multidict import CIMultiDict
import pytest

from aiosysbus import (
    AIOSysbus,
    AiosysbusException,
    HttpRequestFailed,
    RetrieveFailed,
    TimeoutExceededError,
    UnexpectedResponse,
)

_LOGGER = logging.getLogger(__name__)


def create_resp(status_code=200, resp_data=None):
    """Mock aiohttp session request."""
    mock = AsyncMock()
    mock.return_value.headers = CIMultiDict(
        {
            ("Content-Type", "application/json"),
            (
                "Set-Cookie",
                "e2c29097/sessid=; expires=Thu, 01-Jan-1970 00:00:01 GMT; path=/; SameSite=Strict",
            ),
        }
    )
    mock.return_value.status = status_code
    mock.return_value.json = AsyncMock(return_value={"data": resp_data})
    mock.return_value.text = AsyncMock(return_value="It s no good")
    mock.return_value.read = AsyncMock(return_value="RAW Text")

    return mock


@pytest.mark.asyncio
async def test_challenge_error() -> None:
    """Test connect."""
    with (
        pytest.raises(
            AiosysbusException, match="An error occurred while retrieving the challenge"
        ),
        patch("aiohttp.ClientSession.request", side_effect=aiohttp.ClientError),
    ):
        api = AIOSysbus("username", "password")
        await api.async_connect()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_connect(mock_post) -> None:
    """Test connect."""
    mock_post.return_value.json.return_value = {
        "data": {"contextID": "123456789", "groups": "admin"}
    }
    api = AIOSysbus("username", "password")
    with patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()):
        await api.async_connect()

    assert len(mock_post.mock_calls) == 2
    assert api.voiceservice is not None
    assert api.nmc is not None


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_connect_error(mock_post) -> None:
    """Test connect."""
    mock_post.side_effect = aiohttp.ClientError
    api = AIOSysbus("username", "password")
    with (
        pytest.raises(
            AiosysbusException, match="Error occurred while communicating with Livebox"
        ),
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
    ):
        await api.async_connect()

    mock_post.side_effect = asyncio.TimeoutError
    api = AIOSysbus("username", "password")
    with (
        pytest.raises(
            AiosysbusException, match="Timeout occurred while connecting to Livebox"
        ),
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
    ):
        await api.async_connect()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_get_lan(mock_post) -> None:
    """Test connect."""
    gdr = {"NumberOfReadings": 1, "InterfaceName": ["eth0"]}

    mock_post.return_value.json.return_value = {"result": {"lan": "1.2.3.4"}}

    api = AIOSysbus("username", "password")
    with (
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        response = await api.nmc.async_get_lan_ip(gdr)

    assert mock_post.return_value.json.return_value.get("result") == response


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_get_optical(mock_post) -> None:
    """Test get optical information."""
    api = AIOSysbus("username", "password")
    with (
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        await api.sgcomci.async_get_optical()

    assert mock_post.call_count == 1


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_get_api_without_connect(mock_post) -> None:
    """Test get lan ip without connect."""
    gdr = {"NumberOfReadings": 1, "InterfaceName": ["eth0"]}

    mock_post.return_value.json.return_value = {"result": {"lan": "1.2.3.4"}}

    api = AIOSysbus("username", "password")
    with (
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        response = await api.nmc.async_get_lan_ip(gdr)

    assert mock_post.return_value.json.return_value.get("result") == response
    assert api._auth.session_token == "123456789"
    assert api._auth.session_permissions == "admin"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_500(mock_post) -> None:
    """Test error 500."""
    data = {"data": {"error": "Server unavailable"}}

    mock_post.return_value.status = 500
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with (
        pytest.raises(HttpRequestFailed) as error,
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        await api.nmc.async_get_lan_ip()

    assert error.value.args[0] == data


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_contenttype(mock_post) -> None:
    """Test error content type."""
    mock_post.return_value.headers = CIMultiDict(
        {("Content-Type", "plain/text"), ("Set-Cookie", "e2c29097/sessid=;")}
    )

    api = AIOSysbus("username", "password")
    with (
        pytest.raises(UnexpectedResponse) as error,
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        await api.storageservice.async_get_physical_mediums()

    assert (
        error.value.args[0]
        == "Unexpected response, content-type incorrect (plain/text)"
    )


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_text_500(mock_post) -> None:
    """Test connect."""
    data = {"data": {"error": "Server unavailable"}}

    mock_post.return_value.status = 500
    mock_post.return_value.headers = CIMultiDict(
        {("Content-Type", "plain/text"), ("Set-Cookie", "e2c29097/sessid=;")}
    )
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with (
        pytest.raises(HttpRequestFailed) as error,
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        await api.speedtest.async_get_wan_results()

    assert error.value.args[0] == "RAW Text"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_retry_error(mock_post) -> None:
    """Test retry error."""
    data = {"result": {"errors": "Server unavailable"}}
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with (
        pytest.raises(RetrieveFailed) as error,
        patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()),
        patch(
            "aiosysbus.auth.Auth.async_get_session_token",
            return_value=("123456789", "admin"),
        ),
    ):
        await api.async_connect()
        await api.topologydiagnostics.async_get_topodiags()

    assert error.value.args[0] == "Server unavailable"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_connect_keeps_session(mock_post) -> None:
    """Test connect keeps the session for the next calls."""
    mock_post.return_value.json.return_value = {
        "data": {"contextID": "123456789", "groups": "admin"}
    }
    api = AIOSysbus("username", "password")
    with patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()):
        await api.async_connect()

    assert api._auth.session_token == "123456789"
    assert api._auth.session_permissions == "admin"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_logout(mock_post) -> None:
    """Test logout releases the context with the web interface request."""
    api = AIOSysbus("username", "password", verify_tls=False)
    api._auth.session_token = "123456789"
    api._auth.session_permissions = "admin"
    api._auth._cookies = {"e2c29097/sessid": "abc", "sah/contextId": "def"}
    mock_post.return_value.json.return_value = {"status": 0}

    assert await api.async_logout() is True

    mock_post.assert_called_once()
    kwargs = mock_post.call_args.kwargs
    assert kwargs["method"] == "post"
    assert kwargs["url"] == api._auth.base_url
    assert kwargs["headers"] == {
        "Content-Type": "application/x-sah-ws-1-call+json",
        "Authorization": "X-Sah-Logout 123456789",
        "Cookie": "e2c29097/sessid=abc;sah/contextId=def",
    }
    assert kwargs["json"] == {
        "service": "sah.Device.Information",
        "method": "releaseContext",
        "parameters": {"applicationName": "so_sdkut"},
    }
    assert kwargs["verify_ssl"] is False
    assert api._auth.session_token is None
    assert api._auth.session_permissions is None
    assert api._auth._cookies == {}


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_logout_without_session(mock_post) -> None:
    """Test logout does nothing without a session."""
    api = AIOSysbus("username", "password")

    assert await api.async_logout() is False
    mock_post.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("status", "resp_json"),
    [
        (200, {"result": {"errors": [{"error": 196618}]}}),
        (200, None),
        (401, {"status": 0}),
    ],
)
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_logout_refused(mock_post, status, resp_json) -> None:
    """Test logout not confirmed by the livebox."""
    api = AIOSysbus("username", "password")
    api._auth.session_token = "123456789"
    mock_post.return_value.status = status
    mock_post.return_value.json.return_value = resp_json

    assert await api.async_logout() is False
    assert api._auth.session_token is None


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_logout_invalid_json(mock_post) -> None:
    """Test logout with a response which is not json."""
    api = AIOSysbus("username", "password")
    api._auth.session_token = "123456789"
    mock_post.return_value.json.side_effect = ValueError

    assert await api.async_logout() is False
    assert api._auth.session_token is None


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("side_effect", "exception"),
    [
        (aiohttp.ClientError, HttpRequestFailed),
        (asyncio.TimeoutError, TimeoutExceededError),
    ],
)
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_logout_error(mock_post, side_effect, exception) -> None:
    """Test logout when the livebox is unreachable."""
    api = AIOSysbus("username", "password")
    api._auth.session_token = "123456789"
    mock_post.side_effect = side_effect

    with pytest.raises(exception):
        await api.async_logout()

    assert api._auth.session_token is None
