#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import scipy.stats  as stats


# In[91]:


df = pd.read_csv('Tabulated_Metrics.csv', error_bad_lines=False)


# In[92]:


import matplotlib.pyplot as plt


# In[93]:


is_true = df['Project_Name']=='Project 5 - Apache Commons Pool'


# In[94]:


df = df[is_true]


# In[95]:


df.head()


# In[96]:


df['DD'] =  ((df['bugs'] / df['LOC'] )) * 1000


# In[97]:


df['Relative_Churned'] =  ((df['Churned_Code'] / df['LOC'] ))


# In[99]:


df.head(25)


# In[100]:


df.corr(method ='spearman')


# In[101]:


df[['Relative_Churned','DD']].corr(method ='spearman')


# In[102]:


df.plot(x='Statement_Coverage', y='DD', style='o')


# In[103]:


df_clean = df.dropna()


# In[104]:


stats.spearmanr(df_clean['Statement_Coverage'], df_clean['DD'])


# In[105]:


df[['Statement_Coverage','DD']].corr(method ='spearman')


# In[106]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[107]:


df_clean = df.dropna()


# In[108]:


stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[109]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[110]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[ ]:





# In[111]:


df_clean = df.dropna()


# In[112]:


stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[113]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[ ]:





# In[ ]:




