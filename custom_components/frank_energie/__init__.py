"""The Frank Energie component."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_COORDINATOR, DOMAIN
from .coordinator import FrankEnergieCoordinator

_LOGGER = logging.getLogger(__name__)
PLATFORMS = Platform.SENSOR


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the Frank Energie component from a config entry."""

    # Initialise the coordinator and save it as domain-data
    web_session_client = async_get_clientsession(hass)
    frank_coordinator = FrankEnergieCoordinator(hass, web_session_client)

    # Fetch initial data, so we have data when entities subscribe and set up the platform
    await frank_coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        CONF_COORDINATOR: frank_coordinator,
    }

    await hass.config_entries.async_forward_entry_setup(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
