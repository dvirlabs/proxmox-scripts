from netmiko import ConnectHandler
import re
import subprocess

linux = {
    'device_type': 'linux',
    'ip': 'ip of pve',
    'username': 'username',
    'password': 'password',
    'port': 1111,
    'verbose': True
}
# Connect to the Linux Server
connection = ConnectHandler(**linux)
output = connection.send_command('sudo pct list | tail -n +2') # Get the list of the containers with name and status
pattern = "\d{3}" # Extract the ID of the containers
getConID = re.findall(pattern , output) # List of the containers ID
connection.disconnect()

print("What command do you want to exec? ") # Ask the user for the command

userInput = input("Enter command: ") # Get input of the wanted command witout whitespace
if re.search("^apt install", userInput): # In a case there is a flag in the command
    userInputRex = userInput.replace("apt install" , "") # Extract the "apt install" command and replace it with nothing to get the pkg name
    userInput = 'apt-get -- install ' + ' ' + userInputRex + ' ' + '-y' # pct exec 100 apt-get -- install mc -y
    for container in getConID: # Var that get the value of each container in the list
        execCommand = subprocess.getstatusoutput('pct exec ' + container + ' ' + userInput)

        print("container" + ' ' + container + ':' + ' ' + execCommand[1]) # Print the output of the command
        print("\n")
else:

    for container in getConID: # Var that get the value of each container in the list
        execCommand = subprocess.getstatusoutput('pct exec ' + container + ' ' + userInput)

        print("container" + ' ' + container + ':' + ' ' + execCommand[1]) # Print the output of the command
        print("\n")

print("\n" , "The command was executed successfully on all the containers")
