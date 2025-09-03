# week 6, Thursday
# Objective: Write a Python script to list files in C:\Windows\Logs, simulating log file checks.
# Script to:
# Take a directory path (e.g., C:\Windows\Logs).
# List files and modification times.
# Print in YYYY-MM-DD HH:MM:SS format.
# Handle errors.
# Hints:
# Use os.listdir, os.path.getmtime, datetime.



import os
import datetime

# step 1: pick the folder (the toy box)
folder = r'C:\Windows\logs'

try:
    # step 2: look inside the folder
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        # step 3: only check if it really a file
        if os.path.isfile(path):
            # step 4: find last time it was changed
            mtime = os.path.getmtime(path)
            last_time = datetime.datetime.fromtimestamp(mtime)

            # step 5: print name + time in nice format
            print(f"{file} - {last_time.strftime('%Y-%m-%d %H:%M:%S')}")

except Exception as e:
    # step 6: catch any "uh ohs"
    print("Oops! Something went wrong:", e)






