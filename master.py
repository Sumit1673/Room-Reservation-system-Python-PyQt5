from PyQt5 import QtWidgets
from login import Login
from booking_interface import BookingPage
from user_account import UserAccount
from hotel_display import HotelDisplay
from model import DataBase


class Controller:
    """ Class which controls all the flow along the CHILLO App."""

    def __init__(self):
        self.login_page = Login()
        self.booking_page = BookingPage()
        self.database = UserAccount()
        self.login_page.switch_window.connect(self.show_booking)
        self.login_page.show()
        self.login_page.btn_submit.clicked.connect(self.check_submission)
        self.booking_page.check_in_date_sig.connect(self.booking_page.set_date)
        self.booking_page.check_in_date_sig.connect(self.booking_page.verify_checkout_date)
        self.booking_page.room_type_sig.connect(self.booking_page.set_adults_with_room_type)
        self.booking_page.city_changed_sig.connect(self.booking_page.display_hotel)
        self.booking_page.city_changed_sig.connect(self.booking_page.display_room_type)
        # Switch to display hotels
        self.booking_page.ui.view_availability.clicked.connect(self.display_hotels)
        self.booking_page.availability_pb_sign.connect(self.show_hotels)

    def __repr__(self):
        return "Controller <class>"

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

    def display_hotels(self):
        self.get_hotel_availability()
        self.booking_page.availability_pb_sign.emit()

    def show_hotels(self):
        self.booking_page.showMinimized()
        country = self.booking_page.get_country()
        city = self.booking_page.get_city()
        if city and country is not None:            
            self.select_hotel = HotelDisplay(country, city)
            self.select_hotel.close_window_sig.connect(lambda: self.go_back_to_previous_window("display_hotel_win"))
            availability_count, availability_df = self.get_hotel_availability()
            # displaying the images based on count
            # availability_df gives information on whats required. As it contains the filtered
            # data based on user selection.
            user_hotel_confirm = self.select_hotel.display_hotels(availability_count, availability_df)
            self.select_hotel.show()
        else:
            self.booking_page.display_msg("User Input", "Select a country and a city")

    def get_hotel_availability(self):
        user_selection = self.get_user_selection()
        # find any booking for the selected date and city
        data_base = DataBase()
        booked_rooms = data_base.find_hotels_booked(check_in=user_selection['check_in'],
                                                    check_out=user_selection['check_out'],
                                                    city=user_selection['city'], country=user_selection['country'],
                                                    room_type=user_selection['room_type'],
                                                    hotel_name=user_selection['hotel_name'])
        total_available_room = data_base.total_rooms(city=user_selection['city'],
                                                     hotel_name=user_selection['hotel_name'],
                                                     room_type=user_selection['room_type'])

        avail_hotel_room_found = len(total_available_room) - len(booked_rooms)

        return avail_hotel_room_found, total_available_room

    def get_user_selection(self):
        # collecting user selections
        check_in_date, check_out_date = self.booking_page.get_selected_date_period()
        user_selection = {'country': self.booking_page.get_country(), 'city': self.booking_page.get_city(),
                          'check_in': check_in_date, 'check_out': check_out_date,
                          'hotel_name': self.booking_page.get_hotel_name(),
                          'room_type': self.booking_page.get_room_type()}
        return user_selection

    def show_confirmation_page(self):
        pass

    def go_back_to_previous_window(self, sender):
        if sender == 'display_hotel_win':
            print("previous window")
            self.booking_page.show()


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    # controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
