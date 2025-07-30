#Write a program that:
#Takes a list of IPs (e.g., ["192.168.1.1", "10.0.0.1", "192.168.1.1"]).
#Returns unique, sorted IPs.
#Example output: ["10.0.0.1", "192.168.1.1"]


def sorted_ips(ip_list):
    return sorted(list(set(ip_list)))
ip = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]
print(sorted_ips(ip))



