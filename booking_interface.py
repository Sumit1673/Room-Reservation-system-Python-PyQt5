from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtGui, uic
import pandas as pd


import datetime

class hotel:

    def __init__(self, name, city, date, room):
        self.name = name
        self.city = city
        self.date = date
        self.room = room

    def getname(self):
        return self.name

    def getcity(self):
        return self.city

    def getdate(self):
        return self.date

    def getroom(self):
        return self.room


Montreal_jw = hotel('JW Marriott', 'Montreal', datetime.date(2020, 1, 13), 'single')
Montreal_jam = hotel('Jameson', 'Montreal', datetime.date(2020, 4, 22), 'Double')
Toronto_itc = hotel('ITC', 'Toronto', datetime.date(2020, 5, 5), 'Double')
Toronto_noel = hotel('Noel', 'Toronto', datetime.date(2020, 5, 22), 'King')
Van_ramada = hotel('Ramada', 'Vancouver', datetime.date(2020, 6, 19), 'Quad')
Van_hampton = hotel('Hampton', 'Vancouver', datetime.date(2020, 6, 14), 'Single')
Que_royal = hotel('Hotel Royal William', 'Quebec City', datetime.date(2020, 6, 27), 'Double')
Que_univ = hotel('Hotel Universal', 'Quebec City', datetime.date(2020, 7, 10), 'Studio')
New_tree = hotel('Double Tree', 'New York', datetime.date(2020, 7, 8), 'King')
New_central = hotel('The Central Park', 'New York', datetime.date(2020, 7, 25), 'Quad')

my_list = [Montreal_jw, Montreal_jam, Toronto_itc, Toronto_noel, Van_ramada, Van_hampton, Que_royal, Que_univ, New_tree,
           New_central]





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
        self.ui.view_availability.clicked.connect(self.check_availiability(self.ui.ledit_city_name.text(), self.ui.ledit_hotel.text()))
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

    def check_availiability(fname, fcity):
            for x in my_list:
                if fname == x.name():
                    self.window = QtWidgets.QMainWindow()
                    self.label = QLabel()
                    label.setText(x.name)
                    window.show()

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