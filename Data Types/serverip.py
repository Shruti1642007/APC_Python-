server_ip = ("192","168","1","10")
allowed_ips = ["192.168.1.2","192.168.1.3"]

def update_allowed_ips():
    ip = input("Enter new allowed IP:")
    allowed_ips.append(ip)
    print("Allowed IP updated.")

def display():
    print("server IP:",".".join(server_ip))
    print("Allowed IPs:", allowed_ips)

display()        