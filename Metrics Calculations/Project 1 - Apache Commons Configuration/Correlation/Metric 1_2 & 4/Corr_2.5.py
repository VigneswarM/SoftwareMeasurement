#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd


# In[2]:


pd.set_option('display.max_columns', None)


# In[3]:


df = pd.read_csv('mutations.csv', error_bad_lines=False, names = ["Class", "Package", "gc1", "gc2","gc3","Coverage","gc4"])


# In[4]:


df.drop('gc1', axis=1, inplace=True)


# In[5]:


df.drop('gc2', axis=1, inplace=True)


# In[6]:


df.drop('gc3', axis=1, inplace=True)


# In[7]:


df.drop('gc4', axis=1, inplace=True)


# In[8]:


df['Package'] = df['Package'].map(lambda x: str(x)[:x.rfind('.')])


# In[9]:


df['Package'] = df['Package'].map(lambda x:  x if (x.find('$')+1 == 0) else  x[:x.find('$')+1] )


# In[10]:


df['Class'] = df['Class'].map(lambda x: str(x)[:x.rfind('.java')])


# In[11]:


df.rename(columns={'Class':'CLASS',
                          'Package':'PACKAGE'},
                 inplace=True)


# In[12]:


df.head()


# In[13]:


df = df.groupby(['CLASS','PACKAGE','Coverage'],as_index = False).size().unstack(fill_value=0)


# In[14]:


df['Total_Mutant'] =  (df['KILLED'] + df['NO_COVERAGE'] + df['SURVIVED'] + df['TIMED_OUT'])


# In[15]:


df['Mutation_Score'] =  ((df['KILLED']+df['TIMED_OUT']) / df['Total_Mutant'])*100


# In[16]:


df1 = pd.read_csv('jacoco.csv', error_bad_lines=False)


# In[17]:


df1['CLASS'] = df1['CLASS'].map(lambda x:  x if (x.find('.')+1 == 0) else  x[:x.find('.')] )


# In[18]:


df1 = df1.groupby(df1['CLASS']).aggregate(sum).reset_index()


# In[19]:


df1.columns


# In[20]:


merged_inner = pd.merge(left=df,right=df1, left_on='CLASS', right_on='CLASS')


# In[21]:


df1[(~df1.CLASS.isin(merged_inner.CLASS))&(~df1.CLASS.isin(merged_inner.CLASS))]


# In[22]:


df = merged_inner


# In[23]:


df.columns


# In[24]:


merged_inner.head()


# In[25]:


df.plot(x='Mutation_Score', y='Statement Coverage', style='o')


# In[26]:


df[['Mutation_Score','Statement Coverage']].corr(method ='spearman')


# In[27]:


df.plot(x='Mutation_Score', y='Branch Coverage', style='o')


# In[28]:


df[['Mutation_Score','Branch Coverage']].corr(method ='spearman')


# In[ ]:




