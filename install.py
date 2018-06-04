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

InstallpyDir = os.path.dirname(os.path.realpath(__file__))

print ("Running sudo apt-get update\n")
sub.call ("sudo apt-get update".split())

print ("\nRunning sudo apt-get upgrade\n")
sub.call ("sudo apt-get upgrade".split())

print ("\nInstalling pip\n")
sub.call ("sudo apt-get install python3-pip".split())

print ("\nInstalling virtualenv\n")
sub.call("sudo pip3 install virtualenv".split())

print ("\nChanging Directory to /opt\n")
sub.call("cd /opt".split())

print ("\nMaking Vigilant-Euphoria-Server directory\n")
sub.call("mkdir Vigilant-Euphoria-Server".split())

print ("\nChanging Directory to Vigilant-Euphoria-Server\n")
sub.call("cd Vigilant-Euphoria-Server".split())

print ("\nCreating virtual environment\n")
sub.call ("virtualenv flask-env".split())

print ("\nActivating virtual environment\n")
sub.call ("source flask-env/bin/activate".split())

print ("\nInstalling flask\n")
sub.call ("pip install Flask".split())

