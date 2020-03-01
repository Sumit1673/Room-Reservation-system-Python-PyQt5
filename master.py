from PyQt5 import QtWidgets
from login import Login
from booking_interface import BookingPage
from user_account import UserAccount


class Controller:
    """ Class which controls all the flow along the CHILLO App."""
    def __init__(self):
        self.login_page = Login()
        self.booking_page = BookingPage()
        self.database = UserAccount()
        self.login_page.switch_window.connect(self.show_booking)
        self.login_page.show()
        self.login_page.btn_submit.clicked.connect(self.check_submission)

    def __repr__(self):
        return "Controller <class>"

    def show_login(self):

        self.login_page.switch_window.connect(self.show_booking)
        self.login_page.show()
        self.login_page.btn_submit.clicked.connect(self.check_submission)

    def check_submission(self):
        valid = False
        print("Validating User")
        user_type = self.login_page.check_user_type()
        if user_type == "Login":
            login_details = self.login_page.get_login_details()
            valid = self.database.validation(login_details[0], login_details[1])
            if valid:
                self.login_page.display_msg("Authentication", "Login Successful")
                self.login_page.switch_window.emit()
            else:
                self.login_page.display_msg("Authentication",
                                            "Login Failed: Invalid Username or Password")
        else:
            register_details = self.login_page.get_register_details()
            valid = self.database.validation(register_details[0], register_details[1])
            if valid is False:
                self.database.register_user(full_name=register_details[3],
                                            email=register_details[2],
                                            username=register_details[0],
                                            password=register_details[1])
                self.login_page.display_msg("Authentication", "Registration Successful")
                self.login_page.switch_window.emit()
            else:
                self.login_page.display_msg("Registration",
                                            "Failed: Details already present")

    def show_booking(self):

        self.login_page.close()
        self.booking_page.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    # controller.show_login()
    sys.exit(app.exec_())


if __name__== '__main__':
    main()