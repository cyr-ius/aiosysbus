"""NeMo information."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..auth import Auth

# mypy: disable-error-code="no-any-return"


class NeMo:
    """NeMo class.

    Interfaces:
    atm_data, atm_iptv1, atm_iptv2, atm_iptv3, atm_iptv4, atm_multi, atm_voip,
    ETH0, ETH1, ETH2, ETH3, ETH4, dsl0, brguest,
    eth0, eth1, eth2, eth3,eth4, eth6,
    bridge, bridge_aiptv, bridge_viptv, bridge_vviptv, bridge_vvmulti,
    bridge_gvmulti,bridge_vmulti,
    data, dhcp_data, dhcp_iptv, dhcp_voip, dhcp_wan, dhcp6_data,
    guest, gvlan_data, gvlan_multi,
    iptv, lan, lo, ppp_data, rad2g0, rad5g0, rad6g0,
    vap2g0guest0, vap2g0priv0,vap2g0priv1,
    vap5g0guest0, vap5g0priv0, vap5g0priv1, vap6g0priv1,
    veip0, vlan_data, vlan_multi, voip, wifi0_bcm, wifi0_quan,
    wl0, wlguest2, wlguest5, wwan
    """

    def __init__(self, auth: Auth) -> None:
        """Init."""
        self._auth = auth

    async def async_is_up(self, name: str, conf: dict[str, Any] | None = None) -> bool:
        """IsUp.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "isUp", conf)

    async def async_has_flag(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> bool:
        """has Flag.

        Arguments:
        - flag(str) optional
        - condition(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "hasFlag", conf)

    async def async_set_flag(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Set flag.

        Arguments:
        - flag(str) optional
        - condition(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "setFlag", conf)

    async def async_clear_flag(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Clear flag.

        Arguments:
        - flag(str) optional
        - condition(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "clearFlag", conf)

    async def async_is_linked(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> bool:
        """is Linked To.

        Arguments:
        - target(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "isLinkedTo", conf)

    async def async_get_intfs(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> list[Any]:
        """Get interfaces.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getIntfs", conf)

    async def async_lucky_intf(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> str:
        """lucky interface.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "luckyIntf", conf)

    async def async_get_first_parameter(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> str:
        """Get first parameter.

        Arguments:
        - name(str) optional
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getFirstParameter", conf)

    async def async_set_first_parameter(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Set first parameter.

        Arguments:
        - name(str) optional
        - value(str) optional
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "setFirstParameter", conf)

    async def async_get_parameters(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> str:
        """Get parameters.

        Arguments:
        - name(str) optional
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getParameters", conf)

    async def async_set_parameters(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Set parameters.

        Arguments:
        - name(str) optional
        - value(str) optional
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "setParameters", conf)

    async def async_get_MIBs(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Get MIBs.

        Arguments:
        - mibs(str) optional
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getMIBs", conf)

    async def async_set_MIBs(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Set MIBs.

        Argument:
        - mibs(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "setMIBs", conf)

    async def async_open_query(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> int:
        """Open query.

        Argument:
        - subscriber(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "openQuery", conf)

    async def async_close_query(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Close query.

        Arguments:
        - subscriber(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "closeQuery", conf)

    async def async_csi_register(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """csi register.

        Arguments:
        - func (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "csiRegister", conf)

    async def async_csi_unregister(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """csi unregister.

        Arguments:
        - func (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "csiUnregister", conf)

    async def async_csi_finish(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """csi finish.

        Arguments:
        - id(int) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "csiFinish", conf)

    async def async_copy(self, name: str, conf: dict[str, Any] | None = None) -> None:
        """copy.

        Arguments:
        - name (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "copy", conf)

    async def async_get_dhcp_option(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Get DHCP Option.

        Arguments:
        - type(str) optional
        - tag(int) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getDHCPOption", conf)

    async def async_get_addrs(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> list[Any]:
        """Get Addresses.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getAddrs", conf)

    async def async_lucky_addr(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """lucky address.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "luckyAddr", conf)

    async def async_lucky_addr_address(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> str:
        """lucky Addr Address.

        Arguments:
        - flag(str) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "luckyAddrAddress", conf)

    async def async_get_ra_options(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Get RA options.

        Arguments:
        - tag(int) optional
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getRAOptions", conf)

    async def async_get_ra_routers(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Get RA Routers.

        Arguments:
        - traverse(str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "getRARouters", conf)

    async def async_refres_net_dev(self, name: str) -> None:
        """Refresh NetDev."""
        return await self._auth.post(f"NeMo.Intf.{name}", "refreshNetDev")

    async def async_get_net_dev_stats(self, name: str) -> None:
        """Get Net Dev Stats."""
        return await self._auth.post(f"NeMo.Intf.{name}", "getNetDevStats")

    async def async_set_net_dev_flag(self, name: str, conf: dict[str, Any]) -> None:
        """Set Net Dev Flag.

        Argument:
        - flags (str)
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "setNetDevFlag", conf)

    async def async_clear_net_dev_flag(self, name: str, conf: dict[str, Any]) -> None:
        """clear Net Dev Flag.

        Argument:
        - flags (str)
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "clearNetDevFlag", conf)

    # "NeMo.Intf.dsl0
    async def async_get_dsl0_line_stats(self) -> None:
        """Get DSL Line Stats."""
        return await self._auth.post("NeMo.Intf.dsl0", "getDSLLineStats")

    async def async_get_dsl0_stats(self) -> None:
        """Get DSL Stats."""
        return await self._auth.post("NeMo.Intf.dsl0", "getDSLStats")

    async def async_getxdsl0_noise_measure(self, conf: dict[str, Any]) -> None:
        """Get XDSL Noise Measure.

        Argument:
        - typeMeasure (str)
        """
        return await self._auth.post("NeMo.Intf.dsl0", "getXDSLNoiseMeasure", conf)

    async def async_get_dsl0_channel_stats(self) -> None:
        """Get DSL Channel Stats."""
        return await self._auth.post("NeMo.Intf.dsl0", "getDSLChannelStats")

    # NeMo.Intf.xxx.Query
    async def async_get__result(self, name: str) -> None:
        """Get result."""
        return await self._auth.post(f"NeMo.Intf.{name}.Query", "getResult")

    # Specific vap* / wlguest
    async def async_kick_station(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Kick Station.

        Argument:
        - macaddress (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "kickStation", conf)

    async def async_kick_station_reason(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Kick Station Reason.

        Argument:
        - macaddress (str) optional
        - reason (int) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "kickStationReason", conf)

    async def async_clean_station(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Clean station.

        Argument:
        - macaddress (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "cleanStation", conf)

    async def async_send_bss_transfer(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Clean station.

        Argument:
        - mac (str) optional
        - target (str) optional
        - class (int) optional
        - channel (int) optional
        - wait (int) optional
        - retries (int) optional
        - bssidInfo (int) optional
        - transitionReason (int) optional
        """
        return await self._auth.post(
            f"NeMo.Intf.{name}", "sendBssTransferRequest", conf
        )

    async def async_send_publication(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Clean station.

        Argument:
        - mac (str) optional
        - oui (str) optional
        - type (int) optional
        - subtype (int) optional
        - channel (int) optional
        - data (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "sendPublicAction", conf)

    async def async_send_remote_measument(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> None:
        """Clean station.

        Argument:
        - mac (str) optional
        - bssid (str) optional
        - class (int) optional
        - channel (int) optional
        - timeout (int) optional
        - ssid (str) optional
        """
        return await self._auth.post(
            f"NeMo.Intf.{name}", "sendRemoteMeasumentRequest", conf
        )

    async def async_get_ssid_stats(self, name: str) -> None:
        """Get SSID stats."""
        return await self._auth.post(f"NeMo.Intf.{name}", "getSSIDStats")

    async def async_get_status_histogram(self, name: str) -> None:
        """Get status histogram."""
        return await self._auth.post(f"NeMo.Intf.{name}", "getStatusHistogram")

    async def async_get_station_stats(self, name: str) -> None:
        """Get station."""
        return await self._auth.post(f"NeMo.Intf.{name}", "getStationStats")

    async def async_get_far_associated_devices_count(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> int:
        """Get Far Associated Devices count.

        Argument:
        - threshold (int) optional
        """
        return await self._auth.post(
            f"NeMo.Intf.{name}", "getFarAssociatedDevicesCount", conf
        )

    async def async_del_neighbour_AP(
        self, name: str, conf: dict[str, Any] | None = None
    ) -> int:
        """Del neighbour AP.

        Argument:
        - BSSID (str) optional
        """
        return await self._auth.post(f"NeMo.Intf.{name}", "delNeighbourAP", conf)

    async def async_set_wlan_config(
        self, interfacename: str, conf: dict[str, Any]
    ) -> dict[str, Any]:
        """Set WLAN configuration.

        Arguments:
        - Interfacename (str): interface name (lan, wifi0_bcm, wifi0_quan, etc.)
        - conf (dict)
        """
        return await self._auth.post(
            f"NeMo.Intf.{interfacename}", "setWLANConfig", conf
        )

    # Custom methods
    async def async_wifi(self, enable: bool) -> None:
        """Set wifi.

        Arguments:
        - Enable (bool)
        """
        conf = {
            "mibs": {
                "penable": {
                    "wl0": {
                        "Enable": enable,
                        "PersistentEnable": enable,
                        "Status": enable,
                    },
                    "eth4": {
                        "Enable": enable,
                        "PersistentEnable": enable,
                        "Status": enable,
                    },
                },
                "wlanvap": {"wl0": {}, "eth4": {}},
            }
        }
        await self.async_set_wlan_config(interfacename="lan", conf=conf)


# WWAN
#   - void setPin((string pin))
#   - void resetPin((string puk), (string newpin))
#   - void configureConnection((string apn), (string username), (string Password))
#   - string getPinType()

# rad /wifi0
#   - void setChanspec((uint16 channel), (string bandwidth), (string frequency), (string reason), (bool direct), (string reasonDetails))
#   - void apDelayUpDone()
#   - void startAutoChannelSelection()
#   - void getSpectrumInfo((bool update))
#   - void startScan((string SSID), (string channels), (string scanReason), (bool forceFast))
#   - void stopScan()
#   - list scan((string SSID), (string channels), (int minRssi), (string scanReason), (bool forceFast), (bool updateUsage))
#   - void scanCombinedData((string SSID), (string channels), (int minRssi), (string scanReason), (bool forceFast))
#   - list getScanResults((variant results))
#   - int32 DFS_drvdbg((string dbg_action))
#   - void getProbeRequests((datetime fromTime))
#   - void getRadioAirStats()
#   - void getRadioStats()
#   - void getPerAntennaRssi()
#   - variant getLatestPower()
#   - variant getStatusHistogram()
#   - void startDFSclear()
#   - void stopDFSclear()

# atm
# - bool oamPing()
