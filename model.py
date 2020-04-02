""" Model.py will act as a module which provides the information from the database
based on the user query"""
import pandas as pd
import os
import csv

class DataBase:
    def __init__(self):
        self.hotel_df = pd.read_csv("city_hotel_database.csv")
        self.booking_log_df = pd.read_csv("booking_log.csv")

        self.hotel_df = self.clean_data(self.hotel_df)
        self.booking_log_df = self.clean_data(self.booking_log_df)

    @staticmethod
    def clean_data(data_frame):
        # clean data from any nan values
        missing_cols = [cols for cols in data_frame.columns
                        if data_frame[cols].isnull().any()]
        print(missing_cols)
        data_frame = data_frame.dropna(axis=0, subset=missing_cols)
        return data_frame

    def save_booking(self, booking_id, country, username, _in, out, total_price, n_rooms, user_final_booking):
        city = user_final_booking[1]
        room_type = user_final_booking[3].text()
        log = [country, city, user_final_booking[0], room_type,
               _in, out, n_rooms, total_price, username]
        with open("user_booking_log.csv", 'a', newline="") as log_file:
            log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            log_writer.writerow(log)


    def find_hotels_booked(self, check_in, check_out, city, country=None, room_type=None, hotel_name=None):
        """
        :arg: args contains information about country, city , hotel name, room types
        """
        self.filter_option = {}
        if check_in is not None:
            self.filter_option['check_in'] = str(check_in)
        if check_out is not None:
            self.filter_option['check_out'] = str(check_out)
        if country is not None:
            self.filter_option['country'] = str(country)
        if city is not None:
            self.filter_option['city'] = str(city)
        if room_type is not None:
            self.filter_option['room_type'] = str(room_type)
        if hotel_name is not None:
            self.filter_option['hotel_name'] = str(hotel_name)
        bookings = self._get_bookings_for_date()
        return bookings

    def _get_bookings_for_date(self):
        """:arg
            *args : hotel name if asked to filter out the entries
            if the function return 0 means no booking.
        """
        try:
            if 'check_in' in self.filter_option and self.filter_option['check_in'] is not None:
                if 'check_out' in self.filter_option and self.filter_option['check_out'] is not None:
                    if 'city' in self.filter_option and self.filter_option['city'] is not None:
                        bookings_found = self.booking_log_df[
                            (self.booking_log_df["check_in"] == self.filter_option['check_in'])
                            & (self.booking_log_df["check_out"] == self.filter_option['check_out'])
                            & (self.booking_log_df["city"] == self.filter_option['city'])]

            if 'hotel_name' in self.filter_option and self.filter_option['hotel_name'] is not None:
                bookings_found = self.booking_log_df[
                    (self.booking_log_df["hotel_names"] == self.filter_option['hotel_name'])]

            if 'room_type' in self.filter_option and self.filter_option['room_type'] is not None:
                bookings_found = self.booking_log_df[
                    (self.booking_log_df["room_type"] == self.filter_option['room_type'])]

            if bookings_found.empty:
                return []
            else:
                return bookings_found
        except ValueError as val:
            print(val)

    def total_rooms(self, city, hotel_name=None, room_type=None):
        options = {'city': city, 'hotel_names': hotel_name, 'room_type': room_type}
        if 'city' in options and options['city'] is not None:
            df = self.hotel_df[self.hotel_df['city'] == options['city']]
        if 'hotel_names' in options and options['hotel_names'] is not None \
                and options['hotel_names'] != "":
            df = df[df['hotel_names'] == options['hotel_names']]
        if 'room_type' in options and options['room_type'] is not None \
                and options['room_type'] != "":
            df = df[df['room_type'] == options['room_type']]
        if city is None:
            raise ValueError("Not enough value passed")

        return df

    def verify_filter_option_type(self, options):

        return options


#

if __name__ == "__main__":
    c = DataBase()
    print(c.find_hotels_booked(check_in="2020-02-10", check_out="2020-02-23", city='Montreal'))
