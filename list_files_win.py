# Monday week 7
# Script to:
  # 1. Take a directory path (e.g., `C:\Users\StandardUser`).
  # 2. List all files (not folders).
  # 3. Print file names and sizes (bytes).
  # 4. Handle errors (e.g., invalid path).
  # Hints
  # Use `os.listdir`, `os.path.isfile`, `os.path.getsize`.
  # Use raw strings (`r"C:\..."`).
 # Run in Windows VM.


import os

# Function to list files and their sizes in a given directory
def files_list(path):
    try:
        # List all items (files and folders) in the specified path
        items = os.listdir(path)
        print(f"Files in {path}:")
        
        # Loop through each item
        for item in items:
            # Build the full path to the item
            directory = os.path.join(path, item)
            
            # Check if the item is a file (not a folder)
            if os.path.isfile(directory):
                # Get the size of the file in bytes
                size = os.path.getsize(directory)
                # Print the file name and size
                print(f"{item}, {size} bytes")
    
    # Handle the case where the directory doesn't exist
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    
    # Handle permission errors (e.g., trying to access system folders)
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    
    # Catch all other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Set the directory path (use raw string format for Windows paths)
path = r"C:\Users\kemio"
files_list(path)
