# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 04:34:45 2014

@author: giorgos
"""

# coding: utf-8

import os
#import pandas as pd

list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou','vrysses','heraclion','heraclionwest','heraclionport','ierapetra','lentas','metaxochori','moires','paleochora','plakias','pyrathi','rethymno','samaria','samariagorge','sitia','spili','sfakia','tzermiado','falasarna','finokalia','fourfouras','fragmapotamon','chania','chaniacenter']
number_of_stations = len(list_of_stations_crete)

#list the contents of the first folder in our CURRENT directory hence the [0]

def correct_and_rename_files(stations):
    for j in range(len(stations)):
        path = os.path.join(os.getcwd(),list_of_stations_crete[j])        
        files = os.listdir(os.getcwd() + '/' + list_of_stations_crete[j])      
        for i in range(len(files)): 
            f = open(os.path.join(path,files[i]))
            lines = f.readlines()
            f.close()
            os.remove(os.path.join(path,files[i]))
            newfile = open(os.path.join(path,files[i][:-4]+'-'+'data_with_no_spaces.txt'),'w')
            for line in lines[11:-10]:
                newfile.write(line)
            newfile.close()
    pass
correct_and_rename_files(list_of_stations_crete)

'''
a = pd.read_csv(os.path.join(path,files[0][:-4]+'-'+'newdata.txt'),header=None,delim_whitespace=True) #header=None,delim_whitespace=True important
#a.to_csv(os.path.join(path,'aaa.txt'),',')
a.to_excel('mew.xlsx')
'''