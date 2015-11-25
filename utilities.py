import os
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn' source:stackexchange

__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

'''
the logic is:
    1. filter out unneeded rows. (header and footer)
    2. delete empty and dirty files
    3. add a header
    2. add the complete date to each row in the day column
    3. merge each station such as "merged_alikianos" in its own directory
    4. add a header file to each merged location.
'''


def filter_out():
    stations = os.listdir('./data')  # not a good idea. i should be able to choose the location
    for station_i in range(len(stations)):
        dates = os.listdir('./data/'+stations[station_i])  # iterate over the stations
        for j in range(len(dates)):
            data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'r', encoding='cp737')
            data_file_content = data_file.readlines()
            data_file.close()
            index_of_dash = []
            for i, line in enumerate(data_file_content):
                if '-' in line:
                    index_of_dash.append(i)
            if len(index_of_dash) == 0:
                pass
            elif len(index_of_dash) == 4:
                useful_content = data_file_content[index_of_dash[1]+1:index_of_dash[2]]
                data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w', encoding='cp737')
                data_file.writelines(useful_content)
                data_file.close()
            else:
                useful_content = data_file_content[index_of_dash[0]+1:index_of_dash[1]]
                data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w', encoding='cp737')
                data_file.writelines(useful_content)
                data_file.close()


def remove_empty_and_dirty_files():
    stations = os.listdir('./data')
    for station in stations:
        dates = os.listdir('./data/' + station)
        for date in dates:
            try:  # try to read it
                f = open('./data/' + station + '/' + date)
                lines = f.readlines()
                f.close()
                if len(lines) == 0:
                    print('deleting empty data files: ', date)
                    os.remove('./data/' + station + '/' + date)
            except:
                print('CANNOT DECODE DATA WHEN OPENING FILE WITHOUT SPECIFYING ENCODING (it should there are '
                      'only numbers', './data/' + station + '/' + date)
                os.remove('./data/' + station + '/' + date)  # instead of deleting move them to a discard directory


def convert_to_csv_format():
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for date in dates:
            try:
                df = pd.read_csv('./data/' + station + '/' + date, delim_whitespace=1,header=None)
                df.to_csv('./data/' + station + '/' + date,header = None,index=None)
            except:
                for i in np.arange(1,31,1):
                    try:
                        df = pd.read_csv('./data/' + station + '/' + date, skiprows=i,
                                         delim_whitespace=1,header=None)
                        df.to_csv('./data/' + station + '/' + date,header = None,index=None)
                        break
                    except:
                        print('complete failure')


def add_header_to_all_dayly_files():
    default_header = pd.read_csv('default_data_header.txt',header=None)[0].values
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for date in dates:
            df = pd.read_csv('./data/' + station + '/' + date, header=None)
            df.to_csv('./data/' + station + '/' + date,header = default_header,index=None)


def fill_in_empty_days_with_nan():
    pass


def add_complete_dates_location_station(location_geo='crete'):
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for i, date in enumerate(dates):
            data_df = pd.read_csv('./data/' + station + '/' + date)
            empty_dfs = pd.DataFrame(np.zeros((data_df.shape[0], 2)))
            data_df = pd.concat([empty_dfs, data_df], axis=1)
            data_df.columns = ['location', 'station'] + list(data_df.columns.values)[2:]  # just change two first two 
            data_df['location'] = location_geo
            data_df['station'] = station
            for i, day in enumerate(data_df['date']):
                if len(str(data_df['date'][i])) == 1:
                    data_df['date'][i] = date[-11:-4]+'-0'+str(data_df['date'][i])
                else:
                    data_df['date'][i] = date[-11:-4]+'-'+str(data_df['date'][i])
            data_df.to_csv('./data/' + station + '/' + date, index=None)


def merge_all_files_within_a_station(delete_originals=False):
    for station in os.listdir('./data'):
        files = os.listdir('./data/'+station)
        f = open('./data/' + '/' + station + '/' + 'merged_'+station+'.txt', 'w')
        for fi in files:
            lines = open('./data/' + '/' + station + '/'+fi).readlines()[1:]
            for i in range(len(lines)):
                f.write(lines[i])
        f.close()
        if delete_originals:
            for fi in files:
                os.remove('./data/' + '/' + station + '/'+fi)
        else:
            pass


def add_header_to_merged_files():
    new_data_header = pd.read_csv('new_data_header.txt',header=None)[0].values
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        file = pd.read_csv('./data/'+station+'/'+'merged_'+station+'.txt', header=None)
        file.to_csv('./data/'+station+'/'+'merged_'+station+'.txt', header=new_data_header, index=None)





# http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list






























