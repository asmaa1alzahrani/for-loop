#!/usr/bin/env python
# coding: utf-8

# In[3]:


for x in range(0,151):
    print (x)
    


# In[16]:


for i in range (5,1000,1) :
    print(i*5)


# In[7]:


for i in range(1,100):
    if i%5==0:
        print('Coding')
    if i%10==0:
        print('Coding Dojo')


# In[ ]:





# In[20]:


min=0
max=500000
odd_sum=0

for n in range(min,max+1):
    if (n%2 !=0):
        odd_sum=odd_sum+n
        
print("The sum of odd numbers from {0} to {1} = {2}".format(min,max,odd_sum))
        


# In[22]:


num=2018
while num>0:
    print (num)
    num=num-4


# In[ ]:




