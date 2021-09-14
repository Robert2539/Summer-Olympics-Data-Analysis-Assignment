#!/usr/bin/env python
# coding: utf-8

# # Summer Olympics Data Analysis Assignment

# In[14]:


#importing pandas
import pandas as pd
df1=pd.read_csv("summer.csv")
df1.head()


# ## 1. In how many cities Summer Olympics is held so far?

# In[15]:


print(len(df1['City'].unique()))


# ## 2. Which sport is having most number of Gold Medals so far? (Top 5)

# In[16]:


df2=df1[df1['Medal'] == 'Gold']
df2.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot.bar(title="Most gold medals in sports")


# ## 3. Which sport is having most number of medals so far? (Top 5)

# In[17]:


df1.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot.bar(title="Most medals in sports")


# ## 4. Which player has won most number of medals? (Top 5)

# In[18]:


df1.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot.bar(title="Player with Most medals")


# ## 5. Which player has won most number Gold Medals of medals? (Top 5)

# In[19]:


df2.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot.bar(title="Player with Most Gold medals")


# ## 6. In which year India won first Gold Medal in Summer Olympics?

# In[20]:


df1[(df1['Country'] == 'IND') & (df1['Medal'] == 'Gold')]['Year'].min()


# ## 7. Which event is most popular in terms on number of players? (Top 5)

# In[21]:


df1.groupby('Event').count()['Athlete'].sort_values(ascending = False).head().plot.bar(title="Most popular event")


# ## 8. Which sport is having most female Gold Medalists? (Top 5)

# In[22]:


df4=df1[(df1['Gender'] == 'Women')&(df1['Medal'] == 'Gold')]
df4.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot.bar(title="Most female Gold Medalists")


# In[ ]:





# In[ ]:




