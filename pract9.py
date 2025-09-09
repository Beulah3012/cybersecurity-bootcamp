read = "/etc/group"

def group_users():
    try:
        with open(read, "r") as p:
            for line in p:
                name = line.split(":")
                group_name = name[0]

    except Exception as e:
        print("placeholder")
                
            
group_users()  
   
