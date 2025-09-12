# September 11th 2025
# Objective: Write a Pythonscript to capture packets, reinforcing OSI Layers 2–4.
# Task: Script to:
# Capture 5 packets using scapy (e.g., ICMP or TCP).
# Print source/destination IPs (Layer 3) and ports (Layer 4, if TCP/UDP).
# Handle errors (e.g., no packets). Hints: Use scapy (pip install scapy). Run as AdminUser in Command Prompt. Compare with Wireshark output.
# Deliverable: Save script as capture_packets.py in C:\Users\AdminUser. Run: python capture_packets.py. Submit: Script and screenshot of output

from scapy.all import sniff
from datetime import datetime


def capture_packets():
    try:
        timestamp = datetime.now().strftime("%Y%m%d %H:%M:%S")
        print(f"Capturing packets at {timestamp}...")
        packets = sniff(count=5, filter="tcp or icmp")
        for pkt in packets:
            if pkt.haslayer("IP"):
                src_ip = pkt["IP"].src  # Layer 3
                dst_ip = pkt["IP"].dst
                layer_info = f"IP: {src_ip} > {dst_ip} (Layer 3)"
                if pkt.haslayer("TCP"):
                    src_port = pkt["TCP"].sport
                    dst_port = pkt["TCP"].dport
                    layer_info += f", TCP Ports: {src_port} > {dst_port} (Layer 4)"
                print(layer_info)
    except PermissionError:
        print("Error: Run as AdminUser")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    capture_packets()
