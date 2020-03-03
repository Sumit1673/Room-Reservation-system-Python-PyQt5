from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtGui, uic
import pandas as pd


class BookingPage(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Book Hotels ')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.ui = uic.loadUi("interface1.ui", self)
        self.pb_availability.setStyleSheet("background-color: green")
        # self.ui.cal_check_in.clicked[QtCore.QDate].connect(self.showDate)
        # self.ui.cal_check_in.clicked[QtCore.QDate].connect(self.showDate)
        self.init_ui()

    def init_ui(self):

        all_data = self.get_hotel_database()
        if all_data is not None:
            self.display_country(all_data[0])
            self.display_city(all_data[1])
            self.display_hotel(all_data[2])
            self.display_room_type(all_data[3])

    def display_hotel(self, hotel_list):
        completer = QCompleter(hotel_list)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.ledit_hotel.setCompleter(completer)

    def display_city(self, city_list):
        completer = QCompleter(city_list)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.ledit_city_name.setCompleter(completer)

    def display_country(self, country_list):
        completer = QCompleter(country_list)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.ledit_country.setCompleter(completer)

    def display_room_type(self, room_type):
        self.ui.cmbox_room_type.addItems(room_type)
        self.ui.cmbox_room_type.setCurrentIndex(0)

    def select_check_in_out(self):
        pass

    def check_availiability(self):
        pass

    def get_hotel_database(self, col=None):
        try:
            hotel_df = pd.read_csv("city_hotel_database.csv").dropna()
            hotel_database = []
            if col is None:
                for each_col in hotel_df.columns:
                    if each_col == "Country" or "City" or "hotel_names" or "room_type":
                        hotel_database.append(set(hotel_df[each_col]))
                    else:
                        hotel_database.append(hotel_df[each_col])
                return hotel_database
            # use the elif separately to get a data
            elif col in hotel_df.columns:
                return hotel_df[col]
            else:
                print("Invalid data")

        except Exception as e:
            self.display_msg("DataBase Error", "Hotel Database empty")

    def display_msg(self, title, msg):
        QMessageBox.about(self,title, msg)


if __name__ == '__main__':
    app = QApplication([]) #since no command line arguments
    booking_interface = BookingPage()
    font_ = QFont()
    font_.setPointSize(10)
    font_.setFamily("Bahnschrift Light")

    app.setFont(font_)

    # myapp = login.Login()
    booking_interface.show()
    # if myapp.flag is True:
    #     booking_interface.show()
    # # booking_interface.show()
    app.exec_()