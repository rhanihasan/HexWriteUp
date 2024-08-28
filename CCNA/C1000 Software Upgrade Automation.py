import getpass
import telnetlib
import time

# Set the host address for the switch
HOST = "192.168.20.1"  # Replace with your device IP address

# Get the username and password from the user
user = input("Enter your telnet username: ")  
password = getpass.getpass()

# Connect to the switch using telnet
tn = telnetlib.Telnet(HOST)

# Handle the login prompts
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Send the archive command to download the OS via TFTP
tn.write(b"archive download-sw /leave-old-sw tftp://192.168.20.2/c1000-universalk9-tar.152-7.E10.tar\n")

# Wait for the OS to be downloaded and installed (loop until "All software images installed." is detected)
while True:
    output = tn.read_very_eager().decode('ascii')
    
    # Check if the process has completed
    if "All software images installed." in output:
        print("OS download and extraction completed.")
        break

    # Sleep for a while before checking again
    time.sleep(30)

# Proceed with further configuration after the OS download is complete
tn.write(b"conf t\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"exit\n")

# Validate the boot path and set the new boot system
tn.write(b"show boot\n")
time.sleep(2)  # Give the command time to run
boot_output = tn.read_very_eager().decode('ascii')
print(boot_output)

tn.write(b"boot system flash:/c1000-universalk9-mz.152-7.E10/c1000-universalk9-mz.152-7.E6/c1000-universalk9-mz.152-7.E6.bin\n")
time.sleep(2)

# Save the configuration
tn.write(b"do wr\n")
time.sleep(2)
save_output = tn.read_very_eager().decode('ascii')
print(save_output)

# Reload the switch
tn.write(b"reload\n")
tn.write(b"\n")
time.sleep(2)
tn.write(b"\n")  # Confirm reload if needed
time.sleep(180)  # Wait for the switch to reload (adjust time as needed)

# Close the session after reload
tn.write(b"exit\n")

# Read and print the final output from the session
final_output = tn.read_all().decode('ascii')
print(final_output)

tn.close()
