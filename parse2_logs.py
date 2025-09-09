# Objective: Write a Python script to parse exported Event Viewer logs (.csv), reinforcing analysis skills.
# Task:
# Script to:
# Read a .csv log file (e.g., security_log.csv).
List Event ID 4625 entries (failed logins).
# Print event details (e.g., time, user).
# Handle errors.
# Hints:
# Use csv module

import csv

def parse2_logs(file_path):
    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            print("Failed login events (ID 4625):")
            for row in reader:
                if row.get("EventID") == "4625":
                    time = row.get("TimeCreated")
                    user = row.get("AccountName", "Unknown")
                    print(f"Time: {time}, User: {user}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parse2_logs(r"C:\Users\kemio\Documents\file.csv")