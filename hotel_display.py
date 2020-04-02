
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from copy import deepcopy as dc
IMAGE_FOLDER = "./images"


class HotelDisplay(QtWidgets.QMainWindow):
    user_selection_sig = QtCore.pyqtSignal()
    close_window_sig = QtCore.pyqtSignal()
    confirmation_sig = QtCore.pyqtSignal()

    def __init__(self, country=None, city=None):
        super(HotelDisplay, self).__init__()
        self.setObjectName("display_hotel_win")
        self.setFixedWidth(700)
        self.setMinimumHeight(600)
        self.hotel_location = [country, city]
        self.data_to_display = []
        self.setup_ui()

    def __repr__(self):
        return 'HotelDisplay({0.country!r}, {0.city!r})'.format(self)

    @property
    def hotel_info(self):
        return self._hotel_location

    @hotel_info.setter
    def hotel_info(self, hotel_location):
        self._hotel_location = []
        for k in hotel_location:
            if k is not None:
                if isinstance(k, str):
                    self._hotel_location.append(k)
                else:
                    raise TypeError("In valid argument format. Use string")

    def setup_ui(self):
        self.setWindowTitle("Select Hotel")
        self.scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        self.setCentralWidget(self.scrollArea)
        self.content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.content_widget)
        self._vlay = QtWidgets.QVBoxLayout(self.content_widget)
        self.frame = QtWidgets.QFrame(self.content_widget)
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

        self._vlay.addWidget(self.frame)
        self.filter_pb = QtWidgets.QPushButton(self.content_widget)
        self.filter_pb.setMinimumWidth(700)
        self.filter_pb.setMinimumHeight(50)
        self.filter_pb.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.filter_pb.setStyleSheet("QFrame {background-color: #005500}")
        self.filter_pb.setFont(QtGui.QFont("Times", 15, QtGui.QFont.Bold))
        self.filter_pb.setText("Click for filtering options")
        self._vlay.addWidget(self.filter_pb)
        self.img_count = 0
        self._timer = QtCore.QTimer(self, interval=1)
        self._timer.timeout.connect(self.on_timeout)
        self._timer.start()
        self.files_it = iter([])
    #     self.filter_pb.clicked.connect(self.filter_disp)
    # #
    # #
    # def filter_disp(self):
    #     self.s

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close_window_sig.emit()
        self.showMinimized()
    # The controller should display the hotel names after getting the number of availability from
    # the database

    def display_hotels(self, num_bookings, available_df, filters=None):
        # construct_data creates a dict which stores the user selections and uses it to
        # display info with the images
        self.user_booking = []
        user_selection_dict, room_count = self._construct_data(available_df, filters)
        self.frame_label.setText("Showing results: " + str(room_count))
        # self.frame_label.setText("Showing results " + str(len(user_selection_dict)))
        img_folder_path = self._create_img_folder_path()
        image_list = [file for file in os.listdir(img_folder_path)]
        hotel_room_dict = user_selection_dict[self.hotel_location[1]]
        for hotel_names, room_types in hotel_room_dict.items():
            if 'distance' in room_types:
                self.distance = QtWidgets.QLabel(self.content_widget)
                self.distance.setText(str(room_types['distance']) + "KM")
            str_hotel_names = hotel_names.replace(" ", "").lower()
            hotel_image = ""
            for file_i in image_list:
                image_name, extn = file_i.split(".")
                if image_name == str_hotel_names:
                    hotel_image = file_i
                    break
            if hotel_image is not None and hotel_image is not "":
                image_path = os.path.join(img_folder_path, hotel_image)
                pixmap = QtGui.QPixmap(image_path)
                pixmap = pixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
                for rooms, price in room_types.items():
                    if rooms != 'distance':
                        for price_i in price:
                            if type(price_i) is list:
                                self._add_pixmap(pixmap, hotel_names, rooms, price_i[0], filters)
                            else:
                                self._add_pixmap(pixmap, hotel_names, rooms, price_i, filters)
            else:
                return 0
        return self.user_booking

    def _create_img_folder_path(self):
        import os
        path = IMAGE_FOLDER
        if 0 < len(self.hotel_location) < 4:
            for i in self.hotel_location:
                if i is not None:
                    path = os.path.join(path, i.replace(" ", ""))
            return path
        else:
            print("Less arguments passed")

    def on_timeout(self):
        try:
            self.img_count += 1
        except StopIteration:
            self._timer.stop()

    def _add_pixmap(self, pixmap, hotel_names, room_type, price, filters=None):
        if not pixmap.isNull():
            hspacer = QtWidgets.QSpacerItem(120, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
            img_txt_pb_hlyt = QtWidgets.QHBoxLayout(self.content_widget)
            hotel_details_vlyt = QtWidgets.QVBoxLayout(self.content_widget)
            gb_hotel_details = QtWidgets.QGroupBox(self.content_widget)
            gb_final = QtWidgets.QGroupBox(self.content_widget)
            select_pb_button = QtWidgets.QPushButton(self.content_widget)

            # Creating a label to add an image over it
            image_label = QtWidgets.QLabel(pixmap=pixmap)

            # Adding the image to the horizontal layout, which will be aligned horizontally with
            # the push button and the hotel details
            img_txt_pb_hlyt.addWidget(image_label)

            # Creating an area to show the details for the hotels, vertically layout
            # label city
            label_city = QtWidgets.QLabel(self.content_widget)
            label_city.setText(self.hotel_location[1])
            # label hotel name
            label_hotel_name = QtWidgets.QLabel(self.content_widget)
            label_hotel_name.setText(hotel_names)

            # label room type
            label_room_type = QtWidgets.QLabel(self.content_widget)
            label_room_type.setText(room_type)

            # label price
            label_price = QtWidgets.QLabel(self.content_widget)
            label_price.setText("$" + str(price))

            # Adding all the text labels into the vertical layout
            hotel_details_vlyt.addWidget(label_city)
            hotel_details_vlyt.addWidget(label_hotel_name)
            hotel_details_vlyt.addWidget(label_room_type)
            hotel_details_vlyt.addWidget(label_price)
            # distance;
            if filters is not None and filters != "" and filters == 'distance':
                hotel_details_vlyt.addWidget(self.distance)
            # Adding the layout having hotels details to the group box to be further added to another layout
            # We need a widget to be added to the layout, not a layout to layout. Code will throw erro.
            gb_hotel_details.setLayout(hotel_details_vlyt)

            # Push button for selection and its connecting slot
            select_pb_button.setText("Select")
            select_pb_button.clicked.connect(lambda: self.selected_hotel_data(label_hotel_name.text(),
                                                                              label_city.text(),
                                                                              label_price.text(),
                                                                              label_room_type))
            # Concatenating img hotel_detail and push button horizontally
            img_txt_pb_hlyt.addWidget(gb_hotel_details)
            img_txt_pb_hlyt.addWidget(select_pb_button)
            img_txt_pb_hlyt.addItem(hspacer)
            gb_final.setLayout(img_txt_pb_hlyt)
            self._vlay.addWidget(gb_final)

    def _construct_data(self, available_df, filters=None):
        room_count = 0
        city_dict, hotel_dict = {}, {}
        if filters == 'distance' or filters == 'prices':
            available_df.sort_values(by=[filters], inplace=True)
        hotel_names = set(available_df['hotel_names'])
        for hotel_i in list(hotel_names):
            room_dict = {}
            hotel_df = available_df[(available_df['hotel_names'] == hotel_i)]

            if filters == 'transportation' or filters == 'kids':
                hotel_df = hotel_df[(hotel_df[filters] == 'yes')]

                # hotel_dict['distance'] = distance
            room_types = list(hotel_df['room_type'])
            for room_type_i in room_types:
                room_df = hotel_df[(hotel_df['room_type'] == room_type_i)
                                       & (hotel_df['hotel_names'] == hotel_i)]
                price = list(room_df['prices'])
                room_count += 1
                if room_type_i in room_dict:
                    room_dict[room_type_i].append(price)
                else:
                    room_dict[room_type_i] = price
            if filters == 'distance' and 'distance' in hotel_df:
                distance = list(hotel_df['distance'])[0]
                room_dict['distance'] = distance
            hotel_dict[hotel_i] = dc(room_dict)
        # hotel_dict =  self.sort_dict(filters, hotel_dict)
        city_dict[self.hotel_location[1]] = dc(hotel_dict)
        return city_dict, room_count

    def selected_hotel_data(self, hotel_name, city, price, room_type):
        self.user_booking = [hotel_name, city, price, room_type]
        self.confirmation_sig.emit()

    def sort_dict(self, filters, dict):
        from collections import OrderedDict
        return


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = HotelDisplay("Canada", "Montreal")
    rooms = {'single': 200, 'double': 400, 'family': 600}
    #w._display_content()
    w.show()
    sys.exit(app.exec_())