#!/usr/bin/env python
# coding: utf-8

# In[2]:


#impoting dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston


# In[3]:


#understanding the data set
boston=load_boston()
print(boston.DESCR)


# In[6]:


# access data attributes
dataset=boston.data
for name, index in enumerate(boston.feature_names):
    print(index,name)


# In[8]:


#reshaping data
data=dataset[:,12].reshape(-1,1)


# In[9]:


#shape of the data
np.shape(dataset)


# In[10]:


#target values
target=boston.target.reshape(-1,1)


# In[11]:


#shape of the targt
np.shape(target)


# In[13]:


#ensuring that matplotlib is working inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(data,target,color='green')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.show()


# In[16]:


#regression
from sklearn.linear_model import LinearRegression
#creating a regression model
reg=LinearRegression()
#fit the model
reg.fit(data,target)


# from sklearn.linear_model import Laso
# from sklearn.linear_model import Ridge
# can do these too.

# In[18]:


#prediction
pred=reg.predict(data)


# In[20]:


#ensuring that matplotlib is working inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(data,target,color='red')
plt.plot(data,pred,color='green')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.show()


# In[22]:


#circumventing curve issue using polynomial model
from sklearn.preprocessing import PolynomialFeatures
#to allow merging of models
from sklearn.pipeline import make_pipeline


# In[23]:


model=make_pipeline(PolynomialFeatures(3),reg)


# In[24]:


model.fit(data,target)


# In[25]:


pred=model.predict(data)


# In[26]:


#ensuring that matplotlib is working inside the notebook
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(data,target,color='red')
plt.plot(data,pred,color='green')
plt.xlabel('Lower income population')
plt.ylabel('Cost of House')
plt.show()


# In[28]:


#r_2 metric
from sklearn.metrics import r2_score


# In[30]:


#predict
r2_score(pred,target)


# In[ ]:




