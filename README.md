# Uptime Kuma HACS integration

## About

This integration exposes UptimeKuma monitors in HomeAssistant. Two sensors are created for each UptimeKuma monitor:

- Binary Sensor (On/Off)
- Sensor (State of UptimeKuma monitor)

## Installation

Installation is done like any other Home Assistant HACS integration.

### Requirements

In order to setup this integration you will need:

- A Home Assistant instance with [HACS](https://hacs.xyz/) installed.
- An instance of UptimeKuma

### HACS Installation

Search for "Uptime Kuma" in the HACS store. If you don't see it there, you can [add this repository url as a HACS custom repository](https://hacs.xyz/docs/faq/custom_repositories).

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/meichthys/uptime_kuma)

## Home Assistant Integration

[![Open your Home Assistant instance and start setting up a new integration of a specific brand.](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/brand/?brand=+Uptime+Kuma)

After installation, setup the integration via the web UI like any other integration. When prompted, provide the following:

- Your UptimeKuma instance url (i.e. https://myuptimekuma.mydomain.com)
- Port (Generally 443 if running behind reverse proxy)
- Your uptimekuma credentials
  - NOTE: If you have issues connecting, try creating an uptimekuma API key and using that with NO username for the credentials.
  -If you are still having issues,make sure you can successfully connect to `http(s)://your_uptimekuma.url/metrics`
- Verify SSL (Generally checked)

## Contributions

Contributions are welcome!