import os

def files_list(path):
    try:
        items = os.listdir(path)
        print(f"Files in {path}:")
        for item in items:
            directory = os.path.join(path, item)
            if os.path.isfile(directory):
                size = os.path.getsize(directory)
                print(f"{item}, {size} bytes")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
path = r"C:\Users\kemio" 
files_list(path)





