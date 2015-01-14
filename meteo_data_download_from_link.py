
# coding: utf-8

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



