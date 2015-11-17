__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

'''
the logic is:
    1. filter out unnedded rows.
    2. add the complete date to each row in the day column
    3. merge each station such as "alikianos" in its own directory
    4. add a header file to each merged location.
'''

import os


def filter_out():
    stations = os.listdir('./data')
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
            else:
                useful_content = data_file_content[index_of_dash[0]+1:index_of_dash[1]]
                data_file = open('./data/'+stations[station_i]+'/'+dates[j], 'w')
                data_file.writelines(useful_content)
                data_file.close()


def add_dates_to_first_column():
    pass


