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


cidr_bin_array = []
for i in range(4):
    cidr_bin_array.append(cidr_continuous[i * 8: (i+1) * 8])

mask_bin = ""
for i in range(4):
    mask_bin += cidr_bin_array[i]

    if i < 4 - 1: mask_bin += "."

mask_string = ""
for i in range(4):
    mask_string += str(int(cidr_bin_array[i], 2))

    if i < 4 - 1: mask_string += "."

addrs_count = pow(2, (32 - cidr_num)) - 2

given_ip_array = ip[:ip.find("/")].split(".")

print("Mask binary: " + mask_bin)
print("Mask string: " + mask_string)
print()
print("Possible quantity of addresses in the network: " + str(addrs_count))
print()
print("Given IP address: " + str(given_ip_array))
