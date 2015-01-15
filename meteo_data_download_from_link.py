__author__   = 'George Pamfilis'
__version__  = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import datetime 
import dateutil.relativedelta
#with this we will call urllib.URLopener().retrieve(url,file.txt')
#in order to download the webpage to a text
import urllib 
import os
current_directory = os.getcwd() #the current directory
urlseed = "http://penteli.meteo.gr/meteosearch/data/"
list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou','vrysses','heraclion','heraclionwest','heraclionport','ierapetra','lentas','metaxochori','moires','paleochora','plakias','pyrathi','rethymno','samaria','samariagorge','sitia','spili','sfakia','tzermiado','falasarna','finokalia','fourfouras','fragmapotamon','chania','chaniacenter']

try:
    os.mkdir('Gross Weather Data')
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
    f = open("dates.txt")
    lines = f.readlines()
    f.close()
    return lines

def download_file_multiple_locations(lines,locations):
    testfile = urllib.URLopener()
    for location in locations:
        os.mkdir(os.path.join(os.getcwd(),'Gross-Weather-Data')+'/'+location)
        print location
        os.mkdir(location) #makes a directory for a location. once it completes the downloading of the files it creates another directory and so on.
        for i in range(len(lines)):
            try:
                url = urlseed + location + '/' + lines[i][0:-1] + '.txt'
                data_location = os.path.join(current_directory,'Gross-Weather-Data')
                location_to_save_and_name_of_file = data_location + '/' + location +'/'+ location + '-' + lines[i][0:-1] + '.txt'
                testfile.retrieve(url,location_to_save_and_name_of_file)
            except:
                pass
    pass

def download_file_single_location(lines,location):
    os.mkdir(os.path.join(os.getcwd(),'Gross Weather Data')+'/'+location)
    testfile = urllib.URLopener()
    for i in range(len(lines)):         
        try:
            url = urlseed + location + '/' + lines[i][0:-1] + '.txt' #this is the complete url to visit and download its contents
            data_location = os.path.join(current_directory,'Gross Weather Data')
            location_to_save_and_name_of_file = data_location + '/' + location +'/'+ location + '-' + lines[i][0:-1] + '.txt'
            testfile.retrieve(url,location_to_save_and_name_of_file)
        except:
            pass
    pass

if __name__ == "__main__":
    dates_for_program(2014,2000)
    lines = store_dates_in_list()
    download_file_multiple_locations(lines[0:10],list_of_stations_crete[1:1])

