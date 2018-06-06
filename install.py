import subprocess as sub
import sys, tty
import termios
import os
import getpass

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

InstallFileDir = os.path.dirname(os.path.realpath(__file__))
CurrentUser = getpass.getuser()

print ("Running sudo apt-get update\n")
sub.call ("sudo apt-get update".split())

print ("\nRunning sudo apt-get upgrade\n")
sub.call ("sudo apt-get upgrade".split())

print ("\nInstalling pip\n")
sub.call ("sudo apt-get install python3-pip".split())

print ("\nInstalling virtualenv\n")
sub.call("sudo pip3 install virtualenv".split())

print ("\nChanging Directory to /opt\n")
os.chdir(os.path.abspath('/opt'))

print ("\nMaking Vigilant-Euphoria-Server directory\n")
sub.call("sudo mkdir Vigilant-Euphoria-Server".split())

print ("\nChanging Directory to Vigilant-Euphoria-Server\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server'))

print ("\nCreating virtual environment\n")
sub.call ("sudo virtualenv flask-env".split())

print ("\nCopying __init__.py\n")
sub.call ("sudo cp {}/Files/__init__.py .".format(InstallFileDir).split())

print ("\nMaking templates directory\n")
sub.call ("sudo mkdir templates".split())

print ("\nChanging directory to templates\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server/templates'))

print ("\nCopying main.html\n")
sub.call ("sudo cp {}/Files/main.html .".format(InstallFileDir).split())

print ("\nChanging to parent directory\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server/'))

print ("\nMaking flask-install.sh executable\n")
sub.call ("chmod +x {}/Files/flask-install.sh".format(InstallFileDir).split())

print ("\nCopying flask-install.sh\n")
sub.call ("sudo cp {}/Files/flask-install.sh .".format(InstallFileDir).split())

print ("\nMaking {} the owner of Vigilant-Euphoria-Server\n".format (CurrentUser))
sub.call ("sudo chown -R {}:{} /opt/Vigilant-Euphoria-Server".format(CurrentUser, CurrentUser).split())

print ("\nInstalling flask in virtual environment\n")
sub.call ("./flask-install.sh".split())