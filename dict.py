users ={"Gavin": 25, "bob" :30}

#print value for "alice"        
print(users["Gavin"])

#safely get value for "charlie"
print(users.get("charlie", "Not found"))

#add a new user
users["charlie"] = 28

print(users)