read_file = "/etc/passwd"
def user_list():
    try:
        with open(read_file, "r") as p:
            for line in p:
                name = line.split(":")
                username = name[0]
                print(username)
    except FileNotFoundError:
        print(f"Error: File '{read_file}' not found")
    except PermissionError:
        print(f"Error: Permission denied for '{read_file}'")
    except Exception as e:
        print(f"Error: {e}")


user_list()
              

            
            


