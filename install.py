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

print ("Checking if PyQt5 installed")
PyQt5Installed = False
try:
    from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel)
    from PyQt5.QtCore import Qt

    PyQt5Installed = True
    print ("PyQt5 installed")

except ImportError:
    print ("PyQt5 is not installed. Install it ?(y/n)")
    ans = getch()

    if ans == ("y" or "Y"):
        print ("\nInstalling PyQt5.....\n")
        sub.call ("sudo apt-get install python3-pyqt5".split())
        try:
            from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel)
            from PyQt5.QtCore import Qt
            PyQt5Installed = True
            print ("\nPyQt5 successfully installed\n")
        
        except ImportError:
            print ("There was an error installing PyQt5. Try again later.")
            sys.exit(1)
    else:
        print ("Exiting...")
        sys.exit(1)

class Window (QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui (self):
		self.WelcomeLabel = QLabel ("Welcome!")

		self.VBox = QVBoxLayout()

		self.VBox.addWidget (self.WelcomeLabel)

		self.setLayout(self.VBox)
		self.setWindowTitle("Vigiliant Euphoria")

		self.show()

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())