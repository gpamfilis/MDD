from downloader import MeteorologicalDataDownloader
from utilities import convert_to_csv_format, \
    add_header_to_all_dayly_files, \
    add_complete_dates_location_station,\
    merge_all_files_within_a_station, add_header_to_merged_files, filter_out, remove_empty_and_dirty_files

if __name__ == '__main__':
    MeteorologicalDataDownloader().main()
    filter_out()
    remove_empty_and_dirty_files()
    convert_to_csv_format()
    add_header_to_all_dayly_files()
    add_complete_dates_location_station()
    merge_all_files_within_a_station()
    add_header_to_merged_files()
