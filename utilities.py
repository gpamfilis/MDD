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
    3. merge each location such as "merged_alikianos" in its own directory
    4. add a header file to each merged location.
'''


def filter_out_header_and_footer():
    print('\n FILTERING OUT HEADER AND FOOTER')
    stations = os.listdir('./data')  # not a good idea. i should be able to choose the location
    for station_i in range(len(stations)):
        print(stations[station_i])
        dates = os.listdir('./data/'+stations[station_i])  # iterate over the stations
        for j in range(len(dates)):
            data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'r', encoding='cp737')
            data_file_content = data_file.readlines()[8:-8]
            data_file.close()
            index_of_dash = []
            for i, line in enumerate(data_file_content):
                if '-' in line:
                    index_of_dash.append(i)
            if len(index_of_dash) == 0:
                pass
            if len(index_of_dash) >= 2:
                useful_content = data_file_content[index_of_dash[0]+1:index_of_dash[-1]]
                data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w', encoding='cp737')
                data_file.writelines(useful_content)
                data_file.close()
#             elif len(index_of_dash) == 4:
#                 useful_content = data_file_content[index_of_dash[1]+1:index_of_dash[2]]
#                 data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w', encoding='cp737')
#                 data_file.writelines(useful_content)
#                 data_file.close()
#             else:
#                 useful_content = data_file_content[index_of_dash[0]+1:index_of_dash[1]]
#                 data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w', encoding='cp737')
#                 data_file.writelines(useful_content)
#                 data_file.close()


def remove_empty_and_dirty_files():
    print('\n REMOVING EMPTY AND DIRTY FILES')
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


def remove_single_column_files():
    print('\n CONVERTING TO CSV FORMAT')
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for date in dates:
            pass



def convert_to_csv_format():
    print('\n CONVERTING TO CSV FORMAT')
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
    print('\n ADDING A HEADER TO THE DAYLY FILES')
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
    print('\n ADDING NEW COLUMNS LOCATION, STATION, AND FULL DATE')
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for i, date in enumerate(dates):
            data_df = pd.read_csv('./data/' + station + '/' + date)
            empty_dfs = pd.DataFrame(np.zeros((data_df.shape[0], 2)))
            data_df = pd.concat([empty_dfs, data_df], axis=1)
            data_df.columns = ['location', 'location'] + list(data_df.columns.values)[2:]  # just change two first two
            data_df['location'] = location_geo
            data_df['location'] = station
            for i, day in enumerate(data_df['date']):
                if len(str(data_df['date'][i])) == 1:
                    data_df['date'][i] = date[-11:-4]+'-0'+str(data_df['date'][i])
                else:
                    data_df['date'][i] = date[-11:-4]+'-'+str(data_df['date'][i])
            data_df.to_csv('./data/' + station + '/' + date, index=None)


def remove_nans():
    print('\n REMOVING ANY ROWS WITH NANS')
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        dates = os.listdir('./data/' + station)
        for date in dates:
            data = pd.read_csv('./data/'+station+'/'+date).dropna()
            data.to_csv('./data/'+station+'/'+date, index=None)


def merge():
    new_header = pd.read_csv('new_data_header.txt', header=None)[0].values
    for station in os.listdir('./data/'):
        df_list = []
        for i, date in enumerate(os.listdir('./data/'+station)):
            data_file = pd.read_csv('./data/'+station+'/' + date, skiprows=1, header=None)
            df_list.append(data_file)
        merged_df = pd.concat(df_list, axis=0, ignore_index=1)
        merged_df.to_csv('./data/'+station+'/'+'merged_'+station+'.txt', index=None, header=new_header)


def add_header_to_merged_files():
    print('\n ADDING A HEADER TO THE MERGED FILES')
    new_data_header = pd.read_csv('new_data_header.txt', header=None)[0].values
    stations = os.listdir('./data')
    for station in stations:
        print(station)
        file = pd.read_csv('./data/'+station+'/'+'merged_'+station+'.txt', header=None)
        file.to_csv('./data/'+station+'/'+'merged_'+station+'.txt', header=new_data_header, index=None)





# http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list

#http://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-python-pandas-and-concatenate-into-one-dataframe




























