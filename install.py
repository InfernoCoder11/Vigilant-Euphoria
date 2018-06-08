import subprocess as sub
import sys, tty
import termios
import os
import getpass

InstallFileDir = os.path.dirname(os.path.realpath(__file__))
CurrentUser = getpass.getuser()

print ("  Running sudo apt-get update\n")
sub.call ("sudo apt-get update".split())

print ("\n  Running sudo apt-get upgrade\n")
sub.call ("sudo apt-get upgrade".split())

print ("\n  Installing notify-osd for notifications\n")
sub.call ("sudo apt-get install notify-osd".split())

print ("\n  Installing pip\n")
sub.call ("sudo apt-get install python3-pip".split())

print ("\n  Installing virtualenv\n")
sub.call("sudo pip3 install virtualenv".split())

print ("\n  Changing Directory to /opt\n")
os.chdir(os.path.abspath('/opt'))

print ("\n  Making Vigilant-Euphoria-Server directory\n")
sub.call("sudo mkdir Vigilant-Euphoria-Server".split())

print ("\n  Changing Directory to Vigilant-Euphoria-Server\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server'))

print ("\n  Creating virtual environment\n")
sub.call ("sudo virtualenv flask-env".split())

print ("\n  Copying __init__.py\n")
sub.call ("sudo cp {}/Files/__init__.py .".format(InstallFileDir).split())

print ("\n  Making templates directory\n")
sub.call ("sudo mkdir templates".split())

print ("\n  Changing directory to templates\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server/templates'))

print ("\n  Copying main.html\n")
sub.call ("sudo cp {}/Files/main.html .".format(InstallFileDir).split())

print ("\n  Changing to parent directory\n")
os.chdir(os.path.abspath('/opt/Vigilant-Euphoria-Server/'))

print ("\n  Making flask-install.sh executable\n")
sub.call ("chmod +x {}/Files/flask-install.sh".format(InstallFileDir).split())

print ("\n  Copying flask-install.sh\n")
sub.call ("sudo cp {}/Files/flask-install.sh .".format(InstallFileDir).split())

print ("\n  Making {} the owner of Vigilant-Euphoria-Server\n".format (CurrentUser))
sub.call ("sudo chown -R {}:{} /opt/Vigilant-Euphoria-Server".format(CurrentUser, CurrentUser).split())

print ("\n  Installing flask in virtual environment\n")
sub.call ("./flask-install.sh".split())