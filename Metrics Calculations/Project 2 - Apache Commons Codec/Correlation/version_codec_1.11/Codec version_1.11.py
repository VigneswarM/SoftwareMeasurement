#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df_collection = pd.read_csv('jacoco.csv', error_bad_lines=False)


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


df_collection.head()


# In[6]:


df_collection.plot(x='Code Complexity', y='Statement Coverage', style='o')


# In[7]:


df_collection.plot(x='Code Complexity', y='Branch Coverage', style='o')


# In[8]:


plt.scatter(df_collection['Code Complexity'], df_collection['Statement Coverage'])
plt.show()


# In[9]:


df_collection.corr(method ='spearman')


# In[10]:


df_collection[['Code Complexity','Statement Coverage']].corr(method ='spearman')


# In[11]:


df_collection[['Code Complexity','Branch Coverage']].corr(method ='spearman')


# In[ ]:




