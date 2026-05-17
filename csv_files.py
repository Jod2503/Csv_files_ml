#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd


# # Importing a new csv file

# In[8]:


df=pd.read_csv('aug_train.csv')
df


# # Sep parameter

# In[11]:


#usually defaut value of sep is ','(csv files)
# if data is in tsv(tab seperated values) the sep takes a diff value(/t)
# names parameter includes heading of the columns
pd.read_csv('movie_titles_metadata.tsv', sep='\t')


# In[14]:


#to use a heading for these columns
pd.read_csv('movie_titles_metadata.tsv', sep='\t', names=['id','name','year','rating','views','type'])


# # index col_parameter

# In[16]:


pd.read_csv('aug_train.csv')


# In[18]:


#As we have default column(0,1,2...) and enrolee id colums too uniquely identifying
#we can remove default column and replace by any other index column
pd.read_csv('aug_train.csv',index_col='enrollee_id')


# # header parameter

# In[19]:


pd.read_csv('test.csv')


# In[20]:


# if we want to row 0 to be the header, we use header par
pd.read_csv('test.csv', header=1)


# # usecols parameter(important)

# In[23]:


#if we want to select only sepcific cols from the input data, we use this parameter
pd.read_csv('aug_train.csv')


# In[24]:


#if we only want 3 cols 
pd.read_csv('aug_train.csv', usecols=['enrollee_id','experience','city'])


# # Squeeze parameters

# In[33]:


#gives specific column(only 1) from the data extracted(not much used)
pd.read_csv('aug_train.csv', usecols=['enrollee_id']).squeeze()


# # Skiprows/Nrows

# In[36]:


#remove unwanted rows from the data
df=pd.read_csv('aug_train.csv')
df


# In[40]:


pd.read_csv('aug_train.csv',skiprows=[1,3])


# In[41]:


pd.read_csv('aug_train.csv',nrows=100)
#get the first 100 rows


# # dtypes parameter

# In[42]:


# if we want to convert column datatype
pd.read_csv('aug_train.csv')


# In[43]:


# if we want to change datatype of 'target' column(last wala) from float to int
pd.read_csv('aug_train.csv',dtype={'target':int})


# # Handling dates

# In[48]:


#date time are generally stored in a string
#we can convert then into date time data type by parsing
'''Parsing is the process of taking a string of unstructured text or data, analyzing it against a set of rules 
and breaking it down into smaller, readable, and machine-understandable segments.'''
df=pd.read_csv('IPL Matches 2008-2020.csv')
df.info()


# In[50]:


#if we want to change the date column from string
df=pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date'])
df.info()


# # converters

# In[51]:


pd.read_csv('IPL Matches 2008-2020.csv')


# In[55]:


def rename(name):
    if name=='Royal Challengers Bangalore':
        return 'RCB'
    else:
        return name


# In[54]:


rename('Royal Challengers Bangalore')


# In[58]:


#if we want to convert this change in whole data
pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename, 'team2':rename})


# In[ ]:




