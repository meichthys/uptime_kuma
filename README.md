# Uptime Kuma HACS integration (*Deprecated*)

> [!IMPORTANT]  
> There is now an UptimeKuma core integration in HomeAssistant. It is recommended to migrate to that integration since I will no longer be updating this one.
>
> I'm nore than glad to retire the project as it did take a reasonable amount of time and continuous support for non-technical users.
> If you would like to drop a token of appreciation, you can do so [here](https://liberapay.com/meichthys/donate).
>  
> For details on switching to the core integration, [see comment](https://github.com/meichthys/uptime_kuma/issues/132#issuecomment-3186001510).

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

### HTTPS Connections

- URL: Your UptimeKuma instance url (i.e. https://myuptimekuma.mydomain.com _without_ a trailing slash)
- Port: (Generally 443 if running behind reverse proxy)
- User: Your uptimekuma Username
- Password: API Key (UptimeKuma > Settings > API Keys)
- Verify SSL: (Generally checked)

### HTTP Connections

- URL: Your UptimeKuma instance url (i.e. http://xxx.xxx.xxx.xxx)
  - Note: make sure there is NO trailing slash at the end of the url
- Port : 3001
- User: Your uptimekuma Username
- Password: API Key (UptimeKuma > Settings > API Keys)
- Verify SSL: Unchecked

### Troubleshooting

If you are having issues connecting, make sure you can successfully connect to `http(s)://your_uptimekuma.url/metrics` using a private browser window.
There have also been reports of non-ssl instances not being entirely reliable. It is recommended to use a valid SSL certificate. This is made easy by projects like [NGINXProxyManager](https://nginxproxymanager.com/), [Traefik](https://doc.traefik.io/traefik/), [Caddy](https://caddyserver.com/), and others.

## Contributions

Contributions are welcome!
