#!/usr/bin/env python
# coding: utf-8

# # Reversing a string(using slicing)

# In[1]:


#takes string as input from user
str_input = input("Enter the string:")
#gives length of string
str_input_length = len(str_input)
#prints string in reverse by slicing, 
#we are starting the index with str length so it starts from the last letter and prints each letter in reverse 
#as step size is given as -1
print(str_input[str_input_length::-1])


# # Reversing a string(using loop)

# In[2]:


#takes string as input from user
strinput = input("Enter the string:")
#print(strinput[0])
#gives length of string
strinput_len=len(strinput)
#print(strinput_len)
#initialises an empty string to variable strinput_reverse
strinput_reverse=""
while(strinput_len>0):
    strinput_reverse+=strinput[strinput_len-1]
    strinput_len=strinput_len-1
print(strinput_reverse)


# # print pattern

# In[5]:


n=5
for i in range(0,n):
  for j in range(0,i+1):
    print("*", end="")
  print("\r")
for i in range(n+1,0,-1):
  for j in range(0,i-1):
     print("*", end='')
  print("\r")

