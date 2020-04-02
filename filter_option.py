import os

from PyQt5 import QtCore, QtGui, QtWidgets


class FilterOption(QtWidgets.QMainWindow):
    filter_windw_sig = QtCore.pyqtSignal()
    filter_btn_sig = QtCore.pyqtSignal()

    def __init__(self):
        super(FilterOption, self).__init__()
        self.setFixedWidth(250)
        self.setMinimumHeight(300)
        self.btn_pressed = ""
        self.show_popup()

    def show_popup(self):
        self.setWindowTitle('Filtering Options')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # self.scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        self._vlay = QtWidgets.QVBoxLayout(self)
        # self.setCentralWidget(self)
        # self.content_widget = QtWidgets.QWidget()
        # self.scrollArea.setWidget(self.content_widget)
        # # self._vlay = QtWidgets.QVBoxLayout(self.content_widget)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setLineWidth(1)
        self.frame.setMinimumWidth(700)
        self.frame.setMinimumHeight(50)
        self.frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.frame.setStyleSheet("QFrame {background-color: #005500}")
        self.frame_label = QtWidgets.QLabel(self.frame)
        self.frame_label.setMinimumHeight(20)
        self.frame_label.setMinimumWidth(100)
        self.frame_label.setStyleSheet("QLabel {color: white}")
        self.frame_label.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.frame_label.setText("Refine your search ....")
        self.transportation = QtWidgets.QPushButton(self)
        self.transportation.setObjectName('transportation')
        self.transportation.move(40, 80)
        # self.transportation.setMinimumWidth(700)
        # self.transportation.setMinimumHeight(50)
        # self.transportation.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.transportation.setStyleSheet("QFrame {background-color: #005500}")
        # self.transportation.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.transportation.setText("Transportation")
        self.transportation.clicked.connect(self.button_pressed)
        self.transportation.setMinimumWidth(180)
        self._vlay.addWidget(self.transportation)
        self.distance = QtWidgets.QPushButton(self)
        self.distance.setObjectName('distance')
        self.distance.clicked.connect(self.button_pressed)
        self.distance.move(40, 130)

        # self.distance.setMinimumWidth(700)
        # self.distance.setMinimumHeight(50)
        self.distance.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.distance.setStyleSheet("QFrame {background-color: #005500}")
        # self.distance.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.distance.setText("Distance \n from downtown")
        self.distance.setMinimumHeight(40)
        self.distance.setMinimumWidth(180)
        self._vlay.addWidget(self.distance)
        self.price = QtWidgets.QPushButton(self)
        self.price.setObjectName('prices')
        self.price.clicked.connect(self.button_pressed)
        self.price.move(40, 190)
        # self.price.setMinimumWidth(700)
        # self.price.setMinimumHeight(70)
        # self.price.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.price.setStyleSheet("QFrame {background-color: #005500}")
        # self.price.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.price.setText("Sort by Price")
        self.price.setMinimumWidth(180)
        self._vlay.addWidget(self.price)
        self.kids = QtWidgets.QPushButton(self)
        self.kids.setObjectName('kids')
        self.kids.clicked.connect(self.button_pressed)
        self.kids.move(40, 240)
        self.kids.setMinimumWidth(180)
        # self.kids.setMinimumWidth(700)
        # self.kids.setMinimumHeight(50)
        # self.kids.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        # self.kids.setStyleSheet("QFrame {background-color: #005500}")
        # self.kids.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.kids.setText("Kids friendly")
        self._vlay.addWidget(self.kids)
        # self.setLayout(self._vlay)

    def button_pressed(self):
        self.btn_pressed = self.sender().objectName()
        self.filter_btn_sig.emit()



if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    c = FilterOption()
    c.show()
    sys.exit(app.exec_())