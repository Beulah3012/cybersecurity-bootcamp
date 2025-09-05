# week 7, Wednesday
# Objective: Write a Python script to check user account status, reinforcing management skills.
# Task:
# Script to:
# List users and their enabled/disabled status.
# Print usernames and status.
# Handle errors.
# Hints:
# Use winreg module.
# Run in Windows VM as AdminUser.
import winreg
def check_user_status():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SAM\SAM\Domains\Account\Users\Names")
        i = 0
        print("User status:")
        while True:
            try:
                user = winreg.EnumKey(winreg.HKEY_LOCAL_MACHINE, 1)
                subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, f"SOFTWARE\\Domains\\SAM\\Account\\Users\\Names\\{user}")
                flags = winreg.QueryValueEx(subkey, "UserFlags")[0]
                status = "Enabled" if not (flags & 0x2) else "Disabled"
                print(f"{user}: {status}")
                i += 1
            except WindowsError:
                break
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_user_status()


