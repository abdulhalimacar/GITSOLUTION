#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <p style="text-align: center;"><img src="https://docs.google.com/uc?id=1lY0Uj5R04yMY3-ZppPWxqCr5pvBLYPnV" class="img-fluid" 
# alt="CLRSWY"></p>
# 
# ## <p style="background-color:#FDFEFE; font-family:newtimeroman; color:#9d4f8c; font-size:100%; text-align:center; border-radius:10px 10px;">WAY TO REINVENT YOURSELF</p>
# 
# ## <p style="background-color:#FDFEFE; font-family:newtimeroman; color:#060108; font-size:200%; text-align:center; border-radius:10px 10px;">Data Analysis with Python</p>
# 
# ![Image_Assignment](https://i.ibb.co/cY9HhF7/bnote-assignment.gif)
# 
# ## <p style="background-color:#FDFEFE; font-family:newtimeroman; color:#4d77cf; font-size:200%; text-align:center; border-radius:10px 10px;">Assignment 01 (NumPy & Pandas Basics)</p>

# <a id="toc"></a>
# 
# ## <p style="background-color:#9d4f8c; font-family:newtimeroman; color:#FFF9ED; font-size:175%; text-align:center; border-radius:10px 10px;">Content</p>
# 
# * [NUMPY SECTION](#0)
# * [PANDAS SECTION](#1)
# 

# **In this assignment you will start off with Numpy Exercises and then complete the whole Exercise with Pandas questions. All the subjects related to questions here already covered in preclass materials and in-class sessions. So good luck!**

# ## <p style="background-color:#9d4f8c; font-family:newtimeroman; color:#FFF9ED; font-size:175%; text-align:center; border-radius:10px 10px;">Numpy Section</p>
# 
# <a id="0"></a>
# <a href="#toc" class="btn btn-primary btn-sm" role="button" aria-pressed="true" 
# style="color:blue; background-color:#dfa8e4" data-toggle="popover">Content</a>

# ### 1. Import NumPy Library.

# In[4]:


# YOUR CODE IS HERE
import numpy as np


# ### 2. Create an array from my_list = [5, 10, 15, 20, 25]

# In[3]:


# YOUR CODE IS HERE
my_list = np.array([5, 10, 15, 20, 25])
my_list

Desired Output:

array([ 5, 10, 15, 20, 25])
# ### 3. Generate an array of 5x5 with zeros. 

# In[5]:


# YOUR CODE IS HERE
zeros = np.zeros((5,5))

Desired Output:

array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
# ### 4. Generate an array of 4x4 with ones and assign data type as int.

# In[7]:


# YOUR CODE IS HERE
ones = np.ones((4,4), dtype=int)
ones

Desired Output:

array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
# ### 5. Make all the values of the array above with the value of 7.

# In[13]:


# YOUR CODE IS HERE
yediler_erenler = np.ones((4,4), dtype=int) * 7
yediler_erenler

Desired Output:

array([[7, 7, 7, 7],
       [7, 7, 7, 7],
       [7, 7, 7, 7],
       [7, 7, 7, 7]])
# ### 6. Create the previous array above by full() method.

# In[10]:


# YOUR CODE IS HERE
yediler_erenler = np.full((4,4), 7)
yediler_erenler

Desired Output:

array([[7, 7, 7, 7],
       [7, 7, 7, 7],
       [7, 7, 7, 7],
       [7, 7, 7, 7]])
# ### 7. Create an array of even integers from 2 to 16 (inclusive). 

# In[17]:


# YOUR CODE IS HERE
evens = np.arange(2,18,2)
evens

Desired Output:

array([ 2,  4,  6,  8, 10, 12, 14, 16])
# ### 8. Create a 5x5 matrix with the values between 0 to 25 (exclusive).

# In[21]:


# YOUR CODE IS HERE
matrix = np.arange(0,25).reshape(5,5)
matrix

Desired Output:

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])
# ### 9. Create a 5x5 matrix with the values between 0 to 25 (exclusive) using linspace method.

# In[24]:


# YOUR CODE IS HERE
matrix2 = np.linspace(0,24, 25, dtype=int).reshape(5,5)
matrix2

Desired Output:

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])
# ### 10. Create randomly 5 numbers with numpy.

# In[26]:


# YOUR CODE IS HERE
byrandom = np.random.rand(5)
byrandom

Desired Output (WATCH OUT! Your output will probably NOT be the same as the one below due to randomization):

array([0.69664494, 0.66387647, 0.97508534, 0.33818591, 0.58766187])
# ### 11. Create an array of 5*5 shape and fills it with random values as per the standard normal distribution.

# In[33]:


# YOUR CODE IS HERE
normal = np.random.randn(25)
x = normal.reshape(5,5)
x

Desired Output (WATCH OUT! Your output will probably NOT be the same as the one below due to randomization):

