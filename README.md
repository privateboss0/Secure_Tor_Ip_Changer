# Secure_Tor_Ip_Changer 7.6

This tool optimizes and secures the change of Onion network IP address every 67seconds. It is built utilizing the Tor project
how to install :

    REQUIREMENTS:
    Ensure you have Tor package installed on your system, if not type:
    
    sudo apt install tor (For Debian based distros)
    sudo apt install python3-regex
    sudo apt install python3-bs4
    
1: git clone https://github.com/privateboss0/Secure_Tor_Ip_Changer

2: cd Secure_Tor_Ip_Changer

3: type [ python3 install.py ]

4: In the cli terminal type [ sudo aut ] from any directory in the terminal to start the program

5: Type the interval to change your Tor IP in seconds to [ 67 ] for stable internet. The lower the seconds the more unstable the connection due to Tor rebulding the secure connection

6: Type how many times you want the IP to change. [ 0 for infinte IP change ]

7: Go to your Tor Browser/PC and change the manual proxy to [ 127.0.0.1:9050 ] from the network settings

8: For Firefox over Tor users, ensure you check the " Proxy DNS when using SOCKS v5 " box
