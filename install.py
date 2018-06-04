import subprocess as sub
import sys, tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print ("Running sudo apt-get update")
sub.call ("sudo apt-get update".split())

print ("Running sudo apt-get upgrade")
sub.call ("sudo apt-get upgrade".split())

print ("Installing pip")
sub.call ("sudo apt-get install python3-pip")

print "\nInstalling virtualenv\n"
sub.call("sudo pip3 install virtualenv".split())

print "\nChanging Directory to home\n"
sub.call("cd".split())

print "\nMaking Vigilant-Euphoria-Server directory\n"
sub.call("mkdir Vigilant-Euphoria-Server".split())

print "\nChanging dir to Vigilant-Euphoria-Server\n"
sub.call("cd Vigilant-Euphoria-Server".split())

print "\nCreating virtual environment\n"
sub.call ("virtualenv flask-env".split())

print "\nActivating virtual environment\n"
sub.call ("source flask-env/bin/activate".split())

print "\nInstalling flask\n"
sub.call ("pip install Flask".split())