array([[ 0.73087006, -0.34675846, -1.03601606, -0.61227298, -0.57078798],
       [ 1.85976917, -0.37158111, -1.16789003, -0.81271697,  1.39620977],
       [ 0.52695367, -0.19017673,  0.78067235, -1.3520313 ,  0.44878344],
       [ 0.27758877,  0.75391726, -0.52652875,  0.74519765, -0.40414682],
       [ 0.12743864, -0.81637521,  0.14086653, -0.29524574,  0.12703938]])
# ### 12. Create a 3*4 array of random int numbers between 20 and 50.

# In[36]:


# YOUR CODE IS HERE
x = np.random.randint(20,50,12).reshape(3,4)
x

Desired Output (WATCH OUT! Your output will probably NOT be the same as the one below due to randomization):

array([[33, 39, 47, 26],
       [41, 20, 32, 23],
       [25, 22, 41, 28]])
# ### 13. Create an array named "ranarr"consisting of randomly 48 numbers and reshape this array with the shape of 6x8 in different ways.

# In[45]:


# YOUR CODE IS HERE
ranarr = np.random.randint(0,48,48)
ranarr

Desired Output (WATCH OUT! Your output may NOT be the same as the one):

array([ 6, 21, 18, 53, 38, 37, 30, 47, 19, 44, 29, 12, 14, 37, 24, 14, 16,
       18,  3, 19, 19, 41, 28, 41,  3, 47,  4, 18, 27, 44, 15, 21,  5, 55,
       38,  9,  5, 50, 15, 20,  7, 26, 45, 39, 37, 23,  6, 10])
# In[46]:


# YOUR CODE IS HERE (RESHAPING WITH NUM)
x = ranarr.reshape(6,8)
x

Desired Output (WATCH OUT! Your output may NOT be the same as the one):

array([[ 6, 21, 18, 53, 38, 37, 30, 47],
       [19, 44, 29, 12, 14, 37, 24, 14],
       [16, 18,  3, 19, 19, 41, 28, 41],
       [ 3, 47,  4, 18, 27, 44, 15, 21],
       [ 5, 55, 38,  9,  5, 50, 15, 20],
       [ 7, 26, 45, 39, 37, 23,  6, 10]])
# In[48]:


# YOUR CODE IS HERE (RESHAPING WITH -1)
y = ranarr.reshape(-1,12)
y

Desired Output (WATCH OUT! Your output may NOT be the same as the one):

array([[ 6, 21, 18, 53, 38, 37, 30, 47],
       [19, 44, 29, 12, 14, 37, 24, 14],
       [16, 18,  3, 19, 19, 41, 28, 41],
       [ 3, 47,  4, 18, 27, 44, 15, 21],
       [ 5, 55, 38,  9,  5, 50, 15, 20],
       [ 7, 26, 45, 39, 37, 23,  6, 10]])
# In[50]:


# YOUR CODE IS HERE (RESHAPING WITH -1)
u = ranarr.reshape(16,-1)
u

Desired Output (WATCH OUT! Your output may NOT be the same as the one):

array([[ 6, 21, 18, 53, 38, 37, 30, 47],
       [19, 44, 29, 12, 14, 37, 24, 14],
       [16, 18,  3, 19, 19, 41, 28, 41],
       [ 3, 47,  4, 18, 27, 44, 15, 21],
       [ 5, 55, 38,  9,  5, 50, 15, 20],
       [ 7, 26, 45, 39, 37, 23,  6, 10]])
# ## Numpy Indexing and Selection

# ### Create an array named "mat" in accordence with the desired output below.

# In[51]:


# YOUR CODE IS HERE 
mat = np.arange(1,17).reshape(4,4)
mat

Desired Output:

array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
# ### 14. Using the array above, write a code that reproduces the desired output shown below.<br>

# In[54]:


# YOUR CODE IS HERE 
mat[1:3, 1:3]

Desired Output:

array([[ 6,  7],
       [10, 11]])
# ### 15. Get the 1st column (index number 0) of the array above.

# In[55]:


# YOUR CODE IS HERE 
mat[:,0]

Desired Output:

array([ 1,  5,  9, 13])
# ### 16. Get the values in 2nd row (index number 1) for every 2 step.

# In[56]:


# YOUR CODE IS HERE 
mat[1, 0:4:2]

Desired Output:

array([5, 7])
# ### 17.Assign 77 to every cell in 3rd column.

# In[72]:


# YOUR CODE IS HERE 
mat[:,2]= 77,77,77,77
mat[2] = 9,10,77,12
mat

Desired Output:

array([[ 1,  2, 77,  4],
       [ 5,  6, 77,  8],
       [ 9, 10, 77, 12],
       [13, 14, 77, 16]])
