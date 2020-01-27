from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, uic
import login


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([]) #since no command line arguments
    booking_interface = MainWindow()
    font_ = QFont()
    font_.setPointSize(10)
    font_.setFamily("Bahnschrift Light")

    app.setFont(font_)

    myapp = login.Login()
    myapp.show()
    if myapp.flag is True:
        booking_interface.show()
    # booking_interface.show()
    app.exec_()