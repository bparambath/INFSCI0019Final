
# coding: utf-8

# In[1]:


import pandas as pd #importing pandas
import numpy as np #importing numpy

# The following line is a directive that tells matplotlib module to display
# generated graphs inline with the output of your code
get_ipython().run_line_magic('matplotlib', 'inline')

# Import matplotlib module.  Matplotlib module allows us to generate graphs from data
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("degrees-that-pay-back.csv") #create dataframe
df.head()


# In[3]:


#First item  that needs to be cleaned is the dollar sign in all of the salary amounts
#this means that all of the salaries are entered as strings.
#since the data is entered as strings need to convert the salary amounts to integers
#https://www.tutorialspoint.com/python/string_replace.htm

df['Starting Median Salary'] = df['Starting Median Salary'].str.replace(',', '')
df['Starting Median Salary'] = df['Starting Median Salary'].str.replace('$', '')
df['Starting Median Salary'] = df['Starting Median Salary'].astype(float)

df['Mid-Career Median Salary'] = df['Mid-Career Median Salary'].str.replace(',', '')
df['Mid-Career Median Salary'] = df['Mid-Career Median Salary'].str.replace('$', '')
df['Mid-Career Median Salary'] = df['Mid-Career Median Salary'].astype(float)

df['Mid-Career 10th Percentile Salary'] = df['Mid-Career 10th Percentile Salary'].str.replace(',', '')
df['Mid-Career 10th Percentile Salary'] = df['Mid-Career 10th Percentile Salary'].str.replace('$', '')
df['Mid-Career 10th Percentile Salary'] = df['Mid-Career 10th Percentile Salary'].astype(float)

df['Mid-Career 25th Percentile Salary'] = df['Mid-Career 25th Percentile Salary'].str.replace(',', '')
df['Mid-Career 25th Percentile Salary'] = df['Mid-Career 25th Percentile Salary'].str.replace('$', '')
df['Mid-Career 25th Percentile Salary'] = df['Mid-Career 25th Percentile Salary'].astype(float)

df['Mid-Career 75th Percentile Salary'] = df['Mid-Career 75th Percentile Salary'].str.replace(',', '')
df['Mid-Career 75th Percentile Salary'] = df['Mid-Career 75th Percentile Salary'].str.replace('$', '')
df['Mid-Career 75th Percentile Salary'] = df['Mid-Career 75th Percentile Salary'].astype(float)

df['Mid-Career 90th Percentile Salary'] = df['Mid-Career 90th Percentile Salary'].str.replace(',', '')
df['Mid-Career 90th Percentile Salary'] = df['Mid-Career 90th Percentile Salary'].str.replace('$', '')
df['Mid-Career 90th Percentile Salary'] = df['Mid-Career 90th Percentile Salary'].astype(float)

df.head()


# In[28]:


df['Starting Median Salary'].hist()


# In[5]:


df.describe()


# In[6]:


df.plot.bar(x='Undergraduate Major', y='Starting Median Salary')


# In[7]:


df.isnull().sum()


# In[8]:


df


# In[9]:


df.describe()


# In[10]:


df.sort_values(by = 'Starting Median Salary', ascending = False, inplace=True) #ordering the rows by salary (highest salary at the top)
df.head()


# In[11]:


df = df.reset_index() #resetting the indexes so that their index correlates to how high their starting median salary is
df.head()


# In[12]:


df = df.drop(columns=['index']) #removing the old index column


# In[13]:


df.head()


# In[26]:


fig = plt.figure(figsize=(8,12)) #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig.set_size_inches(18.5, 10.5)

x = df['Starting Median Salary'] #switch x and y labels
y = df.index
labels = df['Undergraduate Major']

plt.scatter(x, y, label = 'Starting Median Salary') 
plt.yticks(y, labels) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html

plt.xlabel('US $')
plt.ylabel('Major') 
plt.title('Starting Median Salary by Major')
plt.legend()
plt.show()
fig.savefig('MedianSalarybyMajor.png', dpi=100)


# In[15]:


dfnew = df.sort_values(by='Mid-Career Median Salary', ascending=False)
dfnew = dfnew.reset_index()


