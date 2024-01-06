"""
Provides API access to Livebox.
"""

from .call import Call, Phonebook
from .connection import Connection
from .device import DeviceInfo, Devices
from .diagnostic import Diagnostic
from .dnsdhcp import Dhcp, DynDNS
from .event import Event
from .gui import UserInterface
from .nat import Nat
from .network import GuestWifi, Lan, Wifi
from .schedule import Schedule
from .screen import Screen
from .services import (
    DataHub,
    Domino,
    Locations,
    Manifests,
    Profiles,
    RuleEngine,
    RuleFactory,
    Ssw,
    Zwave,
)
from .storage import HTTPService, StorageService, USBHosts
from .system import System
from .user import UserManagement

__all__ = [
    "Call",
    "Connection",
    "DataHub",
    "DeviceInfo",
    "Devices",
    "Dhcp",
    "Diagnostic",
    "Domino",
    "DynDNS",
    "Event",
    "GuestWifi",
    "HTTPService",
    "Lan",
    "Locations",
    "Manifests",
    "Nat",
    "Phonebook",
    "Profiles",
    "RuleEngine",
    "RuleFactory",
    "Schedule",
    "Screen",
    "Ssw",
    "StorageService",
    "System",
    "USBHosts",
    "UserInterface",
    "UserManagement",
    "Wifi",
    "Zwave",
]
