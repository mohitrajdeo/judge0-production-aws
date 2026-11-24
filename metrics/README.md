# Nephis provider metrics deployment

Two Go control planes expose measured provider values with `value`, `unit`, `observed_at`, `source` and `stale`. Missing values are `null` with `stale: true`.

## Units

Copy the two `*.service` files to `/etc/systemd/system/` on the production host, then:

```bash
sudo mkdir -p /opt/nephis/metrics /var/lib/nephis/metrics-storage
sudo chown ubuntu:ubuntu /var/lib/nephis/metrics-storage
sudo cp mnemon-api-metrics thanaton-api-metrics /opt/nephis/metrics/
sudo chmod 755 /opt/nephis/metrics/*
sudo systemctl daemon-reload
sudo systemctl enable --now nephis-metrics-mnemon nephis-metrics-thanaton
systemctl is-active nephis-metrics-mnemon nephis-metrics-thanaton
```

Binaries are built from `mnemon-control-plane/cmd/api` and `thanaton-control-plane/cmd/api` in the `extra-features` monorepo (`GOOS=linux GOARCH=amd64 CGO_ENABLED=0`).

## Nginx

`patch_remote_nginx_dbapi.py` adds `/db/api/` proxying to the gateway on `127.0.0.1:8080` with the prefix stripped — without it the portal's API calls fall through to the SPA.

`patch_remote_nginx_metrics.py` adds:

- `/v1/metrics/` → `127.0.0.1:7101` (Mnemon)
- `/api/v1/metrics/fleet/` → `127.0.0.1:8399` (Thanaton)

Both scripts run `nginx -t` before reloading. Review the diff before applying on a new host.

## Verification

```bash
curl -H "X-API-Key: $NEPHIS_API_KEY" https://nephis.theeducode.com/v1/metrics/catalog
curl -H "X-API-Key: $NEPHIS_API_KEY" https://nephis.theeducode.com/api/v1/metrics/fleet/overview
```

Full endpoint contract: `docs/METRICS_API_REFERENCE.md` in the `extra-features` monorepo.
