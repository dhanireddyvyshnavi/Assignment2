#!/usr/bin/env python
# coding: utf-8

# ### Assignment 2

# In[1]:


#1. Write a Python program to convert a given  list to a tuple. [5, 10, 7, 4, 15, 3] 


lst=[5, 10, 7, 4, 15, 3] 
t=tuple(lst)
print(t)


# In[3]:


#2. Write a Python program to get the 4th element from first  and 4th element from last of a tuple. 

#( "p" , "y" , "t", "h" , "o" , "n" , "p" , "r" , "o" , "g" , "r" , "a" , "m" , "m" , "i" , "n" , "g" )

t=( "p" , "y" , "t", "h" , "o" , "n" , "p" , "r" , "o" , "g" , "r" , "a" , "m" , "m" , "i" , "n" , "g" )
print(t[3]+t[-5])


# In[5]:


#3. Write a python program to find largest number in a given list with out using max() .[10, 7 , 0 ,14 , 4 , 2 ]


l=[10, 7 , 0 ,14 , 4 , 2 ]

def maxElementDS(ds):
    m = ds[0]
    for i in ds:
        if i>m:
            m = i
    return m
maxElementDS(l)


# In[9]:


#4. Write a python program to print all even numbers from a given list .[111 , 4 , 7 , 16 , 27 , 40 , 18 , 99 ,101, 14]
lst=[111 , 4 , 7 , 16 , 27 , 40 , 18 , 99 ,101, 14]
for i in lst:
    if i%2 == 0:
        print(i)
    
    


# In[11]:


#5. Write a Python script to add a key to a dictionary. 

  #   Sample Dictionary : {0: 10, 1: 20}

  #   Expected Result : {0: 10, 1: 20, 2: 30}
n={0: 10, 1: 20}

n[2]=30
print(n)


# In[9]:


#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x) 

#     Sample Dictionary ( n = 5) : 

 #    Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  
    
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)


# In[ ]:




