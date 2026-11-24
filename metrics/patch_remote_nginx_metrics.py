#!/usr/bin/env python3
"""Route metrics API paths to the deployed Go metrics control planes."""
import re
import subprocess
import sys

CONF = "/etc/nginx/sites-enabled/eschaton.conf"

BLOCKS = """
    location /v1/metrics/ {
        proxy_pass http://127.0.0.1:7101;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }

    location /api/v1/metrics/fleet/ {
        proxy_pass http://127.0.0.1:8399;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
"""

with open(CONF, "r", encoding="utf-8") as f:
    text = f.read()

if "location /v1/metrics/" in text:
    print("metrics routes already present")
    sys.exit(0)

# Insert into each server block that serves a portal web root.
pattern = re.compile(r"(    root /var/www/[^\s]+;)")
matches = list(pattern.finditer(text))
if not matches:
    print("no web roots found")
    sys.exit(1)

out = []
last = 0
for m in matches:
    out.append(text[last:m.end()])
    out.append(BLOCKS)
    last = m.end()
out.append(text[last:])
text = "".join(out)

with open(CONF, "w", encoding="utf-8") as f:
    f.write(text)
print(f"patched {len(matches)} server blocks")

test = subprocess.run(["nginx", "-t"], capture_output=True, text=True)
print(test.stderr or test.stdout)
if test.returncode != 0:
    sys.exit(1)

reload = subprocess.run(["systemctl", "reload", "nginx"], capture_output=True, text=True)
print("reload:", reload.returncode, reload.stderr or reload.stdout)
sys.exit(reload.returncode)