# ### 18. (a) Take 2nd row (index number 1) and 1st column (index number 0) , (b) 4th row (index number 3) and 3rd column (index number 2) .

# In[73]:


# YOUR CODE IS HERE 
mat[1, 0:4:2]

Desired Output:

array([ 5, 77])
# ### 19. Take between 2nd and last row with step 2 and between 1st and last column with step 2.

# In[74]:


# YOUR CODE IS HERE 
mat[1:4:2, 0:4:2]

Desired Output:

array([[ 5, 77],
       [13, 77]])
# ## NumPy Operations

# ### 20. Get the sum of values smaller than 10 and values bigger than 12 in "mat".

# In[75]:


# LET US REMEMBER OUR ARRAY OF "mat" 

# YOUR CODE IS HERE 
x = mat
x

Desired Output:

array([[ 1,  2, 77,  4],
       [ 5,  6, 77,  8],
       [ 9, 10, 77, 12],
       [13, 14, 77, 16]])
# In[79]:


# LET US FIND THE VALUES SMALLER THAN 10 IN "mat" 

# YOUR CODE IS HERE 
x = mat[mat<10]
x

Desired Output:

array([1, 2, 4, 5, 6, 8, 9])
# In[80]:


# LET US FIND THE VALUES BIGGER THAN 12 IN "mat" 

# YOUR CODE IS HERE 
y = mat[mat>12]
y

Desired Output:

array([77, 77, 77, 13, 14, 77, 16])
# In[83]:


# LET US SUM THE VALUES SMALLER THAN 10 AND BIGGER THAN 12 IN "mat" 

# YOUR CODE IS HERE 
a = x + y
a

Desired Output:

array([78, 79, 81, 18, 20, 85, 25])
# ### 21. Get the standard deviation (std) of the result above.

# In[84]:


# YOUR CODE IS HERE 
np.std(a)

Desired Output:

29.700546274093877
# ### 22. Get the sum of the 2nd column in the original "mat".

# In[85]:


# LET US REMEMBER OUR ARRAY OF "mat" 

# YOUR CODE IS HERE 
mat

Desired Output:

array([[ 1,  2, 77,  4],
       [ 5,  6, 77,  8],
       [ 9, 10, 77, 12],
       [13, 14, 77, 16]])
# In[86]:


# LET OBTAIN THE ORIGINAL ARRAY OF "mat" 

# YOUR CODE IS HERE 
mat = np.arange(1,17).reshape(4,4)
mat

Desired Output:

array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
# In[88]:


# YOUR CODE IS HERE 
oursum = mat.sum(axis=0)
oursum[1]

Desired Output:

32
# ### 23. Get the median, mean and std of 3rd column in "mat".

# In[89]:


# LET US REMEMBER OUR ARRAY OF "mat" 

# YOUR CODE IS HERE 
mat

Desired Output:

array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]])
# In[104]:


# LET US ASSIGN THE COLUMN WE ARE INTERESTED IN TO A VARIABLE 

# YOUR CODE IS HERE 
y = mat[:,2]
y

Desired Output:

array([[ 3],
       [ 7],
       [11],
       [15]])
# In[105]:


# WHAT IF WE ARE INTERESTED IN THE 3RD ROW? 

# YOUR CODE IS HERE 

x = mat[2]
x

Desired Output:

array([ 9, 10, 11, 12])
# In[109]:


# LET US GET MEDIAN VALUE 

# YOUR CODE IS HERE 

a = np.median(y)
b = np.median(x)
print(a)
print(b)

Desired Output:

9.0
10.5
# In[111]:


# LET US GET MEAN VALUE 

# YOUR CODE IS HERE 
w = np.mean(y)
t = np.mean(x)
print(w)
print(t)

Desired Output:

9.0
10.5
# In[113]:


# LET US GET STANDART DEVIATION (std) VALUE 

# YOUR CODE IS HERE 

o = np.std(x)
p = np.std(y)
print(p)
print(o)

Desired Output:

4.47213595499958
1.118033988749895
# ## <p style="background-color:#9d4f8c; font-family:newtimeroman; color:#FFF9ED; font-size:175%; text-align:center; border-radius:10px 10px;">Pandas Section</p>
# 
# <a id="1"></a>
# <a href="#toc" class="btn btn-primary btn-sm" role="button" aria-pressed="true" 
# style="color:blue; background-color:#dfa8e4" data-toggle="popover">Content</a>

# ### Import Pandas Library

# In[114]:


import pandas as pd


# ### Read Salaries.csv and take a look at the first 5 rows, df info and df statistical measurements.*

# In[193]:


# LET US READ Salaries.csv 

# YOUR CODE IS HERE 
a = pd.read_csv('/Users/macbookair/Desktop/Salaries.csv')
a


# In[135]:


# LET US LOOK AT THE FIRST 5 ROWS 

# YOUR CODE IS HERE 

