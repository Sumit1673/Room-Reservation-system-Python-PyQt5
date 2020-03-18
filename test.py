# import sys
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
#
# #
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.title = "Image Viewer"
#         self.setWindowTitle(self.title)

#
#         # image_num = "Image_" + str(i)
#         label1 = QLabel(self)
#         label1.setText("1")
#         pixmap = QPixmap('ITC.jpg')
#         label1.setPixmap(pixmap)
#         self.set
#         self.resize(pixmap.width(), pixmap.height())
#
#         label = QLabel(self)
#         label.setText("2")
#         label.move(300,300)
#         pixmap1 = QPixmap('t1.jpg')
#         label.setPixmap(pixmap1)
#         self.setCentralWidget(label)
#         self.resize(pixmap1.width(), pixmap1.height())
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# sys.exit(app.exec_())


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QLabel, QComboBox, QLineEdit,
                             QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # url = # ...
        # highlight_dir = url + '\\highlighted'
        image_name = ['ITC.jpg', 't1.jpg', 'jw.jpg' ]

        self.scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        self.setCentralWidget(self.scrollArea)
        content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(content_widget)
        lay = QtWidgets.QVBoxLayout(content_widget)

        for file in image_name:
            pixmap = QtGui.QPixmap(file)
            if not pixmap.isNull():
                label = QtWidgets.QLabel(pixmap=pixmap)
                lay.addWidget(label)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# class Window(QWidget):
#     def __init__(self):
#         super(Window, self).__init__()
#         layout = QHBoxLayout(self)
#         self.label3 = QLabel(self)
#         self.title = QLabel("<font color = 'green'>ITC HOTEL</font")
#         self.pixmap = QPixmap('ITC.jpg')
#         self.label3.setPixmap(self.pixmap)
#         self.label3.setAlignment(Qt.AlignTop)
#         self.title.setMinimumHeight(self.pixmap.height())
#         self.title.setAlignment(Qt.AlignBottom)
#         layout.addWidget(self.label3)
#         layout.addWidget(self.title)
#
#         layout.setSpacing(50)
#         layout.addStretch()
#
#         layout = QHBoxLayout(self)
#         self.label31 = QLabel(self)
#         self.title1 = QLabel("<font color = 'green'>ITC HOTEL</font")
#         self.pixmap1 = QPixmap('jw.jpg')
#         self.label31.setPixmap1(self.pixmap1)
#         self.label31.setAlignment(Qt.AlignBottom)
#         self.title1.setMinimumHeight(self.pixmap1.height())
#         self.title1.setAlignment(Qt.AlignBottom)
#         layout.addWidget(self.label31)
#         layout.addWidget(self.title1)
#
#         layout.setSpacing(50)
#         layout.addStretch()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setGeometry(600, 100, 200, 30)
#     window.show()
#     sys.exit(app.exec_())


