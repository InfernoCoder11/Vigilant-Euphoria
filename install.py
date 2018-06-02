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

def ImportPyQt5():
    import PyQt5

print ("Checking if PyQt5 installed")
Pyqt5Installed = False
try:
    ImportPyQt5()
    Pyqt5Installed = True
    print ("PyQt5 installed")

except ImportError:
    print ("PyQt5 is not installed. Install it ?(y/n)")
    ans = getch()

    if ans == ("y" or "Y"):
        print ("\nInstalling PyQt5.....\n")
        sub.call ("sudo apt-get install python3-pyqt5".split())
        try:
            ImportPyQt5()
            print ("\nPyQt5 successfully installed\n")
        
        except ImportError:
            print ("There was an error installing PyQt5. Try again later.")
            sys.exit(1)
    else:
        print ("Exiting...")
        sys.exit(1)