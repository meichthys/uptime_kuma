# Uptime Kuma HACS integration

This integration is temporary and is expected to soon be merged into HomeAssistant Core, but until then it will be available via HACS.

## Usage

Install using HACS and setup like any other integration via the UI. Enter the uptime kuma instane url and credentials.

## Issues

Note: Currently, the instance doesn't list the entities on the integrations page, but they should exist under developer tools using the endity id of: `binary_sensor.<uptimekuma monitor name>`. 
