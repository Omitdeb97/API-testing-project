#!/usr/bin/env python
# coding: utf-8

# In[1]:



from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'df52385b-6737-4a9f-af66-e0155aeef416',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[7]:


# Importing pandas library and normalize the data to make all in good dataframe

import pandas as pd

df = pd.json_normalize(data['status'])
df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df

if not os.path.isfile(r'C:\Users\amitd\OneDrive\Documents\Data analysing\python tutorial\API files/API.csv'):
    df.to_csv(r'C:\Users\amitd\OneDrive\Documents\Data analysing\python tutorial\API files/API.csv', header='Columns_name')
else:
    df.to_csv(r'C:\Users\amitd\OneDrive\Documents\Data analysing\python tutorial\API files/API.csv', mode='a', header=False)







# In[4]:


# Allow to see all the rows and columns. 
pd.set_option('display.max.rows', None)
pd.set_option('display.max.columns', None)


# In[ ]:





# In[ ]:





# In[10]:


# Saving data into csv file 
df.to_csv("Crypotocoindata.csv")


# In[ ]:





# In[14]:


pd.read_csv(r'C:\Users\amitd\Crypotocoindata.csv')


# In[ ]:





# In[5]:


# Creating function for appending new dataframe with original datafrage

def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'df52385b-6737-4a9f-af66-e0155aeef416',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    


    

    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')
    df = df.append(df2)    
    
    


# In[6]:


import os
from time import time
from time import sleep


# Using for loop 
for i in range(333):
    api_runner()
    print('Api runner completed')
    # Sleeping print for 60 seconds
    sleep(60)
exit()    
    


# In[ ]:





# In[8]:


df10 = pd.read_csv(r'C:\Users\amitd\OneDrive\Documents\Data analysing\python tutorial\API files/API.csv')
df10


# In[ ]:





# In[ ]:





# In[21]:


# using this to drop a selecting column
df.drop('circulating_supply', axis=1)


# In[11]:


# Coverting scientific numbers into float numbers

pd.set_option('display.float_format', lambda x: '%.3f' %x)


# In[12]:


df10


# In[13]:


# Doing groupby and the mean of name column and quote.USD.percent_change.
df2 = df10.groupby('name')[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df2


# In[ ]:





# In[15]:


df4 = df2.stack()
df4


# In[ ]:





# In[16]:


df5 = df4.to_frame(name='values')
df5


# In[17]:


type(df5)


# In[18]:


df5.count()


# In[19]:


# Creating numeric index
index = pd.Index(range(90))
df6 = df5.reset_index()
df6


# In[22]:


df7 =df6.rename(columns={'level_1': 'USD percentage_change'})
df7           


# In[ ]:





# In[31]:


#Replacing the USD percentage_change all comumns name  
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_1h'],['1h'])
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_24h'],['24h'])
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_7d'],['7d'])
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_30d'],['30d'])
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_60d'],['60d'])
df7['USD percentage_change']=df7['USD percentage_change'].replace(['quote.USD.percent_change_90d'],['90d'])
df7


# In[ ]:





# In[30]:


# Creating visualization using variable of df7 data
import seaborn as sns
import matplotlib.pyplot as mtpl

sns.catplot(x='USD percentage_change',y='values', hue='name', data=df7, kind='point')


# In[24]:


df7.count()


# In[32]:


df


# In[37]:


df12 = df10[['name','quote.USD.price','quote.USD.market_cap_dominance','timestamp']]
df12


# In[38]:


df12.query("name == 'Bitcoin'")


# In[43]:


# Creating lineplot of this df12 data
sns.set_theme(style='whitegrid')
sns.lineplot(x='timestamp',y='quote.USD.price', data=df12)


# In[ ]:




