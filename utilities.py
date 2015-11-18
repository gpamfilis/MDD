import os, sys
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn' source:stackexchange

__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

'''
the logic is:
    1. filter out unneeded rows. (header and footer)
    2. delete empty files
    2. add the complete date to each row in the day column
    3. merge each station such as "alikianos" in its own directory
    4. add a header file to each merged location.
'''


def filter_out():
    stations = os.listdir('./data')  # not a good idea. i should be able to choose the location
    for station_i in range(len(stations)):
        dates = os.listdir('./data/'+stations[station_i])  # iterate over the stations
        for j in range(len(dates)):
            # print(dates[j])
            data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'r', encoding='cp737')
            data_file_content = data_file.readlines()
            data_file.close()
            index_of_dash = []
            # print('stuff 1')
            for i, line in enumerate(data_file_content):
                if '-' in line:
                    index_of_dash.append(i)
            # print(len(index_of_dash))
            # print(index_of_dash)
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


def remove_empty_files():
    stations = os.listdir('./data')
    for station in stations:
        dates = os.listdir('./data/' + station)
        for date in dates:
            f = open('./data/' + station + '/' + date)
            lines = f.readlines()
            f.close()
            if len(lines) == 0:
                print('deleting empty data files: ', date)
                os.remove('./data/' + station + '/' + date)


def fill_in_empty_days_with_nan():
    pass


def add_complete_dates_location_station(location_geo='crete'):
    stations = os.listdir('./data')
    for station in stations:
        dates = os.listdir('./data/' + station)
        for date in dates:
            data_df = pd.read_csv('./data/' + station + '/' + date, header=None, delim_whitespace=True)
            station_ = []
            location_ = []
            for s in range(data_df.shape[0]):
                station_.append(station)
                location_.append(location_geo)
            for i in range(data_df.shape[0]):
                if len(str(data_df[0][i])) == 1:
                    data_df[0][i] = date[-11:-4]+'-0'+str(data_df[0][i])
                else:
                    data_df[0][i] = date[-11:-4]+'-'+str(data_df[0][i])
            empty_column = np.zeros(data_df.shape[0])
            for i, a in enumerate(['geo_location', 'station']):
                data_df.insert(i, a, value=empty_column)
            data_df['geo_location'] = location_
            data_df['station'] = station_
            data_df.to_csv('./data/' + station + '/' + date, index=None, header=None)


def merge_all_files_within_a_location(delete_originals=False):
    for location in os.listdir('./data'):
        files = os.listdir('./data/'+location)
        f = open('./data/' + '/' + location + '/' + 'merged_'+location+'.txt', 'w')
        for fi in files:
            lines = open('./data/' + '/' + location + '/'+fi).readlines()
            for i in range(len(lines)):
                f.write(lines[i])
        f.close()
        if delete_originals:
            for fi in files:
                os.remove('./data/' + '/' + location + '/'+fi)
        else:
            pass
        pass

# merge_all_files_within_a_location(delete_originals=1)
