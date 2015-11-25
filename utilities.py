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


def add_header_to_all():
    default_header = pd.read_csv('data_header.txt',header=None)[0].values
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
            print(round(i/len(dates)*100,2))
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
        df = pd.read_csv('./data/' + '/' + station + '/' + 'merged_'+station+'.txt', header=None)
        header = ['location', 'station'] + list(pd.read_csv('data_header.txt').values)
        df.to_csv('./data/' + '/' + station + '/' + 'merged_'+station+'.txt', index=None, header=header)
        if delete_originals:
            for fi in files:
                os.remove('./data/' + '/' + station + '/'+fi)
        else:
            pass
        

# merge_all_files_within_a_location(delete_originals=1)


# def add_complete_dates_location_station2(location_geo='crete'):
#     stations = os.listdir('./data')
#     for station in stations:
#         dates = os.listdir('./data/' + station)
#         for date in dates:
#             f = open('./data/' + station + '/' + date, encoding='cp737')
#             lines = f.readlines()
#             f.close()
#
#             data_df = pd.read_csv('./data/' + station + '/' + date, header=None, delim_whitespace=True, skip_blank_lines=1)
#             # station_ = []
#             # location_ = []
#             # for s in range(data_df.shape[0]):
#             #     station_.append(station)
#             #     location_.append(location_geo)
#             # for i in range(data_df.shape[0]):
#             #     if len(str(data_df[0][i])) == 1:
#             #         data_df[0][i] = date[-11:-4]+'-0'+str(data_df[0][i])
#             #     else:
#             #         data_df[0][i] = date[-11:-4]+'-'+str(data_df[0][i])
#             # empty_column = np.zeros(data_df.shape[0])
#             # for i, a in enumerate(['geo_location', 'station']):
#             #     data_df.insert(i, a, value=empty_column)
#             # data_df['geo_location'] = location_
#             # data_df['station'] = station_
#             # data_df.to_csv('./data/' + station + '/' + date, index=None, header=None)
#
# # add_complete_dates_location_station2()


# http://stackoverflow.com/questions/1157106/remove-all-occurences-of-a-value-from-a-python-list