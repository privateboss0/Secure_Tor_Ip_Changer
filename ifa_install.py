import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system

if str(choice) =='Y' or str(choice)=='y':

    run('chmod 700 secureautoTOR.py')
    run('mkdir /usr/share/ifa')
    run('cp secureautoTOR.py /usr/share/ifa/secureautoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/ifa/secureautoTOR.py "$@"')
    with open('/usr/bin/ifa','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/ifa & chmod +x /usr/share/ifa/secureautoTOR.py')
    print('''\n\nCongratulations!. Secure Tor Ip Changer has been sucessfully installed ''')
    print("\nTo start the application type: ***sudo ifa*** in terminal ")
    
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/ifa ')
    run('rm /usr/bin/ifa ')
    print('[!] Secure Tor Ip Changer has been uninstalled successfully')