# In[22]:


fig = plt.figure(figsize=(8,12)) #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig.set_size_inches(18.5, 10.5)

x = dfnew['Starting Median Salary'] #switch x and y labels
x2 = dfnew['Mid-Career Median Salary']

y = dfnew.index
labels = dfnew['Undergraduate Major']

plt.scatter(x, y, label = 'Starting Median Salary') 
plt.yticks(y, labels) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html

plt.scatter(x2, y, color='red', label = 'Median Mid Career Salary')

plt.xlabel('US $')
plt.ylabel('Major') 
plt.title('Starting Median Salary by Major')
plt.legend()
plt.show()
fig.savefig('MedianandMidSalarybyMajor.png', dpi=100)


# In[23]:


fig = plt.figure(figsize=(8,12)) #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig.set_size_inches(18.5, 10.5)

x = dfnew['Mid-Career Median Salary']
x2 = dfnew['Mid-Career 10th Percentile Salary'] 
x3 = dfnew['Mid-Career 25th Percentile Salary'] 
x4 = dfnew['Mid-Career 75th Percentile Salary'] 
x5 = dfnew['Mid-Career 90th Percentile Salary'] 


y = dfnew.index
labels = dfnew['Undergraduate Major']

plt.scatter(x, y, color='red', label = 'Median Mid Career Salary') 
plt.yticks(y, labels) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html

plt.scatter(x2, y, color='blue', label = '10th Percentile Mid Career Salary')
plt.scatter(x3, y, color='purple', label = '25th Percentile Mid Career Salary')
plt.scatter(x4, y, color='orange', label = '75th Percentile Mid Career Salary')
plt.scatter(x5, y, color='green', label = '90th Percentile Mid Career Salary')

plt.xlabel('US $')
plt.ylabel('Major') 
plt.title('Mid Career Salary by Major')
plt.legend()
plt.show()
fig.savefig('MidCareerSalaryComparison.png', dpi=100)


# In[18]:


dfnewer = df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)
dfnewer = dfnewer.reset_index()


# In[24]:


fig = plt.figure(figsize=(8,12)) #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig.set_size_inches(18.5, 10.5)

x = dfnewer['Mid-Career Median Salary']
x2 = dfnewer['Mid-Career 10th Percentile Salary'] 
x3 = dfnewer['Mid-Career 25th Percentile Salary'] 
x4 = dfnewer['Mid-Career 75th Percentile Salary'] 
x5 = dfnewer['Mid-Career 90th Percentile Salary'] 


y = dfnewer.index
labels = dfnewer['Undergraduate Major']

plt.scatter(x, y, color='red', label = 'Median Mid Career Salary') 
plt.yticks(y, labels) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html

plt.scatter(x2, y, color='blue', label = '10th Percentile Mid Career Salary')
plt.scatter(x3, y, color='purple', label = '25th Percentile Mid Career Salary')
plt.scatter(x4, y, color='orange', label = '75th Percentile Mid Career Salary')
plt.scatter(x5, y, color='green', label = '90th Percentile Mid Career Salary')


plt.xlabel('US $')
plt.ylabel('Major') 
plt.title('Mid Career Salary by Major (Sorted by 90th Percentile)')
plt.legend()
plt.show()
fig.savefig('90thPercentCareerSalaryComparison.png', dpi=100)


# In[20]:


dfnewest = df.sort_values(by='Mid-Career 90th Percentile Salary', ascending=False)
dfnewest = dfnewer.reset_index()
dfnewest.head()


# In[25]:


fig = plt.figure(figsize=(8,12)) #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
fig.set_size_inches(18.5, 10.5)

x = dfnewer['Mid-Career 90th Percentile Salary'] 

y = dfnewer.index

labels = dfnewer['Undergraduate Major']

plt.scatter(x, y, color='green', label = '90th Percentile Mid Career Salary')
plt.yticks(y, labels) #https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xticks.html


plt.xlabel('US $')
plt.ylabel('Major') 
plt.title('Mid-Career 90th Percentile Salary by Major')
plt.legend()
plt.show()
fig.savefig('90thPercentCareerSalary.png', dpi=100)

