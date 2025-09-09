import os
import stat

path = input("Path to be checked ")
try:
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            variable = os.stat(full_path)
            variable2 =stat.filemode (variable.st_mode)
            print(item, variable2)
except FileNotFoundError:
    print(f"Error: Directory {path} not found")
except PermissionError:
    print(f"Error:Permission denied for {path}")

            
except Exception as e:
    print(f" Error:{e}")