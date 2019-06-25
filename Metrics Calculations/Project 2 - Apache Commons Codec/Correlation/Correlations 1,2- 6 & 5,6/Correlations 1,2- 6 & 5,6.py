#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import scipy.stats  as stats


# In[16]:


df = pd.read_csv('Tabulated_Metrics.csv', error_bad_lines=False)


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


is_true = df['Project_Name']=='Project 2 - Apache Commons Codec'
df = df[is_true]
df.head()
df['DD'] =  ((df['bugs'] / df['LOC'] )) * 1000
df['Relative_Churned'] =  ((df['Churned_Code'] / df['LOC'] ))


# In[19]:


df.head(25)


# In[20]:


boxplot = df.boxplot(column=['bugs'])


# In[21]:


boxplot = df.boxplot(column=['Relative_Churned'])


# In[22]:


boxplot = df.boxplot(column=['DD'])


# In[23]:


df.plot(x='Relative_Churned', y='DD', style='o')


# In[24]:


df.corr(method ='spearman')


# In[25]:


df[['Relative_Churned','DD']].corr(method ='spearman')


# In[26]:


df.plot(x='Statement_Coverage', y='DD', style='o')


# In[27]:


df_clean = df.dropna()
stats.spearmanr(df_clean['Statement_Coverage'], df_clean['DD'])


# In[28]:


df[['Statement_Coverage','DD']].corr(method ='spearman')


# In[29]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[30]:


df_clean = df.dropna()
stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[31]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[ ]:




