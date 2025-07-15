import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                sock.send(b'HEAD / HTTP/1.1\r\n\r\n')
                banner = sock.recv(1024).decode(errors='ignore').strip()
                return (port, banner if banner else "Open - No banner")
            except:
                return (port, "Open - No banner")
        sock.close()
    except Exception:
        return None
    return None

def scan_ports(host, start_port, end_port):
    print(f"\n[+] Scanning {host} from port {start_port} to {end_port}\n")
    results = []

    for port in range(start_port, end_port + 1):
        res = scan_port(host, port)
        if res:
            print(f"[OPEN] Port {res[0]} ➜ {res[1]}")
            results.append(res)

    return results
