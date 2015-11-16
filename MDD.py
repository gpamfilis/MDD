__author__ = 'gpamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import shutil
import datetime 
from urllib.request import URLopener
import os, sys
import pandas as pd
import dateutil.relativedelta
from utilities import filter_out

url_seed = "http://penteli.meteo.gr/meteosearch/data/"
data_folder = 'data'


class MeteorologicalDataDownloader(object):

    def __init__(self, year_from, year_to):
        self.year_from = year_from
        self.year_to = year_to
        self.dates_to_download = []
        self.locations = None

    def station_locations(self, station='crete'):
        """
        :rtype : list
        """
        self.locations = pd.read_csv('stations/'+station+'.txt')

    def dates_for_program(self):
        """
        this method will create a dates.txt file where the year and month will
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
        for station in self.locations['stations']:  # add a way to choose the stations

            try:
                os.mkdir(os.path.join(os.getcwd(), data_folder)+'/'+station)
            except:
                # add logging
                print('directory: {} all ready exists!!!'.format(station))
                pass
            testfile = URLopener()
            os.chdir(data_folder + '/' + station)
            print(os.getcwd())
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
    # if not os.path.exists(data_folder):
    #     os.makedirs(data_folder)
    # else:
    #     shutil.rmtree(data_folder)
    #     os.makedirs(data_folder)
    # mdd = MeteorologicalDataDownloader(2000, 2015)
    # mdd.dates_for_program()
    # mdd.station_locations()
    # mdd.download_file_single_location()
    filter_out()

# bibliography:
#  http://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
#  http://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python











