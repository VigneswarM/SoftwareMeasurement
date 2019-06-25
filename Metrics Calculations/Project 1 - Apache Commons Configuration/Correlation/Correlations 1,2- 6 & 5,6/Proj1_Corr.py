#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import scipy.stats  as stats

df = pd.read_csv('Tabulated_Metrics.csv', error_bad_lines=False)

import matplotlib.pyplot as plt


# In[2]:


is_true = df['Project_Name']=='Project 1 - Apache Commons Configuration'
df = df[is_true]
df.head()
df['DD'] =  ((df['bugs'] / df['LOC'] )) * 1000
df['Relative_Churned'] =  ((df['Churned_Code'] / df['LOC'] ))


# In[3]:


df.head()


# In[4]:


boxplot = df.boxplot(column=['bugs'])


# In[5]:


boxplot = df.boxplot(column=['Relative_Churned'])


# In[6]:


boxplot = df.boxplot(column=['DD'])


# In[7]:


df.plot(x='Relative_Churned', y='DD', style='o')


# In[8]:


df.corr(method ='spearman')


# In[9]:


df[['Relative_Churned','DD']].corr(method ='spearman')


# In[10]:


df.plot(x='Statement_Coverage', y='DD', style='o')


# In[11]:


df_clean = df.dropna()


# In[12]:


stats.spearmanr(df_clean['Statement_Coverage'], df_clean['DD'])


# In[13]:


df[['Statement_Coverage','DD']].corr(method ='spearman')


# In[14]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[15]:


df_clean = df.dropna()


# In[16]:


stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[17]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[ ]:




