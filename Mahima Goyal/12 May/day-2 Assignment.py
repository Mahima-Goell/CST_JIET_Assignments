#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Q3 day 2 date:12 May
#take the value for no. of rows and columns
n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
arr=[]
#variable for counting no. of column with odd 1s
count=0
print("enter the elements of matrix of order {}*{}".format(n,m))
for i in range(n):
    r=[]
    for j in range(m):
        p=int(input())
        r.append(p)
    arr.append(r)
print("entered matrix is:")
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
res=0 #result variable to hold value of xor of all values of a column
for j in range(m):
    res=0 # at each new column initialize res as zero
    for i in range(n):
        res=res^arr[i][j]
    if(res==1): #if xor of 1 column is one then it means no. of 1s  in that column are odd
        count=count+1
print("no. of columns with odd 1s:",count)


=================================================================================================================================================================

# In[10]:


#Q1 day 2 date:12 May
def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return 0
                break
        else:
                return 1
n=int(input("Enter the no. of rows:"))
m=int(input("Enter the no. of columns:"))
mat=[]
count=0
#enter the values in matrix
for i in range(n):
    r=[]
    for j in range(m):
        p=int(input())
        r.append(p)
    mat.append(r)
#check and sum the adjacent cell values valid to the condition of problem stated
for i in range(n):
    for j in range(m):
        sum=0
        if(i-1>=0):
            sum=sum+mat[i-1][j]
        if(i+1<n):
            sum=sum+mat[i+1][j]
        if(j-1>=0):
            sum=sum+mat[i][j-1]
        if(j+1<m):
            sum=sum+mat[i][j+1]
        print("sum at end of {} and {}:".format(i,j),sum)
        if prime(sum)==1:
            count=count+1
print("count of those cells having adjacent cell sum as prime:",count)
            
        
============================================================================================================================================================


# In[8]:


#Q2 day 2 date:12 May
#enter no. to be searched
x=int(input("Enter the no. to be searched in matrix:"))
n=int(input("Enter the no. of rows:"))
m=int(input("Enter the no. of columns:"))
mat=[]
count=0
#enter the values in matrix
for i in range(n):
    r=[]
    for j in range(m):
        p=int(input())
        r.append(p)
    mat.append(r)
i=0
j=n-1
found=0
while(i<n and j>=0):
    if(mat[i][j] == x):
        print("Found at (",i,",",j,")")
        found=1
        break
    elif(mat[i][j]>x):
        j=j-1
    else:
        i=i+1
if(found==0):
    print("Element not found")


========================================================================================================================




