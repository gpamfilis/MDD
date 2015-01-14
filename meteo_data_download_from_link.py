
# coding: utf-8

<<<<<<< HEAD
# In[ ]:


import datetime


# In[2]:

import datetime 
import dateutil.relativedelta
dates = open("dates.txt","w")
for i in range((2014-2009)*12):
    now = datetime.datetime.now() 
    before = now + dateutil.relativedelta.relativedelta(months=-i)
    #print str(before)[0:7]
    dates.write(str(before)[0:7])
    dates.write("\n")
dates.close()


#### import urllib testfile = urllib.URLopener() testfile.retrieve(url, "file.txt")

# In[3]:

f = open("dates.txt")
lines = f.readlines()
print len(lines)
f.close()
#dd = lines[11:-10]


# In[6]:

'''
data = open('2006-05.txt','w')
for i in dd:
    data.write(i)
    data.write('\n')
data.close()
#data = lines[11:-10]
'''


# In[ ]:




# In[7]:

'''
import urllib
testfile = urllib.URLopener()

a = open('dates.txt','r')
lines = a.readlines()
lenline = len(lines)
a.close()
    testfile.retrieve('http://penteli.meteo.gr/meteosearch/data/heraclion/'+'2006-05'+'.txt', "file.txt")
'''


# In[8]:




# In[4]:

import urllib
import time
testfile = urllib.URLopener()
for i in range(len(lines)):
    try:
        testfile.retrieve('http://penteli.meteo.gr/meteosearch/data/chaniacenter/'+lines[i][0:-1]+'.txt', lines[i][0:-1]+'.txt')
        #time.sleep(5)
    except:
        pass


# In[128]:

#pd.DataFrame(lines[11:])
#pd.DataFrame.from_csv('file.txt', sep='\t')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[36]:
'''
import urllib

site = urllib.urlopen('http://penteli.meteo.gr/meteosearch/data/heraclion/2006-05.txt')
site_data = site.read()
'''

# In[57]:




# In[37]:




# In[ ]:



=======
import datetime 
import dateutil.relativedelta
#with this we will call urllib.URLopener().retrieve(url,file.txt')
#in order to download the webpage to a text
import urllib 
import os
current_directory = os.getcwd() #the current directory
urlseed = "http://penteli.meteo.gr/meteosearch/data/"
list_of_stations_crete = ['aghiosnikolaos','alikianos','anogeia','askyfou','vrysses','heraclion','heraclionwest','heraclionport','ierapetra','lentas','metaxochori','moires','paleochora','plakias','pyrathi','rethymno','samaria','samariagorge','sitia','spili','sfakia','tzermiado','falasarna','finokalia','fourfouras','fragmapotamon','chania','chaniacenter']

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
        os.mkdir(location) #makes a directory for a location. once it completes the downloading of the files it creates another directory and so on.
        for i in range(len(lines)):
            try:
                testfile.retrieve(urlseed + location + '/' + lines[i][0:-1] + '.txt',current_directory + '/' + location + '/' + location + '-' + lines[i][0:-1] + '.txt')
            except:
                pass
    pass

def download_file_single_location(lines,location):
    os.mkdir(location)
    testfile = urllib.URLopener()
    for i in range(len(lines)):         
        try:
            testfile.retrieve(urlseed+location+'/'+lines[i][0:-1]+'.txt',current_directory+'/'+location+'/'+location+'-'+lines[i][0:-1]+'.txt')
        except:
            pass
    pass

if __name__ == "__main__":
    dates_for_program(2014,2000)
    lines = store_dates_in_list()
    download_file_multiple_locations(lines,list_of_stations_crete)
>>>>>>> d6b42b583204553b14fcea1f7923ac074d16d72a
