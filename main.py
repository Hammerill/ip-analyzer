def binToArray(bin):
    array = ""

    for i in range(4):
        array += bin[i * 8: (i+1) * 8]

        if i < 4 - 1: array += "."

    return array

def binToIp(bin):
    ip = ""

    for i in range(4):
        ip += str(int(bin[i * 8: (i+1) * 8], 2))

        if i < 4 - 1: ip += "."

    return ip

print("Input an IP address like this \"192.168.0.1/16\": ")
ip = input()
print()

cidr_num = int(ip[ip.find("/")+1:])

cidr_continuous = ""
for i in range(32):

    if i < cidr_num:
        cidr_continuous += "1"

    else:
        cidr_continuous += "0"

addrs_count = pow(2, (32 - cidr_num)) - 2

given_ip_array = ip[:ip.find("/")].split(".")
given_ip_bin = []
for i in range(4):
    given_ip_bin.append("{0:08b}".format(int(given_ip_array[i])))

given_ip_continuous = ""
for i in range(4):
    given_ip_continuous += given_ip_bin[i]

server_ip = ""
for i in range(32):

    if i < cidr_num:
        server_ip += given_ip_continuous[i]

    else:
        server_ip += "0"

diffusion_ip = ""
for i in range(32):

    if i < cidr_num:
        diffusion_ip += given_ip_continuous[i]

    else:
        diffusion_ip += "1"

last_ip = ""
for i in range(31):

    if i < cidr_num:
        last_ip += given_ip_continuous[i]

    else:
        last_ip += "1"

last_ip += "0"

first_ip = ""
for i in range(31):

    if i < cidr_num:
        first_ip += given_ip_continuous[i]

    else:
        first_ip += "0"

first_ip += "1"

print("Mask binary: " + binToArray(cidr_continuous))
print("Mask string: " + binToIp(cidr_continuous))
print("Possible quantity of addresses in the network: " + str(addrs_count))
print()
print("Given IP binary: " + binToArray(given_ip_continuous))
print("Given IP string: " + binToIp(given_ip_continuous))
print("\n")
print("Server IP binary: " + binToArray(server_ip))
print("Server IP string: " + binToIp(server_ip))
print()
print("First IP binary: " + binToArray(first_ip))
print("First IP string: " + binToIp(first_ip))
print()
print("Last IP binary: " + binToArray(last_ip))
print("Last IP string: " + binToIp(last_ip))
print()
print("Diffusion IP binary: " + binToArray(diffusion_ip))
print("Diffusion IP string: " + binToIp(diffusion_ip))
print()
