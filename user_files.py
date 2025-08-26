# Script to:
# Take a directory and username (e.g., /tmp, testuser).
# List files owned by the user.
# Print file paths.
# Handle errors.
# Hints:
# Use os.walk, os.stat, pwd.getpwuid.
# Run in Kali VM.
# Save as user_files.py, run in Kali VM.
#Submit script and screenshot of output.


import os
import pwd

def find_user_files(path, username):
    try:
        # Look up the student's ID number
        uid = pwd.getpwman(username).pw_uid
        print(f"files owned by {username} in {path}:")

        #walk around the toy box folder
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, files)
                
                #check if the toy belongs to the student
                if os.stat(file_path).st_uid == uid:
                    print(file_path)
    except KeyERROR:
        print(f"Error: User {username} not found")
    except PermissionError:
        print(f"Error: Permission denied")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == " __main__":
    find_user_files("/tmp", "testuser")


