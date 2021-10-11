#!/usr/bin/env python
# coding: utf-8

# In[3]:quistion 1 print all integers from 0 to 150


for x in range(0,151):
    print (x)
    


# In[16]:Quistion 2 Print all the multiples of 5 from 5 to 1000


for i in range (5,1000,1) :
    print(i*5)


# In[7]:print integeres 1 to 100 .if divisible by 5 print Coding , if divisible by 10 print Coding Dojo


for i in range(1,100):
    if i%5==0:
        print('Coding')
    if i%10==0:
        print('Coding Dojo')




# In[20]:Add odd integers from 0 to 500000 and print the final sum?


min=0
max=500000
odd_sum=0

for n in range(min,max+1):
    if (n%2 !=0):
        odd_sum=odd_sum+n
        
print("The sum of odd numbers from {0} to {1} = {2}".format(min,max,odd_sum))
        


# In[22]:Print positive numbers starting at 2018,counting down by fours 


num=2018
while num>0:
    print (num)
    num=num-4


# In[ ]:





