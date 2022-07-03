"""UptimeKuma binary_sensor platform."""
from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from pyuptimekuma import UptimeKumaMonitor

from . import UptimeKumaDataUpdateCoordinator
from .const import DOMAIN
from .entity import UptimeKumaEntity
from .utils import format_entity_name


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

    def __init__(
        self,
        coordinator: UptimeKumaDataUpdateCoordinator,
        description: EntityDescription,
        monitor: UptimeKumaMonitor,
    ) -> None:
        """Set entity ID."""
        super().__init__(coordinator, description, monitor)
        self.entity_id = (
            f"binary_sensor.uptimekuma_{format_entity_name(self.monitor.monitor_name)}"
        )

    @property
    def is_on(self) -> bool:
        """Return True if the entity is on."""
        return self.monitor_available
