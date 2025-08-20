# Script to:
# Read `/etc/passwd`.
# List usernames (first field).
# Print usernames.
# Handle errors (e.g., file access).
# Hints:
# Use `open()` to read file.
# Save as `list_users.py`, run in Kali VM.




list_users = "/etc/passwd"

def file_users():
    try:
        with open(list_users, "r") as f:
            for line in f:
                name = line.split(":")
                username = (name[0])
                print(username)
    except FileNotFoundError:
        print(f"Error: {list_users} not found.")
    except PermissionError:
        print(f"Error: Permission denied when reading{list_users}.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    file_users()