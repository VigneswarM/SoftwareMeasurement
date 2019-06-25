#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import scipy.stats  as stats


# In[3]:


df_collection = pd.read_csv('jacoco.csv', error_bad_lines=False)


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


df_collection['StatementCoverage'] =  (df_collection['LINE_COVERED'] / (df_collection['LINE_COVERED'] + df_collection['LINE_MISSED'])) * 100


# In[6]:


df_collection['BranchCoverage'] =  (df_collection['BRANCH_COVERED'] / (df_collection['BRANCH_COVERED'] + df_collection['BRANCH_MISSED'])) * 100


# In[7]:


df_collection['CodeComplexity'] =  df_collection['COMPLEXITY_COVERED'] + df_collection['COMPLEXITY_MISSED'];


# In[8]:


df_collection.plot(x='CodeComplexity', y='StatementCoverage', style='o')


# In[9]:


df_collection.plot(x='CodeComplexity', y='BranchCoverage', style='o')


# In[10]:


plt.scatter(df_collection['CodeComplexity'], df_collection['StatementCoverage'])


# In[11]:


plt.show()


# In[12]:


df_collection.corr(method ='spearman')


# In[13]:


df_collection[['CodeComplexity','StatementCoverage']].corr(method ='spearman')


# In[14]:


df_clean = df_collection.dropna()


# In[15]:


stats.spearmanr(df_clean['StatementCoverage'], df_clean['CodeComplexity'])


# In[16]:


df_collection[['CodeComplexity','BranchCoverage']].corr(method ='spearman')


# In[17]:


df_clean = df_collection.dropna()


# In[18]:


stats.spearmanr(df_clean['BranchCoverage'], df_clean['CodeComplexity'])


# In[19]:


print('Statment Coverage '+str((df_collection.LINE_COVERED.sum()/(df_collection.LINE_MISSED.sum() + df_collection.LINE_COVERED.sum()))*100))


# In[20]:


print('Branch Coverage '+str((df_collection.BRANCH_COVERED.sum()/(df_collection.BRANCH_MISSED.sum() + df_collection.BRANCH_COVERED.sum()))*100))


# In[ ]:




