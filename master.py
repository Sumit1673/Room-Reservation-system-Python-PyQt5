from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)
from login import Login
from booking_interface import BookingPage


class Controller:
    """ Class which controls all the flow along the CHILLO App."""
    def __init__(self):
        self.login_page = Login()
        self.booking_page = BookingPage()

    def __repr__(self):
        return "Controller Class"

    def show_login(self):

        self.login_page.switch_window.connect(self.show_booking)
        self.login_page.show()

    def show_booking(self):

        self.login_page.close()
        self.booking_page.show()


class UserAccount:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def validation(self):
        pass

    def register_user(self):
        pass

    def delete_user(self):
        pass


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__== '__main__':
    main()