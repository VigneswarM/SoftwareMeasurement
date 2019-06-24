#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_columns', None)


# In[2]:


df = pd.read_csv('mutations.csv', error_bad_lines=False, names = ["Class", "Package", "gc1", "gc2","gc3","Coverage","gc4"])


# In[3]:


df.drop('gc1', axis=1, inplace=True)
df.drop('gc2', axis=1, inplace=True)
df.drop('gc3', axis=1, inplace=True)
df.drop('gc4', axis=1, inplace=True)
df['Package'] = df['Package'].map(lambda x: str(x)[:x.rfind('.')])
df['Package'] = df['Package'].map(lambda x:  x if (x.find('$')+1 == 0) else  x[:x.find('$')+1] )
df['Class'] = df['Class'].map(lambda x: str(x)[:x.rfind('.java')])
df.rename(columns={'Class':'CLASS',
                          'Package':'PACKAGE'},
                 inplace=True)
df.head()


# In[4]:


df = df.groupby(['CLASS','PACKAGE','Coverage'],as_index = False).size().unstack(fill_value=0)


# In[5]:


df['Total_Mutant'] =  (df['KILLED'] + df['NO_COVERAGE'] + df['SURVIVED'] + df['TIMED_OUT'])
df['Mutation_Score'] =  ((df['KILLED']+df['TIMED_OUT']) / df['Total_Mutant'])*100


# In[6]:


df1 = pd.read_csv('jacoco.csv', error_bad_lines=False)
df1['CLASS'] = df1['CLASS'].map(lambda x:  x if (x.find('.')+1 == 0) else  x[:x.find('.')] )
df1 = df1.groupby(df1['CLASS']).aggregate(sum).reset_index()
df1.columns


# In[7]:


merged_inner = pd.merge(left=df,right=df1, left_on='CLASS', right_on='CLASS')


# In[8]:


df1[(~df1.CLASS.isin(merged_inner.CLASS))&(~df1.CLASS.isin(merged_inner.CLASS))]


# In[9]:


df = merged_inner
df.columns
merged_inner.head()


# In[10]:


df.plot(x='Mutation_Score', y='Statement Coverage', style='o')


# In[11]:


df[['Mutation_Score','Statement Coverage']].corr(method ='spearman')


# In[12]:


df.plot(x='Mutation_Score', y='Branch Coverage', style='o')


# In[13]:


df[['Mutation_Score','Branch Coverage']].corr(method ='spearman')
