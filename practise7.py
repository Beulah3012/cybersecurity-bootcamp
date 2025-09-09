import os
import stat

directory = input("What is your directory called? ").strip()
for root, _, files in os.walk(directory):
    for file in files:
        full_path = os.path.join (root, file)
        if os.stat(full_path).st_mode & stat.S_IWOTH:
            print(full_path)

        
            
        

    

