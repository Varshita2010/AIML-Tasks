#!/usr/bin/env python
# coding: utf-8

# In[10]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter + 1
        sum += x
    mean = sum / counter
    return mean


# In[22]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)

    if l%2 == 0:
        medium = (num_list[int(l/2)] + num_list[int((l/2))-1])/2
    else:
        medium = num_list[int(l/2)]
    return medium 


# In[24]:


mean_value(1,3,5,7,9,12,14,16,18)


# In[28]:


median_value(1,3,5,7,9,12,14,16,18)


# In[ ]:




