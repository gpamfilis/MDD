__author__  = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import datetime 
import dateutil.relativedelta
import urllib 
import os

current_directory = os.getcwd() #the current directory
url_seed = "http://penteli.meteo.gr/meteosearch/data/" #this is the main url on which we add on other strings to navigate to the corresponding file
list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou','vrysses',
                          'heraclion','heraclionwest','heraclionport','ierapetra','lentas','metaxochori','moires',
                          'paleochora','plakias','pyrathi','rethymno','samaria','samariagorge','sitia','spili',
                          'sfakia','tzermiado','falasarna','finokalia','fourfouras','fragmapotamon',
                          'chania','chaniacenter']

raw_data_folder = 'Raw_Data'
try:
    os.mkdir(raw_data_folder)
except:
    pass


class MeteorologicalDataDownloader():
    def __init__(self, year_from, year_to):
        self.year_from = year_from
        self.year_to = year_to
        self.dates_to_download = []

    def dates_for_program(self):
        """
        this function will create a dates.txt file where the year and month will
        be stored from now to then. in a year-month format.
        """
        years = self.year_to - self.year_from  # number of years between now and then
        for i in range((years-3)*12):
            now = datetime.datetime.now()
            before = now + dateutil.relativedelta.relativedelta(months=-i)
            self.dates_to_download.append(str(before)[0:7])

        return self.dates_to_download


def download_file_single_location(lines, location):
    '''
    this function will visit a url for a specific loacation,enter the date
    and save the file to a specified directory
    '''    
    
    try:
        os.mkdir(os.path.join(os.getcwd(),raw_data_folder)+'/'+location)
    except:
        pass
    testfile = urllib.URLopener()
    for i in range(len(lines)):   
        name_of_file = os.getcwd()+'/'+raw_data_folder+'/'+location + '/' +location + '-' + lines[i][0:-1] + '.txt'
        try:
            url = url_seed + location + '/' + lines[i][0:-1] + '.txt' #this is the complete url to visit and download its contents
            testfile.retrieve(url,name_of_file)
        except:
            pass
    pass

def main(lines,locations):
    '''
    this function will perform the same operation as download_file_single_location
    but ovwr multiple location for a specified area.
    '''
    for location in locations:
        print location
        download_file_single_location(lines,location)
    return None 

if __name__ == "__main__":
    lines = MeteorologicalDataDownloader(2005, 2015).dates_for_program()
    print lines[1]


    #main(lines, list_of_stations_crete)
    















