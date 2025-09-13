import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP (e.g., 127.0.0.1): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))
    scan_ports(target_ip, start, end)
