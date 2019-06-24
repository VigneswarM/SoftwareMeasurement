#!/usr/bin/env python
# coding: utf-8

# In[67]:


import pandas as pd
import scipy.stats  as stats


# In[68]:


df = pd.read_csv('Tabulated_Metrics.csv', error_bad_lines=False)


# In[69]:


import matplotlib.pyplot as plt


# In[70]:


is_true = df['Project_Name']=='Project 3 - Apache Commons Collections'


# In[71]:


df = df[is_true]


# In[72]:


df.head()


# In[73]:


df['DD'] =  ((df['bugs'] / df['LOC'] )) * 1000


# In[74]:


df['Relative_Churned'] =  ((df['Churned_Code'] / df['LOC'] ))


# In[75]:


df.head(25)


# In[76]:


df.corr(method ='spearman')


# In[77]:


df[['Relative_Churned','DD']].corr(method ='spearman')


# In[78]:


df.plot(x='Statement_Coverage', y='DD', style='o')


# In[79]:


df_clean = df.dropna()


# In[80]:


stats.spearmanr(df_clean['Statement_Coverage'], df_clean['DD'])


# In[81]:


df[['Statement_Coverage','DD']].corr(method ='spearman')


# In[82]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[83]:


df_clean = df.dropna()


# In[84]:


stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[85]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[86]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[ ]:





# In[87]:


df_clean = df.dropna()


# In[88]:


stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[89]:


df[['Branch_Coverage','DD']].corr(method ='spearman')

