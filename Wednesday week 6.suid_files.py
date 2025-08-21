#coding challenge: Objective: Write a Python script to list SUID files, reinforcing permission audits.
#Task:
#Script to:
#Take a directory path (e.g., /usr/bin).
#List files with SUID bit set.
#Print file paths.
#Hints:
#Use os.walk, os.stat, stat.S_ISUID.


import os

path = "/usr/bin"
print("SUID files in:", path)

for name in os.listdir(path):
    p = os.path.join(path, name)
    if os.path.isfile(p) and (os.stat(p).st_mode & 0o4000):
        print(p)


