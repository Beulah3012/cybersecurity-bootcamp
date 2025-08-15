import os
import stat

def list_file_permissions(path):
    try:
        items = os.listdir(path)
        print(f"\nFiles and permissions in: {path}\n")
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                file_stat = os.stat(item_path)
                permissions = stat.filemode(file_stat.st_mode)
                print(f"{item}: {permissions}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    path = input("Enter a full directory path (e.g., /tmp): ").strip()
    list_file_permissions(path)
