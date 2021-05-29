"""Diagnostics and data statistics."""

class Diagnostic:
    """System class."""

    def __init__(self, access):
        """Init."""
        self._access = access

    # ############ DATA STATS #############

    def get_stats_account(self, conf=None):
        """Set  enable remote access."""
        return self._access.post("DataStatistics.account", "getStats", conf)

    def get_stats_media(self, conf=None):
        """Get time left for remote access."""
        return self._access.post("DataStatistics.mediahub", "getStats", conf)

    def get_stats_storage(self, conf=None):
        """Reset timer for remote access."""
        return self._access.post("DataStatistics.storage", "getStats", conf)

    # ############ AUTO DIAG #############

    def run_diags(self, conf):
        """Set  enable remote access."""
        return self._access.post("AutoDiag", "executeDiagnostics", conf)

    def run_diags_trigger(self, conf):
        """Get time left for remote access."""
        return self._access.post("AutoDiag", "executeTrigger", conf)

    def remove_diags(self, conf):
        """Reset timer for remote access."""
        return self._access.post("AutoDiag", "cancelDiagnostics", conf)

    def get_diags_states(self, conf=None):
        """Set  enable remote access."""
        return self._access.post("AutoDiag", "getDiagnosticsState", conf)

    def get_diags_list(self, conf=None):
        """Get time left for remote access."""
        return self._access.post("AutoDiag", "getDiagnosticsList", conf)

    def get_diags_listdiag(self, conf=None):
        """Reset timer for remote access."""
        return self._access.post("AutoDiag", "listDiagnostics", conf)

    def set_diags(self, conf):
        """Set  enable remote access."""
        return self._access.post("AutoDiag", "setUserInput", conf)

    # ############ TOPOLOGY DIAG #############

    def get_topodiags(self, conf=None):
        """Get topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "get", conf)

    def set_topodiags(self, conf):
        """Set topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "set", conf)

    def set_topodiags_build(self, conf=None):
        """Build topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "buildTopology", conf)

    def upload_topodiags(self, conf=None):
        """Upload topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "uploadTopology", conf)

    def enable_topodiags(self, conf=None):
        """Enable topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "enableAutomaticUpload", conf)

    def get_topodiags_isautoupload(self, conf=None):
        """Is Automatic Upload enabled of topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "isAutomaticUploadEnabled", conf)

    def set_topodiags_customerauthor(self, conf):
        """Set customer authorization of topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "setCustomerAuthorization", conf)

    def export_topodiags(self, conf):
        """Export topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "export", conf)

    def import_topodiags(self, conf):
        """Import topology diagnostics."""
        return self._access.post("TopologyDiagnostics", "import", conf)

    def get_topodiags_result(self, conf={"result": None}):
        """Get result of topology diagnostics."""
        result = conf.pop("result")
        return self._access.post(f"TopologyDiagnostics.Results.Result.{result}", "get", conf)

    # ############ PROCESS MONITOR #############

    def get_process(self, conf=None):
        """Get process monitor."""
        return self._access.post("ProcessMonitor", "get", conf)

    def set_process(self, conf):
        """Set process monitor."""
        return self._access.post("ProcessMonitor", "set", conf)

    def get_process_component(self, conf={"component": None}):
        """Get process monitor component."""
        component = conf.pop("component")
        return self._access.post(f"ProcessMonitor.Test.{component}", "get", conf)

    def set_process_component(self, conf={"component": None}):
        """Set process monitor component."""
        component = conf.pop("component")
        return self._access.post(f"ProcessMonitor.Test.{component}", "set", conf)

    def reset_process_component(self, conf={"component": None}):
        """Reset process monitor component."""
        component = conf.pop("component")
        return self._access.post(f"ProcessMonitor.Test.{component}", "reset", conf)
