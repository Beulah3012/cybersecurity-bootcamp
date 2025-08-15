#Objective: Write a Python script to find files by extension, reinforcing search skills.

#Write a script to: Take a directory and extension (e.g., /home, .txt). List files with the extension. Print full paths. Handle errors.

#Hints: Use os.walk, os.path.join. Run in Kali VM.

#Deliverable: Save as find_files.py, run in Kali VM. Submit script and screenshot of output.
#This was done in the Kali VM and pasted here so that it can be pushed to git hub





import os

folder = "/home/kali"
extension = ".txt"

for root, _, files in os.walk(folder):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))





