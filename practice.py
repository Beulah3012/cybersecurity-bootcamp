import os

directory = input("What is the path?")

try:
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            print(item)
except FileNotFoundError:
    print("Path does not exist")
except PermissionError:
    print("Permission denied to path")
except Exception as e:
    print(f"Error: {e}")
    print(f"Path entered: {directory}")




            









        



       
        



