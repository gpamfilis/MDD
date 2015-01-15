__author__   = 'George Pamfilis'
__version__  = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import datetime 
import dateutil.relativedelta
#with this we will call urllib.URLopener().retrieve(url,file.txt')
#in order to download the webpage to a text
import urllib 
import os
#import sys

current_directory = os.getcwd() #the current directory
urlseed = "http://penteli.meteo.gr/meteosearch/data/"
list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou','vrysses','heraclion','heraclionwest','heraclionport','ierapetra','lentas','metaxochori','moires','paleochora','plakias','pyrathi','rethymno','samaria','samariagorge','sitia','spili','sfakia','tzermiado','falasarna','finokalia','fourfouras','fragmapotamon','chania','chaniacenter']

raw_data_folder = 'Raw_Data'
try:
    os.mkdir(raw_data_folder)
except:
    pass

def dates_for_program(yearnow,yearfrom):
    """
    this function will create a dates.txt file where the year and month will
    be stored from now to then. in a year-month format.
    """
    dates = open("dates.txt","w") #this opens a dates.txt file in write mode
    years = yearnow-yearfrom #number of years between now and then
    for i in range((years-3)*12): #multiply by 12 because of the months in a year i dont know yet why i have to subtract at leat one but anyway 8)
        now = datetime.datetime.now() #this is the datetime of today   
        before = now + dateutil.relativedelta.relativedelta(months = -i)
        dates.write(str(before)[0:7]) #convert the date to a string and remove the day part
        dates.write("\n")
    dates.close()    
    pass

def store_dates_in_list():
    f = open('dates.txt')
    lines = f.readlines()
    f.close()
    return lines

def download_file_single_location(lines,location):
    try:
        os.mkdir(os.path.join(os.getcwd(),raw_data_folder)+'/'+location)
    except:
        pass
    testfile = urllib.URLopener()
    for i in range(len(lines)):   
        name_of_file = os.getcwd()+'/'+raw_data_folder+'/'+location +'/' +location + '-' + lines[i][0:-1] + '.txt'
        try:
            url = urlseed + location + '/' + lines[i][0:-1] + '.txt' #this is the complete url to visit and download its contents
            testfile.retrieve(url,name_of_file)
        except:
            pass
    pass

def main(lines,locations):
    for location in locations:
        print location
        download_file_single_location(lines,location)
    pass

#date_to = str(sys.argv[2])
#date_from = str(sys.argv[1])

if __name__ == "__main__":
    dates_for_program(2014,2000)
    lines = store_dates_in_list()
    main(lines,list_of_stations_crete)         
    
#download_file_single_location(lines[1:50],'aghiosnikolaos')
#download_file_multiple_locations(lines[0:10],list_of_stations_crete[1:1])


















