
# coding: utf-8

# In[1]:

def parse_file():
    data=[]
    with open ('database.csv', 'r' ) as f:
        hearder= f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                print('broke_out')
                break
            #up to the tenth line
            field=line.split(",")
            entry={}
            for i, value in enumerate(field):
                entry[hearder[i].strip()]= value.strip()
                data.append(entry)
                counter +=1 
        return data


# In[2]:


doc_data = parse_file()


# In[3]:

doc_data


# In[5]:

all_magnitudes = {}

max_key = 0
max_mag = 0
for i, document in enumerate(doc_data):
    magnitude = document['Magnitude']
    if ( magnitude > max_mag):
        max_key = i
        max_mag = magnitude
    all_magnitudes[i]=(document['Magnitude'])


# In[6]:

max_key


# In[7]:

doc_data[max_key]


# In[8]:

all_magnitudes


# In[9]:

doc_data[20]


# In[10]:


from datetime import date, timedelta
 #Find all the datea between
d1 = date( 1965,2,1)  # start date
d2 = date(2016,12,30)  # end date

delta = d2 - d1         # timedelta

for i in range(delta.days + 1):
    print(d1 + timedelta(days=i))


# In[11]:

doc_data = parse_file()


# In[12]:

#Find all the date
import pandas as pd

#Tabular format data
tab_data = pd.read_csv('database.csv')


# In[13]:

tab_data


# In[14]:

tab_data.Magnitude


# In[15]:


tab_data.groupby(['Date','Depth'])['Magnitude'].max()
#DataFrame.loc[DataFrame['Magnitude'].idmax()]





# In[17]:

max_series = tab_data['Magnitude']


# In[18]:


max_row = max_series.idxmax()


# In[19]:

tab_data.ix[max_row]


# In[20]:


tab_data[['Date','Depth', 'Magnitude']].ix[max_row]


# In[21]:

df = pd.read_csv('database.csv')


# In[22]:

type(df)


# In[23]:

DataFrame = pd.read_csv('database.csv')


# In[24]:

DataFrame


# In[25]:

# import matplotlib.pyplot as plt
# %matplotlib inline


# tab_data = pd.read_csv('database.csv',index_col='Magnitude')
# tab_data.hist(by=tab_data['Date'])
# tab_data.plt.bar()
# plt.title('Magnitude vs Date')

# plt.show()


# In[ ]:

get_ipython().magic(u'matplotlib inline')

tab_data['Magnitude'].hist()
plt.title('Magnitude vs Date')
#df.plot.scatter(x='Date', y='Magnitude', s=50)


# In[ ]:

import matplotlib.pyplot as plt
histogram.plot


# In[ ]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

tab_data['Magnitude'].hist()
plt.title('Magnitude vs Date')
histogram.plot
#df.plot.scatter(x='Date', y='Magnitude', s=50)


# In[ ]:





# In[ ]:



