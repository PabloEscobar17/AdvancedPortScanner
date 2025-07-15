import socket

def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"[✓] Resolved {host} to {ip}")
        return ip
    except socket.gaierror:
        print(f"[✗] Could not resolve domain: {host}")
        return None
