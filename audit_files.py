# audit_files.py
# Objective: Write a Python script to find world-writable files.
# - Take a directory path as input (e.g., /tmp).
# - List files with world-writable permissions (o=w).
# - Print the full file paths of those files.
# - Handle errors (e.g., permission issues, missing files).
# Hints:
# - Use os.walk to recursively scan directories.
# - Use os.stat and stat.S_IWOTH to check file permissions.




import os
import stat

def audit_writable(path):
    try:
        print(f"World-writeable files in {path}:()")
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    if os.stat(file_path).st_mode & stat.S_IWOTH:
                        print(file_path)
                except PermissionError:
                    print(f"Errror: permission deny for {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    audit_writable("/tmp")
