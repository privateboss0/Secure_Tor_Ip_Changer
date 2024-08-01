#This is built on top of the Tor network to allow
#for a private, secure, and continous random allocation of tor ip addresses to 
#facilitate an anonymous browsing experience on the internet from the network level

import time
import os
import subprocess
import re
from bs4 import BeautifulSoup

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')

try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def tor_ip():
    url = 'https://check.torproject.org'
    try:
        response = requests.get(url,proxies=dict(https='socks5://127.0.0.1:9050'))
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            ip_element = soup.find(string=re.compile(r'Your IP address appears to be'))

            if ip_element:
                ip_address = ip_element.find_next('strong').text.strip()
                return ip_address
            else:
                print("Failed to find IP address in HTML")
                return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def tor_ip_changer():
    os.system("service tor reload")
    tor_ip_text = tor_ip()
    if tor_ip_text:
        print(f'[+] You are connected to Tor!. New Tor IP is: {tor_ip_text}')
    else:
        print('[+] You might be disconnected. Check your connection as I failed to fetch a new Tor IP')


print('''\033[1;32;31m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
            SECURE           Version 7.6
from Nero
''')

print("\033[1;40;34m https://github.com/privateboss0/\n")

os.system("service tor start")

time.sleep(3)
print("\033[0;32;32m change the proxy socks5 in your browser to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] time to change Ip in Secs [type=67] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
if int(lin) ==int(0):

        while True:
                try:
                        time.sleep(int(x))
                        tor_ip_changer()
                except KeyboardInterrupt:

                        print(' Ifa Tor session has ended ')
                        quit()

else:
        for i in range(int(lin)):
                    time.sleep(int(x))
                    tor_ip_changer()
