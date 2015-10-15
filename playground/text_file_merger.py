# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 15:20:29 2014

@author: giorgos
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 04:34:45 2014

@author: giorgos
"""

# coding: utf-8

import os
import pandas as pd

list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou',
'vrysses','heraclion','heraclionwest','heraclionport','ierapetra','lentas',
'metaxochori','moires','paleochora','plakias','pyrathi','rethymno','samaria',
'samariagorge','sitia','spili','sfakia','tzermiado','falasarna','finokalia',
'fourfouras','fragmapotamon','chania','chaniacenter']


def add_dates_and_rename_files_multiple_stations(stations):
    for j in range(len(stations)):
        path = os.path.join(os.getcwd(),list_of_stations_crete[j])        
        files = os.listdir(os.getcwd() + '/' + list_of_stations_crete[j])   
        '''
        this block of code will try the normal way to read from the csv.
        '''
        
        for i in range(len(files)):
            try:
                text = pd.read_csv(os.path.join(path,files[i]), header = None,delim_whitespace = True)
                for line in range(text.shape[0]):                
                    text[0][line] = files[i][len(list_of_stations_crete[j])+1:-24] + '-' + str(text[0][line])            
                os.remove(os.path.join(path,files[i]))
                text.to_csv(os.path.join(path,files[i][:-24] + '-' + 'dates_included.txt'),',',header = None)
            except:
                pass
                
                '''
                stil needs work ill see it in !!!!!
                #if the block above fails we will begin ignoring from the top the lines and we will stop until it is saved.
                f = open(os.path.join(path,files[i]),'r')
                lines = f.readlines()
                f.close()
           
                for n in range(len(lines)):
                    try:
                        text = pd.read_csv(os.path.join(path,files[i]), header = None, delim_whitespace = True,skiprows = n)                                               
                        text = pd.read_csv(os.path.join(path,files[i]), header = None, delim_whitespace = True,skiprows = (n-1)) 
                        for line in range(text.shape[0]):                
                            text[0][line] = files[i][len(list_of_stations_crete[j])+1:-24] + '-' + str(text[0][line])            
                        os.remove(os.path.join(path,files[i]))
                        text.to_csv(os.path.join(path,files[i][:-24] + '-' + 'dates_included.txt'),',',header = None)                        
                        break
                    except:
                        pass
                '''
                pass
    pass

if __name__ == '__main__':
    add_dates_and_rename_files_multiple_stations(list_of_stations_crete)









