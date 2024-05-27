import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 secureautoTOR.py')
    run('mkdir /usr/share/aut')
    run('cp secureautoTOR.py /usr/share/aut/secureautoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/secureautoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/secureautoTOR.py')
    print('''\n\ncongratulations! Secure Tor Ip Changer has been sucessfully installed \to start type \x1b[6;30;42msudo aut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] Secure Tor Ip Changer has been uninstalled successfully')
