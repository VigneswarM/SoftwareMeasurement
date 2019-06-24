#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import scipy.stats  as stats


# In[ ]:


df = pd.read_csv('https://raw.githubusercontent.com/niravjdn/Software-Measurement-Project/master/data/DD-CC-Churned_Code/Coverage-Statement_Branch-COV-DD%20-%20COV-DD.csv', error_bad_lines=False)


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


is_true = df['Project_Name']=='Math'
df = df[is_true]
df.head()
df['DD'] =  ((df['bugs'] / df['LOC'] )) * 1000
df['Relative_Churned'] =  ((df['Churned_Code'] / df['LOC'] ))


# In[5]:


df.head(25)


# In[6]:


boxplot = df.boxplot(column=['bugs'])


# In[7]:


boxplot = df.boxplot(column=['Relative_Churned'])


# In[8]:


boxplot = df.boxplot(column=['DD'])


# In[9]:


df.plot(x='Relative_Churned', y='DD', style='o')


# In[10]:


df.corr(method ='spearman') 


# In[11]:


df[['Relative_Churned','DD']].corr(method ='spearman')


# In[ ]:


#df.to_csv('data.csv')
#from google.colab import files
#files.download("data.csv")


# In[13]:


df.plot(x='Statement_Coverage', y='DD', style='o')


# In[14]:


df_clean = df.dropna()
stats.spearmanr(df_clean['Statement_Coverage'], df_clean['DD'])


# In[15]:


df[['Statement_Coverage','DD']].corr(method ='spearman')


# In[16]:


df.plot(x='Branch_Coverage', y='DD', style='o')


# In[17]:


df_clean = df.dropna()
stats.spearmanr(df_clean['Branch_Coverage'], df_clean['DD'])


# In[19]:


df[['Branch_Coverage','DD']].corr(method ='spearman')


# In[ ]:




