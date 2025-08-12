#Objective: Write a Python script to list directories, reinforcing navigation skills.

##Task: Script to: Take a directory path (e.g., /home). List only directories (not files). Print directory names. Handle errors (e.g., invalid path).

#Hints: Use os.listdir, os.path.isdir, os.path.join. Run in Kali VM. Use try/except.

#Takes a directory path as input.

#Lists only directories inside it (ignores files).


import os

def list_directories(path):
    try:
        # Get all entries in the path
        entries = os.listdir(path)

        print(f"Directories in '{path}':")
        for entry in entries:
            full_path = os.path.join(path, entry)  # Join path + entry
            if os.path.isdir(full_path):  # Check if it's a directory
                print(entry)

    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for path
directory_path = input("Enter the directory path: ")
list_directories(directory_path)
