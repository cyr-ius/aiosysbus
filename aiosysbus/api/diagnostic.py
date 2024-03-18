"""Diagnostics and data statistics."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class AutoDiag:
    """AutoDiag class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_run_diags(self, conf: dict[str, Any]) -> bool:
        """Run diagnostic.

        Arguments:
        - id (str)
        - usr (bool) optional
        """
        return await self._auth.post("AutoDiag", "executeDiagnostics", conf)

    async def async_run_diags_trigger(self, conf: dict[str, Any]) -> bool:
        """Execute trigger diagnostic.

        Arguments:
        - event (str)
        """
        return await self._auth.post("AutoDiag", "executeTrigger", conf)

    async def async_remove_diags(self, conf: dict[str, Any]) -> bool:
        """Cancel diagnostic.

        Arguments:
        - id (str)
        """
        return await self._auth.post("AutoDiag", "cancelDiagnostics", conf)

    async def async_get_diags_states(self) -> None:
        """Get diagnostic states."""
        return await self._auth.post("AutoDiag", "getDiagnosticsState")

    async def async_get_diags_datamodel(self) -> None:
        """Get datamodel white list."""
        return await self._auth.post("AutoDiag", "getDatamodelWhiteList")

    async def async_get_diags_functions(self) -> None:
        """Get function white list."""
        return await self._auth.post("AutoDiag", "getFunctionWhiteList")

    async def async_get_diags_list(self) -> None:
        """Get diagnostic list."""
        return await self._auth.post("AutoDiag", "getDiagnosticsList")

    async def async_get_diags_listdiag(self) -> list[dict[str, Any]]:
        """List diagnostics."""
        return await self._auth.post("AutoDiag", "listDiagnostics")

    async def async_get_diags_context(self) -> list[dict[str, Any]]:
        """Get context."""
        return await self._auth.post("AutoDiag", "getContext")

    async def async_clear_diags_context(self) -> bool:
        """Get context."""
        return await self._auth.post("AutoDiag", "clearContext")

    async def async_set_diags_userinput(self, conf: dict[str, Any]) -> dict[str, Any]:
        """Set  user input.

        Argument:
        - input (str)
        """
        return await self._auth.post("AutoDiag", "setUserInput", conf)


class TopologyDiagnostics:
    """Topology diagnostics class."""

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_get_topodiags(self) -> dict[str, Any]:
        """Get topology diagnostics."""
        return await self._auth.post("TopologyDiagnostics", "get")

    async def async_set_topodiags(self, conf: dict[str, Any]) -> bool:
        """Set topology diagnostics.

        Argument:
        - data (dict)
        """
        return await self._auth.post("TopologyDiagnostics", "set", conf)

    async def async_set_topodiags_build(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Build topology diagnostics.

        Arguments:
        - Timeout (int) optional
        - LLTDIcon (bool) optional
        - SendXmlFile (bool) optional
        """
        return await self._auth.post("TopologyDiagnostics", "buildTopology", conf)

    async def async_upload_topodiags(self) -> bool:
        """Upload topology diagnostics."""
        return await self._auth.post("TopologyDiagnostics", "uploadTopology")

    async def async_enable_topodiags(self, conf: dict[str, Any] | None = None) -> bool:
        """Enable topology diagnostics.

        Argument:
        - enable (bool) optional
        """
        return await self._auth.post(
            "TopologyDiagnostics", "enableAutomaticUpload", conf
        )

    async def async_get_topodiags_isautoupload(self) -> bool:
        """Is Automatic Upload enabled of topology diagnostics."""
        return await self._auth.post("TopologyDiagnostics", "isAutomaticUploadEnabled")

    async def async_set_topodiags_customerauthor(self, conf: dict[str, Any]) -> bool:
        """Set customer authorization of topology diagnostics.

        Argument:
        - enable (bool)
        """
        return await self._auth.post(
            "TopologyDiagnostics", "setCustomerAuthorization", conf
        )

    async def async_export_topodiags(self) -> None:
        """Export topology diagnostics."""
        return await self._auth.post("TopologyDiagnostics", "export")

    async def async_import_topodiags(self) -> None:
        """Import topology diagnostics."""
        return await self._auth.post("TopologyDiagnostics", "import")

    # TopologyDiagnostics.Results

    async def async_get_topodiags_result(self, conf: dict[str, Any]) -> bool:
        """Set result of topology diagnostics.

        Argument:
        - state (str)
        """
        return await self._auth.post("TopologyDiagnostics.Results", "setState", conf)
