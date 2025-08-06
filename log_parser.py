#Write a program to:
#Extract IPs from a log string (e.g., “Error from 192.168.1.1”).
#Use regex.
#Example output: IP: 192.168.1.1

import re

# Example log string
log = "IP: 192.168.1.1, Time: 2025-06-20"

# Split the log by ", " for individual parts (optional)
parts = log.split(", ")
print(parts[0])  # This prints: IP: 192.168.1.1

# Search for an IP address using regex
ip = re.search(r"\d+\.\d+\.\d+\.\d+", log)

# If an IP was found, print it
if ip:
    print(f"IP: {ip.group()}")
else:
    print("No IP address found.")
