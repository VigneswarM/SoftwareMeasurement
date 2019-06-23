#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df_collection = pd.read_csv('jacoco_4.1.csv', error_bad_lines=False)

import matplotlib.pyplot as plt

df_collection.head()


# In[3]:


df_collection.plot(x='Code Complexity', y='Statement Coverage', style='o')

df_collection.plot(x='Code Complexity', y='Branch Coverage', style='o')

plt.scatter(df_collection['Code Complexity'], df_collection['Statement Coverage'])
plt.show()


# In[4]:


df_collection.corr(method ='spearman')

df_collection[['Code Complexity','Statement Coverage']].corr(method ='spearman')

df_collection[['Code Complexity','Branch Coverage']].corr(method ='spearman')


# In[ ]:




