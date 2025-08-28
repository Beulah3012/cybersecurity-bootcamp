# Week 7, Wednesday
# Write a Python script to list running services, reinforcing service management.
# Task:
# Script to:
# List running Windows services.
# Print service names and statuses.
# Handle errors (e.g., permission issues).
# Hints:
# Use winreg module to access registry.
# Run in Windows VM as AdminUser.



import os

try:
    print("=== running services ===")
    os.system("sc query state= all")
except Exception as e:
    print("Error:",e)


