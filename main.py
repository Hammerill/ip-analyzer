def binToArray(bin):
    array = []

    for i in range(4):
        array.append(bin[i * 8: (i+1) * 8])
    
    return array

def binToIp(bin):
    array = binToArray(bin)
    ip = ""

    for i in range(4):
        ip += str(int(array[i], 2))

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

print("Mask binary: " + str(binToArray(cidr_continuous)))
print("Mask string: " + binToIp(cidr_continuous))
print()
print("Possible quantity of addresses in the network: " + str(addrs_count))
print()
print("Given IP address: " + str(given_ip_array))
print("Given IP address in binary: " + str(given_ip_bin))
print()
print("First IP binary: " + str(binToArray(first_ip)))
print("First IP string: " + binToIp(first_ip))
print()
print("Last IP binary: " + str(binToArray(last_ip)))
print("Last IP string: " + binToIp(last_ip))
print()
print("Server IP binary: " + str(binToArray(server_ip)))
print("Server IP string: " + binToIp(server_ip))
print()
print("Diffusion IP binary: " + str(binToArray(diffusion_ip)))
print("Diffusion IP string: " + binToIp(diffusion_ip))
