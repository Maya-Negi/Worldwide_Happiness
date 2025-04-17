#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Importing the dataset 2
happiness_report = pd.read_csv("D:/Python/worldwide_happiness_report.csv")
dataset = pd.read_csv("D:/Python/covid19_Confirmed_dataset.csv")


# In[3]:


happiness_report


# In[4]:


# Drop Useless Columns
useless_cols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]


# In[5]:


happiness_report.drop(useless_cols, axis=1, inplace = True)
happiness_report.head()


# In[6]:


happiness_report.set_index("Country or region", inplace = True)
happiness_report.head()


# In[7]:


# aggregate the rows by country
corona_dataset_aggregated = dataset.groupby("Country/Region").sum()


# In[8]:


countries = list(corona_dataset_aggregated.index)
max_infections_rates = []

for c in countries:
    max_infections_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["Max_infections_rates"] = max_infections_rates


# In[9]:


# Create a new Data Frame
corona_data = pd.DataFrame(corona_dataset_aggregated["Max_infections_rates"])


# In[10]:


#Join the dataset
corona_data.shape


# In[11]:


happiness_report.shape


# In[12]:


data = corona_data.join(happiness_report, how = "inner")
data


# In[13]:


data.corr()


# In[14]:


data


# In[15]:


# Vizualisation 
x = data["GDP per capita"]
y = data["Max_infections_rates"]
sns.scatterplot(x=x, y=y, color='red')


# In[16]:


sns.regplot(x=x, y=np.log(y))


# In[17]:


x = data["Social support"]
y = data["Max_infections_rates"]
sns.scatterplot(x=x, y=np.log(y))


# In[18]:


sns.regplot(x=x, y=np.log(y))


# In[19]:


x = data["Healthy life expectancy"]
y = data["Max_infections_rates"]
sns.scatterplot(x=x, y=np.log(y))


# In[20]:


sns.regplot(x=x, y=np.log(y))


# In[21]:


x = data["Freedom to make life choices"]
y = data["Max_infections_rates"]
sns.scatterplot(x=x, y=np.log(y))


# In[22]:


sns.regplot(x=x, y=np.log(y))


# In[ ]:





# In[ ]:




