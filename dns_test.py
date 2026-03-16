import socket
import requests

host = 'oauth2.googleapis.com'
print(f"Testing DNS for {host}...")

try:
    addr_info = socket.getaddrinfo(host, 443)
    print(f"Socket getaddrinfo success: {addr_info}")
except Exception as e:
    print(f"Socket getaddrinfo failed: {e}")

try:
    r = requests.get(f"https://{host}/", timeout=5)
    print(f"Requests get success: {r.status_code}")
except Exception as e:
    print(f"Requests get failed: {e}")

# Check for proxy env vars
import os
print(f"HTTP_PROXY: {os.environ.get('HTTP_PROXY')}")
print(f"HTTPS_PROXY: {os.environ.get('HTTPS_PROXY')}")
print(f"ALL_PROXY: {os.environ.get('ALL_PROXY')}")
