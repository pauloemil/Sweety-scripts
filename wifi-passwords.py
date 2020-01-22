import subprocess
import re
networks = subprocess.check_output("netsh wlan show profile", shell=True).decode('utf-8')
networks_names = re.findall("(?:Profile\s*:\s)(.*)", networks)
networks_passwords = []
for name in networks_names:
    command = "netsh wlan show profile " + name + " key=clear"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    result = process.stdout.read().decode('utf-8')
    networks_password = re.findall("(?:Key Content\s*:\s)(.*)", result)
    networks_passwords.append(networks_password)
# print(networks_passwords)
for i in range(len(networks_names)):
    password = str(networks_passwords[i])[2:-4]
    print(networks_names[i].strip(), "is:\t", password.strip())
    
# Done at 23/8/2019 6:00 Pm
# get all the passwords stored on your device "windows-only".
