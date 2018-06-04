import subprocess as sub
import sys, tty
import termios
import os

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

print ("\nActivating virtual environment\n")
sub.call ("sudo source flask-env/bin/activate".split())

print ("\nInstalling flask\n")
sub.call ("sudo pip install Flask".split())

print ("Copying __init__.py")
sub.call ("sudo cp {}/Files/__init__.py .".format(InstallFileDir).split())