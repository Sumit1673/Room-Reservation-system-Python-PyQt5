

__versión__ = "1.0"


from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton)


class Login(QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        
        self.setWindowTitle("Login Page")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 380)

        paleta = QPalette()
        paleta.setColor(QPalette.Background, QColor(200,200,200))
        self.setPalette(paleta)

        self.initUI()

    def initUI(self):

      # ==================== Frame for the Icon and the Title ====================

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

      # ===================== WIDGETS LOGIN ======================

        label_user_type = QLabel("Register or Login", self)
        label_user_type.resize(400, 20)
        label_user_type.move(60, 110)

        self.cmbo_box_user_type = QComboBox(self)
        self.cmbo_box_user_type.addItems(["Login", "Register"])
        self.cmbo_box_user_type.setCurrentIndex(-1)
        self.cmbo_box_user_type.setFixedWidth(280)
        self.cmbo_box_user_type.setFixedHeight(26)
        self.cmbo_box_user_type.move(60, 136)

        label_username = QLabel("Username", self)
        label_username.move(60, 170)

        frame_username = QFrame(self)
        frame_username.setFrameShape(QFrame.StyledPanel)
        frame_username.setFixedWidth(280)
        frame_username.setFixedHeight(28)
        frame_username.move(60, 196)
  #
        image_username = QLabel(frame_username)
        image_username.setPixmap(QPixmap("username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                              Qt.SmoothTransformation))
        image_username.move(10, 4)

        self.line_edit_username = QLineEdit(frame_username)
        self.line_edit_username.setFrame(False)
        self.line_edit_username.setTextMargins(8, 0, 4, 1)
        self.line_edit_username.setFixedWidth(238)
        self.line_edit_username.setFixedHeight(26)
        self.line_edit_username.move(40, 1)

        label_pswd = QLabel("Password", self)
        label_pswd.move(60, 224)

        frame_pswd = QFrame(self)
        frame_pswd.setFrameShape(QFrame.StyledPanel)
        frame_pswd.setFixedWidth(280)
        frame_pswd.setFixedHeight(28)
        frame_pswd.move(60, 250)

        img_pswd = QLabel(frame_pswd)
        img_pswd.setPixmap(QPixmap("password.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                     Qt.SmoothTransformation))
        img_pswd.move(10, 4)

        self.line_edit_pswd = QLineEdit(frame_pswd)
        self.line_edit_pswd.setFrame(False)
        self.line_edit_pswd.setEchoMode(QLineEdit.Password)
        self.line_edit_pswd.setTextMargins(8, 0, 4, 1)
        self.line_edit_pswd.setFixedWidth(238)
        self.line_edit_pswd.setFixedHeight(26)
        self.line_edit_pswd.move(40, 1)

# ================== WIDGETS QPUSHBUTTON ===================

        buttonLogin = QPushButton("Submit", self)
        buttonLogin.setFixedWidth(135)
        buttonLogin.setFixedHeight(28)
        buttonLogin.move(60, 286)

        butn_cancel = QPushButton("Cancel", self)
        butn_cancel.setFixedWidth(135)
        butn_cancel.setFixedHeight(28)
        butn_cancel.move(205, 286)

        # buttonLogin.clicked.connect(self.Login)
        # butn_cancel.clicked.connect(self.close)


# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    fuente.setFamily("Bahnschrift Light")

    aplicacion.setFont(fuente)
    
    ventana = Login()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
