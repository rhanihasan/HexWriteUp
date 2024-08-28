import getpass
import telnetlib



HOST = "192.168.20.1"  # Replace with your device IP address
user = input("Enter your telnet username: ")  # Changed from raw_input to input for Python 3
password = getpass.getpass()

# Connect to the device
tn = telnetlib.Telnet(HOST)

# Read the "Username" prompt and send the username
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

# If there is a password, read the "Password" prompt and send the password
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Send commands to configure the VLANs
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"end\n")
tn.write(b"copy tftp://192.168.20.2/text.txt flash:\n")
tn.write(b"\n")
#tn.write(b"archive download-sw /leave-old-sw tftp://192.168.20.2/c1000-universalk9-tar.152-7.E10.tar\n")
output = tn.read_until(b"[OK]", timeout=500).decode('ascii')  # Adjust the timeout if necessary
print(output)
tn.write(b"conf t\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"exit\n")




# End configuration mode and close the session
tn.write(b"end\n")
tn.write(b"exit\n")

# Read and print the output from the session
output = tn.read_all().decode('ascii')
print(output)
