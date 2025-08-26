
import os

path = input("What is the path?")


def list_directory(path):
    items = os.listdir(path)
    try:
    

    for item in items:
        directory = os.path.join(path, item)
        #Here I'm using an if statement to check whether the current item is a directory
        #I pass the full path (stored in directory) into os.path.isdir(), which returns True if it's a folder, and False otherwise.
        #Only if it's True, the code inside the if block will run."
        if os.path.isdir(directory):
            #If the condition is true — meaning the item is a directory — then print(item) displays just the name of that directory.
#Since I'm inside the loop, this happens for every item that passes the check."
            print(item)

        
        

       
    

list_directory(path)



    
    




    
