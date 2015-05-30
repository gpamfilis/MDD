__author__  = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import datetime 
import urllib
import os
import pandas as pd
import dateutil.relativedelta


url_seed = "http://penteli.meteo.gr/meteosearch/data/"
raw_data_folder = 'RAW_DATA'

try:
    os.mkdir(raw_data_folder)
except:
    pass


class MeteorologicalDataDownloader(object):

    def __init__(self, year_from, year_to):
        self.year_from = year_from
        self.year_to = year_to
        self.dates_to_download = []
        self.locations = None

    def station_locations(self):
        self.locations = pd.read_csv('Stations/crete_stations.txt')

    def dates_for_program(self):
        """
        this function will create a dates.txt file where the year and month will
        be stored from now to then. in a year-month format.
        """
        years = self.year_to - self.year_from  # number of years between now and then
        for i in range(years*12):
            now = datetime.datetime.now()
            before = now + dateutil.relativedelta.relativedelta(months=-i)
            self.dates_to_download.append(str(before)[0:7])
        return self.dates_to_download

    def download_file_single_location(self):
        """
        this function will visit a url for a specific location, enter the date
        and save the file to a specified directory
        # http://penteli.meteo.gr/meteosearch/data/aghiosnikolaos/2009-11.txt
        """
        for station in self.locations['stations'][:2]:

            try:
                os.mkdir(os.path.join(os.getcwd(), raw_data_folder)+'/'+station)
            except:
                print 'directory: {} all ready exists!!!'.format(station)
                pass
            testfile = urllib.URLopener()
            os.chdir(raw_data_folder + '/' + station)
            print os.getcwd()
            for i, date in enumerate(self.dates_to_download):
                name_to_save_file = os.getcwd() + '/' + station + '-' + date + '.txt'
                try:
                    #  this is the complete url to visit and download its contents
                    url = url_seed + station + '/' + date + '.txt'
                    testfile.retrieve(url, name_to_save_file)

                except:
                    pass
            os.chdir(os.pardir)
            os.chdir(os.pardir)

if __name__ == "__main__":
    mdd = MeteorologicalDataDownloader(2013, 2015)
    mdd.dates_for_program()
    mdd.station_locations()
    mdd.download_file_single_location()



















