#Create user_parser.py.
#Write a program for:
#Dictionary like {"alice": {"ip": "192.168.1.1", "login": "2025-06-20"}}.
#Print users and IPs.
#Example output: alice: 192.168.1.1




users = {
    "alice": {"ip": "192.168.1.1", "login": "2025-06-20"},
    "bob": {"ip": "192.168.1.2", "login": "2025-06-19"},
    "ben": {"ip": "192.168.1.3", "login": "2025-06-20"}
}

for user, data in users.items():
    print(f"{user}: {data['ip']}")


