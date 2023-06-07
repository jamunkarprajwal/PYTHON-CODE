#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


dict1 = {'Name':['Priyang','Aadhya','Krishna','Vedant','Parshv','Mittal','Archana'],'Marks':[89,98,99,67,88,90,95],
         'Gender':['Male','Female','Male','Male','Male','Male','Female']}

print(dict1)


# In[5]:


dict1 = {'Name':['Priyang','Aadhya','Krishna','Vedant','Parshv','Mittal','Archana'],'Marks':[89,98,99,67,88,90,95],
         'Gender':['Male','Female','Male','Male','Male','Male','Female']}

df=pd.DataFrame(dict1)
display(df)


# In[6]:


# display top 3 rows of dataset
df.head(3)


# In[7]:


#check last 3 rows of dataset
df.tail(3)


# In[8]:


#find shape of our dataset (Number of rows and number of columns)
df.shape


# In[9]:


print("Number of rows",df.shape[0])
print("Number of columns",df.shape[1])


# In[10]:


#Get informtion about our dataset like total number of rows,columns ,datatypes of each column and memory requirement
df.info()


# In[14]:


#check null values in dataset
df.isnull().sum(axis=1)  # row wise
df.isnull().sum(axis=0)  #column wise


# In[16]:


#get overall statistics about the dataframe by default gives for column
df.describe(include='all')


# In[17]:


#find distinct values from gender column
df['Gender'].unique()


# In[18]:


#find the number of unique values from gender column
df['Gender'].nunique()


# In[19]:


#display count of unique values in gender column
df['Gender'].value_counts()


# In[20]:


# find total number of students having marks between 90 to 100 (inclusive) using b/w method
df[df['Marks']>=85]


# In[22]:


df[(df['Marks']>=90) & (df['Marks']<=95)]


# In[23]:


len(df[(df['Marks']>=90) & (df['Marks']<=95)])


# In[25]:


#Find Average marks
df['Marks'].mean()


# In[26]:


# Max value
df['Marks'].max()


# In[27]:


# Min value
df['Marks'].min()


# In[28]:


# Apply method

def marks(x):
    return x/2


# In[29]:


df['Marks'].apply(marks)


# In[31]:


df['Half_marks']=df['Marks'].apply(marks)


# In[32]:


df


# In[33]:


#Alternative way to solve this

df['Marks'].apply(lambda x:x/2)


# In[34]:


# length of records in name column
df['Name'].apply(len)


# In[39]:


# Map Function
df['Male_Female']=df['Gender'].map({'Male':1,'Female':0})
df


# In[40]:


# drop columns 
df.drop('Male_Female',axis=1)


# In[43]:


# drop multiple column 
df.drop(['Male_Female','Half_marks'],axis=1,inplace=True)


# In[44]:


df


# In[45]:


# print name of columns
df.columns


# In[46]:


df.index


# In[47]:


#sort the dataframe as per the marks column either in ascending or descending

df.sort_values(by='Marks',ascending=False)



# In[48]:


# Display the marks of female 
df[df['Gender']=='Female']


# In[ ]:




