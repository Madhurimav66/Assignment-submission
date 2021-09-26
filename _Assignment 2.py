#!/usr/bin/env python
# coding: utf-8

# # Assignment 2: 1

# In[40]:


#range(2000,3200) takes values from 2000 to 3200 excluding 3200 and that is why, I have taken 3201 to include 3200
for i in range(2000,3201):#for loop iterates through each value given in range
    #condition to check if the value is divisible by 7 and multiple of 5 is always divisible by 5,
    #so the if condition checks if i is divisible by 7 and not divisible by 5
    if (i%7)==0 and (i%5)!=0:
        #after checking condition, prints the values which fulfills the condition as 
        #comma separated values in a single line
        print(i, end = ",") 


# # Assignment 2:2

# In[43]:
#Firstname and lastname are taken as input from user using input()
#using print, the lastname and firstname are printed

First_name = input("Enter your Firstname:")
Last_name = input("Enter your Lastname:")
print(Last_name,First_name)


# # Assignment 2:3

# In[45]:

#math is imported to use pi value and volume of sphere is obtained in print statement
import math
print("The volume of a sphere with diameter 12cm is:",(4/3)*math.pi*(12/2))

