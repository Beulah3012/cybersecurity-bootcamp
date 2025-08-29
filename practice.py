import os

items = input("What is the path?")

try:
    for item in os.listdir(items):
        directory = os.path.join(items, item)
        if os.isdir(directory):
            print(item)





        



       
        



