"""Diagnostics and data statistics."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..access import Access


class Diagnostic:  # pylint: disable=[too-many-public-methods]
    """System class."""

    def __init__(self, access: Access) -> None:
        """Init."""
        self._access = access

    # ############ DATA STATS #############

    async def async_get_stats_account(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return await self._access.post("DataStatistics.account", "getStats", conf)

    async def async_get_stats_media(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time left for remote access."""
        return await self._access.post("DataStatistics.mediahub", "getStats", conf)

    async def async_get_stats_storage(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reset timer for remote access."""
        return await self._access.post("DataStatistics.storage", "getStats", conf)

    # ############ AUTO DIAG #############

    async def async_run_diags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return await self._access.post("AutoDiag", "executeDiagnostics", conf)

    async def async_run_diags_trigger(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Get time left for remote access."""
        return await self._access.post("AutoDiag", "executeTrigger", conf)

    async def async_remove_diags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Reset timer for remote access."""
        return await self._access.post("AutoDiag", "cancelDiagnostics", conf)

    async def async_get_diags_states(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return await self._access.post("AutoDiag", "getDiagnosticsState", conf)

    async def async_get_diags_list(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get time left for remote access."""
        return await self._access.post("AutoDiag", "getDiagnosticsList", conf)

    async def async_get_diags_listdiag(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Reset timer for remote access."""
        return await self._access.post("AutoDiag", "listDiagnostics", conf)

    async def async_set_diags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set  enable remote access."""
        return await self._access.post("AutoDiag", "setUserInput", conf)

    # ############ TOPOLOGY DIAG #############

    async def async_get_topodiags(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Get topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "get", conf)

    async def async_set_topodiags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "set", conf)

    async def async_set_topodiags_build(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Build topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "buildTopology", conf)

    async def async_upload_topodiags(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Upload topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "uploadTopology", conf)

    async def async_enable_topodiags(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Enable topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "enableAutomaticUpload", conf)

    async def async_get_topodiags_isautoupload(
        self, conf: dict[str, Any] | None = None
    ) -> dict[str, Any] | None:
        """Is Automatic Upload enabled of topology diagnostics."""
        return await self._access.post(
            "TopologyDiagnostics", "isAutomaticUploadEnabled", conf
        )

    async def async_set_topodiags_customerauthor(
        self, conf: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        """Set customer authorization of topology diagnostics."""
        return await self._access.post(
            "TopologyDiagnostics", "setCustomerAuthorization", conf
        )

    async def async_export_topodiags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Export topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "export", conf)

    async def async_import_topodiags(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Import topology diagnostics."""
        return await self._access.post("TopologyDiagnostics", "import", conf)

    async def async_get_topodiags_result(
        self, conf: dict[str, Any] = {"result": None}
    ) -> dict[str, Any] | None:
        """Get result of topology diagnostics."""
        result = conf.pop("result")
        return await self._access.post(
            f"TopologyDiagnostics.Results.Result.{result}", "get", conf
        )

    # ############ PROCESS MONITOR #############

    async def async_get_process(self, conf: dict[str, Any] | None = None) -> dict[str, Any] | None:
        """Get process monitor."""
        return await self._access.post("ProcessMonitor", "get", conf)

    async def async_set_process(self, conf: dict[str, Any] | None) -> dict[str, Any] | None:
        """Set process monitor."""
        return await self._access.post("ProcessMonitor", "set", conf)

    async def async_get_process_component(
        self, conf: dict[str, Any] = {"component": None}
    ) -> dict[str, Any] | None:
        """Get process monitor component."""
        component = conf.pop("component")
        return await self._access.post(f"ProcessMonitor.Test.{component}", "get", conf)

    async def async_set_process_component(
        self, conf: dict[str, Any] = {"component": None}
    ) -> dict[str, Any] | None:
        """Set process monitor component."""
        component = conf.pop("component")
        return await self._access.post(f"ProcessMonitor.Test.{component}", "set", conf)

    async def async_reset_process_component(
        self, conf: dict[str, Any] = {"component": None}
    ) -> dict[str, Any] | None:
        """Reset process monitor component."""
        component = conf.pop("component")
        return await self._access.post(f"ProcessMonitor.Test.{component}", "reset", conf)
