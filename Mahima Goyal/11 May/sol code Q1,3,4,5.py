#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Q1 day 1 date:11 May
#declaring an array
arr = [7,1,2,3,1,3,2]
#variable holding occurence of elements
occur=arr[0]
#XORing the elements of array by each other as XOR of element by itself is 0 thus causing the similar elements to result as 0
for i in range(1,7):
    occur=occur^arr[i]
print("element with one occurence is:",occur)

---------------------------------------------------------------------------------------------------------------------------------------

# 

# In[6]:


#Q5 day 1 date:11 May
def sqrt(number):
    if(number==0 or number==1):
        return number
    i=1
    square=1
    # check until the square of i number is less than entered number
    # update square to find all perfect square till that number
    while(square<=number):
        i=i+1
        square=i*i
    return (i-1)
print("enter number whose square root we need to find:")
number=int(input())
print("square root of entered number is:",sqrt(number))

-------------------------------------------------------------------------------------------------------------------------------------------

# In[7]:


#Q3 day 1 date:11 May
def max_height(n):
    i=1
    h=0
    # do check for maximum heigth until the number of blocks become 0
    while(n>=0): 
        n=n-i #reduce number of blocks as we go further from one step to other no.of blockinstaircaseareequivalentto i atthatstep
        if(n>=0):
            h=h+1 #increase height only when n>=0
        i=i+1
    return (h)
print("enter number of blocks:")
n=int(input())
print("maximum height of staricase is:",max_height(n))

-----------------------------------------------------------------------------------------------------------------------------------------------------------

# In[4]:


#Q4 day 1 date:11 May
#defining a function for providing number of paths possible
def number_of_paths(n):
    path_count = [[0]*n]*n
    #for loop for updating the values of path_count showing the no. of ways to reach particular position in path_count of column 1
    for i in range(n):
        path_count[i][0]=1
    #for loop for updating the values of path_count showing the no. of ways to reach particular position in path_count of row 1
    for j in range(n):
        path_count[0][j]=1
    #upadte value of each cell in path_count by no.of ways to reach that cell
    for i in range(1,n):
        for j in range(1,n):
            path_count[i][j]=path_count[i-1][j]+path_count[i][j-1]
    return path_count[n-1][n-1]
print("enter the no. of rows and columns:")
n=int(input())
print("no. of possible paths to reach at right-bottom corner from top-left corner without crossing diagonal are:",number_of_paths(n))

------------------------------------------------------------------------------------------------------------------------------------------------------------
# In[ ]:




