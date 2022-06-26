"""UptimeKuma binary_sensor platform."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import UptimeKumaDataUpdateCoordinator
from .const import DOMAIN
from .entity import UptimeKumaEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the UptimeKuma binary_sensors."""
    coordinator: UptimeKumaDataUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        UptimeKumaBinarySensor(
            coordinator,
            BinarySensorEntityDescription(
                key=str(monitor.monitor_name),
                name=monitor.monitor_name,
                device_class=BinarySensorDeviceClass.CONNECTIVITY,
            ),
            monitor=monitor,
        )
        for monitor in coordinator.data
    )


class UptimeKumaBinarySensor(UptimeKumaEntity, BinarySensorEntity):
    """Representation of a UptimeKuma binary sensor."""

    @property
    def is_on(self) -> bool:
        """Return True if the entity is on."""
        return self.monitor_available
