from downloader import MeteorologicalDataDownloader
from utilities import convert_to_csv_format, \
    add_header_to_all_dayly_files, \
    add_complete_dates_location_station,\
    merge, filter_out_header_and_footer, remove_empty_and_dirty_files,remove_nans

if __name__ == '__main__':
    MeteorologicalDataDownloader().main()
    filter_out_header_and_footer()
    remove_empty_and_dirty_files()
    convert_to_csv_format()
    add_header_to_all_dayly_files()
    add_complete_dates_location_station()
    remove_nans()
    merge()
