#Create port_scanner.py.
#Write a program to:
#Check ports 80, 443 on a host (e.g., “localhost”).
#Use socket to test connections.


import socket

host = "localhost"
ports = [80, 443]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()
    except Exception as e:
        print(f"Error checking port {port}: {e}")

