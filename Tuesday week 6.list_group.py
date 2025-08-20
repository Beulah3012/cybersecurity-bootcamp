#Objective**: Write a Python script to list group members from `/etc/group`.
#Script to:
# Read `/etc/group`.
# List users in a specified group (e.g., `team`).
# Print usernames.
# Handle errors.
# Use `open()` to read file.
#Run in Kali VM.


list_group = "/etc/group"

def file_group():
    try:
        with open(list_group, "r") as f:
            print("Group members:")
            for line in f:
                if line.strip():
                    team = line.split(":")[0]
                    print(team)               
    except FileNotFoundError:
        print(f"Error: {list_group} not found.")
    except PermissionError:
        print(f"Error: Permission denied when reading{list_group}.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    file_group()
        