import os

directory = input("Tell us the name of your directory: ").strip()
extension = input("Tell us the type of extension: e.g, .txt ").strip()

try:
    for root, _, files in os.walk(directory):
         for file in files:
              if file.endswith(extension):
                   print(file)
                   path = os.path.join(root, file)
                   print(path)
except FileNotFoundError:
     print(f"Error: Directory {directory} not found")
except PermissionError:
     print(f"Error:No permissions for {directory} ")
     
except Exception as e:
     print(f"Error: {e}")