a.head()


# Desired Output:
# 
# ![image.png](https://i.ibb.co/6BTmGX8/assignment1a.png)

# In[137]:


# LET US GET A SAMPLE 

# YOUR CODE IS HERE 

a.sample()


# Desired Output (WATCH OUT! Your output may NOT be the same as the one):
# 
# ![image.png](https://i.ibb.co/mcsCxxC/assignment1b.png)

# In[155]:


# YOUR CODE IS HERE 

Desired Output:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 148654 entries, 0 to 148653
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148045 non-null  float64
 4   OvertimePay       148650 non-null  float64
 5   OtherPay          148650 non-null  float64
 6   Benefits          112491 non-null  float64
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            0 non-null       float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB
# In[156]:


# LET US GET SOME DESCRIPTIVE MEASUREMENTS  

# YOUR CODE IS HERE 

a.describe()


# Desired Output:
# 
# ![image.png](https://i.ibb.co/ftMP67H/assignmnet1c.png)

# ### How many different year values are there?

# In[170]:


# YOUR CODE IS HERE 

a.groupby("Year").count()

Desired Output:

2014    38123
2013    37606
2012    36766
2011    36159
Name: Year, dtype: int64
# In[173]:


# LET US FIND THE NUMBER OF UNIQUE VALUES IN THE COLUMN OF "Year"

# YOUR CODE IS HERE 

print(a.Year.unique())

Desired Output:

4
# In[187]:


# LET US FIND THE UNIQUE VALUES IN THE COLUMN OF "Year"

# YOUR CODE IS HERE 

a.Year.unique()

Desired Output:

array([2011, 2012, 2013, 2014], dtype=int64)
# ### Print out max and avg values in the column of "Totalpay".

# In[203]:


# LET US FIND THE MAXIMUM TOTALPAY

# YOUR CODE IS HERE 

m = a["TotalPay"].max()
m

Desired Output:

567595.43
# In[209]:


# LET US FIND THE AVERAGE TOTALPAY

# YOUR CODE IS HERE 

n = a["TotalPay"].mean()
n

Desired Output:

74768.321971703
# ### How many records in the TotalPay column are there bigger than avg TotalPay?

# In[212]:


# YOUR CODE IS HERE 


# Desired Output:
# 
# ![image.png](https://i.ibb.co/nj84FbZ/assignment1d.png)

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

69489
# ### How much does ALBERT PARDINI make money (including benefits)?

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

2    335279.91
Name: TotalPayBenefits, dtype: float64
# ### Who is the lowest paid person?

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

148653    Joe Lopez
Name: EmployeeName, dtype: object
# ### What are the unique Jobs in dataset?

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

array(['GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY',
       'CAPTAIN III (POLICE DEPARTMENT)',
       'WIRE ROPE CABLE MAINTENANCE MECHANIC', ..., 'Conversion',
       'Cashier 3', 'Not provided'], dtype=object)
# ### List the top 3 least common Jobs in the dataset.

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

COURT COMPUTER FACILITIES COORDINATOR             1
AUTOMOTIVE BODY AND FENDER WORKER SUPERVISOR I    1
VICTIM & WITNESS TECHNICIAN                       1
Name: JobTitle, dtype: int64
# ### How many people earned more than avg in 2012?

# In[ ]:


# YOUR CODE IS HERE 

Desired Output:

20366
# ### How many people have a title of Manager in their jobs?

# In[ ]:


# USE APPLY FUNCTION

# YOUR CODE IS HERE 

Desired Output:

4110
# ### Take Id, EmployeeName, JobTitle, TotalPay and TotalPayBenefits columns with iloc and assign them as sal_new dataframe.

# In[ ]:


# YOUR CODE IS HERE 


# Desired Output:
# 
# ![image.png](https://i.ibb.co/ZgFCbPm/assignment1e.png)

# ### Take the columns betweeen EmployeeName and TotalPayBenefits with loc and assign them as sal_new df.

# In[ ]:


# YOUR CODE IS HERE 


# Desired Output:
# 
# ![image.png](https://i.ibb.co/s2CYS7H/assignment1f.png)

# ### Print out the names of the employees who earn more than min but less than avg.

# In[ ]:


# YOUR CODE IS HERE 


# Desired Output:
# 
# ![image.png](https://i.ibb.co/mtNB2TX/assignment1g.png)

# <p style="text-align: center;"><img src="https://docs.google.com/uc?id=1lY0Uj5R04yMY3-ZppPWxqCr5pvBLYPnV" class="img-fluid" 
# alt="CLRSWY"></p>
# 
# ## <p style="background-color:#FDFEFE; font-family:newtimeroman; color:#9d4f8c; font-size:100%; text-align:center; border-radius:10px 10px;">WAY TO REINVENT YOURSELF</p>
# 
# ________
