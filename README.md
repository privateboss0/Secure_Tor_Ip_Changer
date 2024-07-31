# Secure_Tor_Ip_Changer 7.6

This secure tool optimizes and secures the automated change of Onion IP address preferably every 67seconds to access the Tor network. It is built on top of the Tor project. You can read about it here: https://www.torproject.org/about/history/ . Use RESPONSIBLY and I DO NOT take any responsibility for any misuse of this tool in the TOR network

    REQUIREMENTS:
    Install these required packages for the application to run:
    
    sudo apt install tor
    sudo apt install python3-regex
    sudo apt install python3-bs4

How to install :

    Depending on your system permission setting, you can use home/root.
1: From your ( home/root ) directory type [ git clone https://github.com/privateboss0/Secure_Tor_Ip_Changer ]

2: Go into the directory from ( home/root ) using [ cd Secure_Tor_Ip_Changer ]

3: type [ sudo python3 ifa_install.py ] and follow the prompt [ 'y' for install or 'n' for uninstall ] 

4: In the cli terminal type [ sudo ifa ] from any directory in the terminal to start the application

5: Type the interval to change your Tor IP in seconds to minimum of[ 67 ] for stable internet. The lower the seconds the more unstable the connection due to Tor rebulding the secure connection to frequently

6: Type how many times you want the IP to change. [ 0 for infinte IP change ]

7: Go to your Tor Browser/Firefox Browser and change the manual proxy to [ 127.0.0.1:9050 ] and SOCKSV5 from the network settings

8: For Firefox over Tor users, ensure you check the " Proxy DNS when using SOCKS v5 " box
