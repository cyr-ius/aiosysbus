"""Tests connection."""
from __future__ import annotations

import asyncio
import logging
from unittest.mock import AsyncMock, patch

import aiohttp
import pytest

from aiosysbus import (
    AIOSysbus,
    AiosysbusException,
    HttpRequestFailed,
    RetrieveFailed,
    UnexpectedResponse,
)

_LOGGER = logging.getLogger(__name__)


def create_resp(status_code=200, resp_data=None):
    """Mock aiohttp session request."""
    mock = AsyncMock()
    mock.return_value.headers = {"Content-Type": "application/json"}
    mock.return_value.status = status_code
    mock.return_value.json = AsyncMock(return_value={"data": resp_data})
    mock.return_value.text = AsyncMock(return_value="It s no good")
    mock.return_value.read = AsyncMock(return_value="RAW Text")

    return mock


@pytest.mark.asyncio
async def test_challenge_error() -> None:
    """Test connect."""
    with pytest.raises(AiosysbusException, match="Open session failed"), patch(
        "aiohttp.ClientSession.request", side_effect=aiohttp.ClientError
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
    assert api.call is not None
    assert api.zwave is not None


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_connect_error(mock_post) -> None:
    """Test connect."""
    mock_post.side_effect = aiohttp.ClientError
    api = AIOSysbus("username", "password")
    with pytest.raises(
        AiosysbusException, match="Error occurred while communicating with Livebox"
    ), patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()):
        await api.async_connect()

    mock_post.side_effect = asyncio.TimeoutError
    api = AIOSysbus("username", "password")
    with pytest.raises(
        AiosysbusException, match="Timeout occurred while connecting to Livebox"
    ), patch("aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()):
        await api.async_connect()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_get_lan(mock_post) -> None:
    gdr = {"NumberOfReadings": 1, "InterfaceName": ["eth0"]}

    mock_post.return_value.json.return_value = {"result": {"lan": "1.2.3.4"}}

    api = AIOSysbus("username", "password")
    with patch(
        "aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()
    ), patch(
        "aiosysbus.auth.Auth.async_get_session_token",
        return_value=("123456789", "admin"),
    ):
        await api.async_connect()
        response = await api.lan.async_get_lan(gdr)
        print(response)

    assert mock_post.return_value.json.return_value.get("result") == response


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_500(mock_post) -> None:
    """Test connect."""
    data = {"data": {"error": "Server unavailable"}}

    mock_post.return_value.status = 500
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with pytest.raises(HttpRequestFailed) as error, patch(
        "aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()
    ), patch(
        "aiosysbus.auth.Auth.async_get_session_token",
        return_value=("123456789", "admin"),
    ):
        await api.async_connect()
        await api.lan.async_get_lan()

    assert error.value.args[0] == data


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_contenttype(mock_post) -> None:
    """Test connect."""
    mock_post.return_value.headers = {"Content-Type": "plain/text"}
    api = AIOSysbus("username", "password")
    with pytest.raises(UnexpectedResponse) as error, patch(
        "aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()
    ), patch(
        "aiosysbus.auth.Auth.async_get_session_token",
        return_value=("123456789", "admin"),
    ):
        await api.async_connect()
        await api.lan.async_get_lan()

    assert error.value.args[0] == "Unexpected response from the Livebox API"
    assert error.value.args[1] == {
        "Content-Type": "plain/text",
        "response": "It s no good",
    }


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_error_text_500(mock_post) -> None:
    """Test connect."""
    data = {"data": {"error": "Server unavailable"}}

    mock_post.return_value.status = 500
    mock_post.return_value.headers = {"Content-Type": "plain/text"}
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with pytest.raises(HttpRequestFailed) as error, patch(
        "aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()
    ), patch(
        "aiosysbus.auth.Auth.async_get_session_token",
        return_value=("123456789", "admin"),
    ):
        await api.async_connect()
        await api.lan.async_get_lan()

    assert error.value.args[0] == "RAW Text"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request", new_callable=create_resp)
async def test_retry_error(mock_post) -> None:
    """Test connect."""
    data = {"result": {"errors": "Server unavailable"}}
    mock_post.return_value.json.return_value = data
    api = AIOSysbus("username", "password")
    with pytest.raises(RetrieveFailed) as error, patch(
        "aiosysbus.auth.Auth._async_get_challenge", return_value=AsyncMock()
    ), patch(
        "aiosysbus.auth.Auth.async_get_session_token",
        return_value=("123456789", "admin"),
    ):
        await api.async_connect()
        await api.lan.async_get_lan()

    assert error.value.args[0] == "Server unavailable"
