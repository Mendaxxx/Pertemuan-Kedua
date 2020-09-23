#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np


# In[18]:


print(np.__version__)


# # Big O Notation
# 

# In[19]:


def getFirst(myList):
    return myList[0]


# In[20]:


getFirst([1,2,3])


# # Linear Time (O(n)) Complexity
# An Alghoritm is said to have a complexity of linear time, represented by O(n),

# In[21]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[22]:


getSum([[1,2,5],[3,4,7]])


# In[11]:



def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while(first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[12]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[13]:


searchBinary([8,9,10,100,1000,2000,3000], 5)


# In[ ]:




