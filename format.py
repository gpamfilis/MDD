from utilities import convert_to_csv_format, \
    add_header_to_all_dayly_files, \
    add_complete_dates_location_station,\
    merge_all_files_within_a_station, add_header_to_merged_files

if __name__ == '__main__':
    convert_to_csv_format()
    add_header_to_all_dayly_files()
    add_complete_dates_location_station()
    merge_all_files_within_a_station()
    add_header_to_merged_files()
