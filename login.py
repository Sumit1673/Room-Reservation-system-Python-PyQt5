

__versión__ = "1.0"

from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)
from booking_interface import BookingInterface

class Login(QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.flag = 0
        self.setWindowTitle("Login Page")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        self.setFixedSize(400, 380)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(200,200,200))
        self.setPalette(paleta)
        self.user_credential = {'Sumit': '12345', 'Yibo': '11111'}
        self.frame_username = QFrame(self)
        self.frame_full_name = QFrame(self)
        self.frame_email = QFrame(self)
        self.cmbo_box_user_type = QComboBox(self)

        self.label_username = QLabel("Username", self)
        self.label_pswd = QLabel("Password", self)
        self.edit_full_name = QLineEdit(self.frame_full_name)
        self.edit_email = QLineEdit(self.frame_email)

        self.line_edit_username = QLineEdit(self.frame_username)
        self.lbl_full_name = QLabel("Full Name", self)
        self.lbl_email = QLabel("Email", self)

        self.btn_submit = QPushButton("Submit", self)
        self.btn_cancel = QPushButton("Cancel", self)
        self.frame_pswd = QFrame(self)
        self.app_header()
        self.create_forms()

    def __repr__(self):
        return 'Login(Qt Window)'

    def app_header(self):
        palet = QPalette()
        palet.setColor(QPalette.Background, QColor(10, 80, 30))

        # QFrame preserves a space of your size in the main window
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(palet)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)
        frame.move(0, 0)
        #
        label_icon = QLabel(frame)
        label_icon.setFixedWidth(60)
        label_icon.setFixedHeight(60)
        label_icon.setPixmap(QPixmap("icons8-room-service-64.png").scaled(40,40, Qt.KeepAspectRatio,
                                                                          Qt.SmoothTransformation))
        label_icon.move(37, 22)

        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)

        lable_title = QLabel("<font color='white'>CHILLO</font>", frame)
        lable_title.setFont(title_font)
        lable_title.move(183, 20)
        #
        description_font = QFont()
        description_font.setPointSize(9)

        description_label = QLabel("<font color='white'>Hassle free hotel booking.</font>", frame)
        description_label.setFont(description_font)
        description_label.move(150, 46)

    def create_forms(self):
        self.login_form()
        label_user_type = QLabel("Register or Login", self)
        label_user_type.resize(400, 20)
        label_user_type.move(60, 110)
        self.cmbo_box_user_type.addItems(["Login", "Register"])
        self.cmbo_box_user_type.setCurrentIndex(0)
        self.cmbo_box_user_type.setFixedWidth(280)
        self.cmbo_box_user_type.setFixedHeight(26)
        self.cmbo_box_user_type.move(60, 136)
        self.cmbo_box_user_type.currentIndexChanged.connect(self.on_combobox_togl)

    def registration_form(self):

        print("Registeration")
        self.frame_email.show()
        self.frame_full_name.show()
        self.lbl_email.show()
        self.lbl_full_name.show()
        self.setFixedSize(400, 440)

        # Full name --> frame and label
        self.frame_full_name.setFrameShape(QFrame.StyledPanel)
        self.frame_full_name.setFixedWidth(280)
        self.frame_full_name.setFixedHeight(28)
        self.lbl_full_name.move(60, 170)
        self.frame_full_name.move(60, 196)
        image_username = QLabel(self.frame_full_name)
        image_username.setPixmap(QPixmap("username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))
        image_username.move(10, 4)
        self.edit_full_name.setFrame(False)
        self.edit_full_name.setTextMargins(8, 0, 4, 1)
        self.edit_full_name.setFixedWidth(238)
        self.edit_full_name.setFixedHeight(26)
        self.edit_full_name.move(40, 1)

        # Email --> frame and label
        self.frame_email.setFrameShape(QFrame.StyledPanel)
        self.frame_email.setFixedWidth(280)
        self.frame_email.setFixedHeight(28)
        self.lbl_email.move(60, 224)
        self.frame_email.move(60, 250)
        self.edit_email.setFrame(False)
        self.edit_email.setTextMargins(8, 0, 4, 1)
        self.edit_email.setFixedWidth(238)
        self.edit_email.setFixedHeight(26)
        self.edit_email.move(40, 1)

        # Move login form
        self.label_username.move(60, 275)
        self.frame_username.move(60, 300)

        self.label_pswd.move(60, 325)
        self.frame_pswd.move(60, 350)

        self.btn_submit.move(60, 380)
        self.btn_cancel.move(205, 380)

    def on_combobox_togl(self, index):
        if index == 1:
            self.registration_form()
        else:
            self.login_form()

    def login_form(self):
        self.frame_email.hide()
        self.frame_full_name.hide()
        self.lbl_email.hide()
        self.lbl_full_name.hide()
        self.setFixedSize(400, 380)
        self.label_username.move(60, 170)

        self.frame_username.setFrameShape(QFrame.StyledPanel)
        self.frame_username.setFixedWidth(280)
        self.frame_username.setFixedHeight(28)
        self.frame_username.move(60, 196)
        #
        image_username = QLabel(self.frame_username)
        image_username.setPixmap(QPixmap("username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))
        image_username.move(10, 4)
        self.line_edit_username.setFrame(False)
        self.line_edit_username.setTextMargins(8, 0, 4, 1)
        self.line_edit_username.setFixedWidth(238)
        self.line_edit_username.setFixedHeight(26)
        self.line_edit_username.move(40, 1)
        self.label_pswd.move(60, 224)

        self.frame_pswd.setFrameShape(QFrame.StyledPanel)
        self.frame_pswd.setFixedWidth(280)
        self.frame_pswd.setFixedHeight(28)
        self.frame_pswd.move(60, 250)

        img_pswd = QLabel(self.frame_pswd)
        img_pswd.setPixmap(QPixmap("password.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                          Qt.SmoothTransformation))
        img_pswd.move(10, 4)

        self.line_edit_pswd = QLineEdit(self.frame_pswd)
        self.line_edit_pswd.setFrame(False)
        self.line_edit_pswd.setEchoMode(QLineEdit.Password)
        self.line_edit_pswd.setTextMargins(8, 0, 4, 1)
        self.line_edit_pswd.setFixedWidth(238)
        self.line_edit_pswd.setFixedHeight(26)
        self.line_edit_pswd.move(40, 1)

        # ================== WIDGETS QPUSHBUTTON ===================


        self.btn_submit.setFixedWidth(135)
        self.btn_submit.setFixedHeight(28)
        self.btn_submit.move(60, 286)

        self.btn_cancel.setFixedWidth(135)
        self.btn_cancel.setFixedHeight(28)
        self.btn_cancel.move(205, 286)

        self.btn_submit.clicked.connect(self.check_submission)
        # if flag:

        # butn_cancel.clicked.connect(self.close)
    def check_submission(self):
        self.flag = 0
        user_type = str(self.cmbo_box_user_type.currentText())
        user_inp = str(self.line_edit_username.text())
        user_paswd  = str(self.line_edit_pswd.text())
        if user_type == "Login":
            if user_inp in self.user_credential.keys():
                if user_paswd == self.user_credential[user_inp]:
                    self.flag = 1
                    print("Login Successfull")
                    book = BookingInterface()
                    book.show()

        if user_type is "Register":
            if user_inp is not self.user_credential:
                self.user_credential[user_inp] = user_paswd
            else:
                print("user name already exists... !! ")

    def change_window_size(self):
        if str(self.cmbo_box_user_type.currentText()) == "Register":
            self.setFixedSize(400, 500)


if __name__ == '__main__':
    
    import sys
    
    application = QApplication(sys.argv)

    font_ = QFont()
    font_.setPointSize(10)
    font_.setFamily("Bahnschrift Light")

    application.setFont(font_)
    
    myapp = Login()
    
    myapp.show()
    
    sys.exit(application.exec_())
