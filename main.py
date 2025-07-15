from scanner.resolver import resolve_host
from scanner.port_scan import scan_ports
from scanner.logger import save_results
import argparse

def main():
    parser = argparse.ArgumentParser(description="Modular Python Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", help="Port range (e.g. 20-100)", default="20-1024")

    args = parser.parse_args()
    port_range = args.ports.split("-")

    try:
        start = int(port_range[0])
        end = int(port_range[1])
        if not (0 < start <= end <= 65535):
            raise ValueError
    except:
        print("[✗] Invalid port range. Use format: 20-80")
        return

    ip = resolve_host(args.target)
    if ip:
        results = scan_ports(ip, start, end)
        if results:
            save_results(results, args.target)
        else:
            print("[!] No open ports found.")

if __name__ == "__main__":
    main()
