from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QCompleter
from PyQt5 import QtGui, uic
import pandas as pd
from PyQt5.QtCore import QDate
from datetime import datetime
import calendar


class BookingPage(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)
    check_in_date_sig = QtCore.pyqtSignal()
    room_type_sig = QtCore.pyqtSignal()
    availability_pb_sign = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(BookingPage, self).__init__(parent)
        self.setWindowTitle('Book Hotels ')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint) # Remove maximize button
        self.ui = uic.loadUi("interface1.ui", self)
        self.current_month = datetime.now().month
        self.current_year = datetime.now().year
        self.current_day = datetime.now().day
        self.init_ui()

    def init_ui(self):

        all_data = self.get_hotel_database()
        if all_data is not None:
            self.display_country(all_data[0])
            self.display_city(all_data[1])
            self.display_hotel(all_data[2])
            self.display_room_type(all_data[3])

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.pb_availability.setStyleSheet("background-color: green")
        self.ui.cmbox_room_type.setCurrentIndex(-1)
        self.ui.cal_check_in.setGridVisible(True)
        self.ui.cal_check_out.setGridVisible(True)
        self.ui.cal_check_in.setMinimumDate(QDate(self.current_year, self.current_month,
                                                  self.current_day))
        self.ui.cal_check_in.setMaximumDate(QDate(self.current_year, self.current_month + 1,
                                                  calendar.monthrange(self.current_year,
                                                                      self.current_month)[1]))
        self.ui.cal_check_out.setMinimumDate(QDate(self.current_year, self.current_month,
                                                   self.current_day))
        self.ui.cal_check_out.setMaximumDate(QDate(self.current_year, self.current_month + 1,
                                                   calendar.monthrange(self.current_year,
                                                                       self.current_month)[1]))

        self.ui.cal_check_in.clicked.connect(self.check_in_date_sig)
        self.ui.cal_check_out.clicked.connect(self.check_in_date_sig)
        self.ui.cal_check_out.clicked.connect(self.check_in_date_sig)
        self.ui.cmbox_room_type.currentIndexChanged.connect(self.room_type_sig)

    def get_city(self):
        return self.ui.ledit_city_name.text()

    def get_hotel_name(self):
        return self.ui.ledit_hotel.text()

    def get_country(self):
        return self.ui.ledit_country.text()

    def get_n_adults(self):
        return self.ui.spn_box_adults.Value()

    def get_room_type(self):
        return self.ui.cmbox_room_type.currentText()

    def get_rooms(self):
        return self.ui.spn_box_rooms.Value()

    def set_adults_with_room_type(self):
        room_type = self.ui.cmbox_room_type.currentText().lower()
        if room_type == "double":
            self.ui.spn_box_adults.setMaximum(2)
        if room_type == "conference":
            self.ui.spn_box_adults.setMaximum(60)
        if room_type == "single":
            self.ui.spn_box_adults.setMaximum(1)
        if room_type == "family":
            self.ui.spn_box_adults.setMaximum(4)
        if room_type == "suite":
            self.ui.spn_box_adults.setMaximum(4)

    def set_date(self):
        cal = self.sender()
        self.set_spin_box_date(cal.objectName())
    
    def verify_checkout_date(self):
        cal = self.sender().objectName()
        if cal == 'cal_check_out':
            if self.ui_date_edit_check_in.date() > self.ui_date_edit_check_out.date():
                self.display_msg("Date Error", "Check Out should be ahead of check in date")
            
    def get_selected_date_period(self):
        return self.ui.date_edit_check_in.date(), self.ui.date_edit_check_out.date()

    def set_spin_box_date(self, spin_box_name):
        if spin_box_name == "cal_check_in":
            self.ui.date_edit_check_in.setDate(self.ui.cal_check_in.selectedDate())
        elif spin_box_name == "cal_check_out":
            self.ui.date_edit_check_out.setDate(self.ui.cal_check_out.selectedDate())
        else:
            raise TypeError("Invalid Entry")
    
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
        room_type = [str(room) for room in list(room_type) if str(room) != "nan"]
        self.ui.cmbox_room_type.addItems(room_type)
        self.ui.cmbox_room_type.setCurrentIndex(0)

    def get_hotel_database(self, col=None):
        try:
            hotel_df = pd.read_csv("city_hotel_database.csv")
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
        QMessageBox.about(QMessageBox(), title, msg)


if __name__ == '__main__':
    app = QApplication([])  # since no command line arguments
    booking_interface = BookingPage()
    font_ = QFont()
    font_.setPointSize(10)
    font_.setFamily("Bahnschrift Light")
    app.setFont(font_)
    booking_interface.show()
    app.exec_()
