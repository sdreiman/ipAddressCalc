# Asks user for Class A info.  Class A address range is any address starting with "0-"
while True:
        try:
                networks_a = int(input("Enter Class A network bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if networks_a != 8:
                print("Sorry, try 8.")
                continue
        else:
                break
while True:
        try:
                hosts_a = int(input("Enter Class A host bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if hosts_a != 24:
                print("Sorry, try 24.")
                continue
        else:
                break
network_a_adjust = int(networks_a) - 1 # Class A uses the remainder of the first octet to define networks i.e. 7 bits

# Asks user for Class B info.  Class B address range is any address starting with "10-"
while True:
        try:
                networks_b = int(input("Enter Class B network bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if networks_b != 16:
                print("Sorry, try 16.")
                continue
        else:
                break
while True:
        try:
                hosts_b = int(input("Enter Class B host bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if hosts_b != 16:
                print("Sorry, try 16.")
                continue
        else:
                break
network_b_adjust = int(networks_b) - 2 # Class B uses the remainder of the first octet and the whole 2nd octet to define networks i.e. 14 bits

# Asks user for Class C info.  Class C address range is any address starting with "110-"
while True:
        try:
                networks_c = int(input("Enter Class C network bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if networks_c != 24:
                print("Sorry, try 24.")
                continue
        else:
                break
while True:
        try:
                hosts_c = int(input("Enter CLass C host bits:"))
        except ValueError:
                print("Sorry, that's incorrect.")
                continue
        if hosts_c != 8:
                print("Sorry, try 8.")
                continue
        else:
                break
network_c_adjust = int(networks_c) - 3 # Class C uses the remainder of the first octet and the whole 2nd and 3rd octet to define networks i.e 21 bits

# Calculates Class A
network_ips_a = 2 ** int(network_a_adjust) - 2
host_ips_a = 2 ** int(hosts_a) - 2
readable_network_a = '{:,}'.format(network_ips_a) # Separates each set of three numbers with a comma
readable_host_a = '{:,}'.format(host_ips_a) # Separates each set of three numbers with a comma

# Calculates Class B
network_ips_b = 2 ** int(network_b_adjust) - 2
host_ips_b = 2 ** int(hosts_b) - 2
readable_network_b = '{:,}'.format(network_ips_b) # Separates each set of three numbers with a comma
readable_host_b = '{:,}'.format(host_ips_b) # Separates each set of three numbers with a comma

# Calculates Class C
network_ips_c = 2 ** int(network_c_adjust) - 2
host_ips_c = 2 ** int(hosts_c) - 2
readable_network_c = '{:,}'.format(network_ips_c) # Separates each set of three numbers with a comma
readable_host_c = '{:,}'.format(host_ips_c) # Separates each set of three numbers with a comma

print("Total usable Class A network IP addresses " + str(readable_network_a) + ". " + "Total usable Class A host IP addresses " + str(readable_host_a) + ".")
print("Total usable Class B network IP addresses " + str(readable_network_b) + ". " + "Total usable Class B host IP addresses " + str(readable_host_b) + ".")
print("Total usable Class C network IP addresses " + str(readable_network_c) + ". " + "Total usable Class C host IP addresses " + str(readable_host_c) + ".")
