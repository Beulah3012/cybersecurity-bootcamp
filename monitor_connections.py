import psutil
import time
from datetime import datetime

def monitor_connections():
    try:
        for i in range(3):
            timestamp = datetime.now().strftime("%m%d%Y %H:%M:%S")
            print(f"\nscan {i+1} at {timestamp} (layer 4: transport):")
            for conn in psutil.net_connections(kind="tcp"):
                if conn.status == "ESTABLISHED":
                    local = f"{conn.laddr.ip}:{conn.laddr.port}"
                    remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "None"
                    print(f"Local: {local}, Remote: {remote}")
            time.sleep(10)
    
    except PermissionError:
        print("Error: Run as Admin")

monitor_connections()        


















    
