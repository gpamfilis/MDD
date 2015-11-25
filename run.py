__author__ = 'gpamfilis'

from utilities import convert_to_csv_format, add_header_to_all, add_complete_dates_location_station,merge_all_files_within_a_station

if __name__ == '__main__':

    convert_to_csv_format()
    add_header_to_all()
    add_complete_dates_location_station()
    # merge_all_files_within_a_station()
