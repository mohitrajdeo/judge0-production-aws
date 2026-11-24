#!/usr/bin/env python3
"""Add /db/api gateway routing to the mnemon and thanaton nginx server blocks."""
import subprocess
import sys

CONF = "/etc/nginx/sites-enabled/eschaton.conf"

BLOCK = """
    # Portal API bridge: the deployed portal pages call /db/api/<path>.
    # The gateway serves those endpoints at the root, so strip the prefix.
    location /db/api/ {
        rewrite ^/db/api/(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-API-Key $http_x_api_key;
        proxy_set_header Authorization $http_authorization;
        proxy_read_timeout 120s;
    }
"""

with open(CONF, "r", encoding="utf-8") as f:
    text = f.read()

changed = 0
for webroot in ("/var/www/mnemon", "/var/www/thanaton"):
    marker = f"    root {webroot};"
    idx = text.find(marker)
    if idx == -1:
        print(f"WARN: marker not found for {webroot}")
        continue
    section_start = text.rfind("server {", 0, idx)
    section_end = text.find("\n}", idx)
    section = text[section_start:section_end]
    if "location /db/api/" in section:
        print(f"already present for {webroot}")
        continue
    insert_at = idx + len(marker)
    text = text[:insert_at] + "\n" + BLOCK + text[insert_at:]
    changed += 1

if changed == 0:
    print("no changes needed")
    sys.exit(0)

with open(CONF, "w", encoding="utf-8") as f:
    f.write(text)
print(f"patched {changed} server blocks")

test = subprocess.run(["nginx", "-t"], capture_output=True, text=True)
print(test.stderr or test.stdout)
if test.returncode != 0:
    print("nginx test failed; configuration left in place for manual review")
    sys.exit(1)

reload = subprocess.run(["systemctl", "reload", "nginx"], capture_output=True, text=True)
print("reload:", reload.returncode, reload.stderr or reload.stdout)
sys.exit(reload.returncode)
