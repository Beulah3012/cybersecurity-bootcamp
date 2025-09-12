# Objective: Write a Python script to retrieve the VM’s IP address, reinforcing Layer 3 (Network) concepts.
# Task:
# Script to:
# Get VM’s IPv4 address (e.g., 192.168.56.100) using socket.
# Print address with timestamp (Layer 7: Application).
# Handle errors (e.g., no network).
# Hints:
# Use socket.gethostbyname and datetime.
# Run as StandardUser in Command Prompt.
# Verify with ipconfig /all.
# Deliverable:
# Save script as get_ip.py in C:\Users\StandardUser.
# Run: python get_ip.py.
# Submit: Script and screenshot of output (StudentName_Week9_Monday_Output.png).
# Push to GitHub (git add ., git commit -m "Week 9 Monday homework", git push).


import socket
import datetime

try:
    ip = socket.gethostbyname(socket.gethostname())
    print(f"{datetime.datetime.now()} - VM IP Address:{ip}")
except:
    print("could not retrieve ip address.")