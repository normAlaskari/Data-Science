# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#%% Q1
print("\n Q1: \n")
a=np.array([[2,8,4],[5,4,2]])
b=np.array([[4,1],[6,4],[5,3]])
c=np.array([[4 ,1 ,2],[6 ,4 ,3],[5, 3, 4] ])
d=np.array([[4 ,1 ,2],[6 ,4 ,3]])
print("\n Part A: \n")
print("the result: A * B = \n",np.dot(a,b))
print("\n Part B: \n")
print("the result: A * C = \n",np.dot(a,c))
print("\n Part C: \n")
print("the result: A * D = \n",
      """This will retrun an error: Matrix A
      and D cannot be multiplied together because the 
      "number of columns in A ≠ the number of rows in D.""")
print("\n-----------------------End-----------------------\n")

#%% Q2
print("\n Q2: \n")
print("\n Part A: \n")
print("""\nThe formula for calculating a z-score is is z = (x-μ)/σ, where x is the raw score, μ is the population mean,
and σ is the population standard deviation.\n""")
def zscore(numArray):
 return (numArray - np.mean(numArray))/np.std(numArray)
x = np.array([50, 68, 74, 70, 65, 61, 63, 74, 62])
y = np.array([170, 173, 209, 130, 215, 127, 108, 152, 183])
zx= zscore(x)
zy = zscore(y)
plt.scatter(zx, zy)
plt.xlabel('Zscore of x')
plt.ylabel('Zscore of y')
plt.show()

print("\n Part B \n")
print("\nplease look at the graph\n")


print("\n Part C \n")


pearson_def= zx.dot(zy)/len(x)
 

print("my personal corrcoef methods", pearson_def,"\n")
print("corrcoef function in numpy library personal Answer",np.corrcoef(x,y)[0,1],"\n")
print("both my answer and numpy are the same expet the last digit")

print("\n---------------------End-------------------------\n")

#%% Q3

print("\n Q3: \n")
x = np.array([ 50, 68, 74, 70, 65, 61, 63, 74, 62, 20])
y = np.array([170, 173, 209, 130, 215, 127, 108, 152, 183, 800])

print("\n Part A: \n")
print("Pearson correlation coefficient is",np.corrcoef(x,y)[0,1])

print("\n Part B: \n")
x_rank = np.argsort(np.argsort(x))
y_rank = np.argsort(np.argsort(y))

print("Spearman Rank Correlation Coefficient is",np.corrcoef(x_rank, y_rank)[0,1],"\n")

print("\n Part C: \n")
print("the two coefficients are not the same, Spearman is more appropriate since our measurements taken from ordinal scales")

print("\n Part D: \n")
print("1 means a postive Correlation , -1 means a negtive Correlation",
      ",Finally 0 means there are no Correlation")

print("\n---------------------End--------------------------\n")

#%% Q4

print("\n Q4: \n")
amswer1 = norm.cdf(0.5)- norm.cdf(-0.5)

print("Answer 1 is :", amswer1)

amswer2 = 2*(0.5-norm.cdf(-0.5))

print("Answer 2 is :", amswer2)

print("\n---------------------End-------------------------\n")

#%% Q5


print("\n Q5: \n")
print("\n Part A: \n")

print("a: X’ =  X’ ~ N(aμ+b, a^2 σ^2 )")

print("\n Part B: \n")

print("b: If X ~ N(μ, σ^2 ),","Then Z = (X- μ)/ σ ~ N(0, 1)",
      "This is called Z-transformation or standardization.")

print("\n Part C: \n")

print("c: normal distribution is ", norm.cdf(7,5,3)-norm.cdf(2, 5, 3))

print("\n Part D: \n")

print("d: standard normal distribution is ", norm.cdf(1.5)-norm.cdf(-1.5))
print("\n-------------------End----------------------------\n")

#%% Q6

print("\n Q6: \n")
print("\n Part A: \n")
print("P(A U B) = P(A) + P(B) – P(A ∩ B)")
print("\n Part B: \n")
print("P(A | B) = P(A ∩ B) / P(B)")
print("\n Part C: \n")
print("P(A ∩ B) = P(A | B) * P(B)")
print("\n Part D: \n")
print("P(A ∩ B) = P(A) * P(B)")

print("\n---------------------End--------------------------\n")



#%% Q7
print("\n Q7: \n")
print("(P(d = even and d < 5) = 1/4) == (P(d = even) * P(d < 5) = 1/4), therefor it is independent ")

print("\n--------------------End---------------------------\n")

#%% Q8

print("\n Q8: \n")
print("0.5^4 * 0.01 / (0.5^4 * 0.01 + (1/6)^4 * 0.95) = 0.81")

print("\n----------------------End------------------------\n")



#%% Q9
print("\n Q9: \n")
print("\n Part A: \n")
print("If we consider the following  N = test positive and  S = has disease\n")
print("p(S) = 1/1000 = 0.0001 ")
print("p(N | S) = 99.9% = 0.999")
print("p(N | S`) = 0.002% = 0.0002\n")
print("Using the complement rule\n")
print("p(S`) = 1- p(S) = 1- 0.00001 = 0.9999 \n")
print("Using Bayes theorem\n")
print("a: 0.999*0.0001/ (0.999 * 0.0001) + (0.0002 * 0.9999) ≈ 0.3331")
print("\n Part B: \n")
print("Using the complement rule\n")
print("p(S`) = 1- p(S) = 1- 0.00001 = 0.9999")
print("p(N`|F`) = 1 - p(N|F`) = 1-0.0002 = 0.9998")
print("p(N`|F) = 1 - p(E|F)= 1-0.999 = 0.001\n")
print("Using Bayes theorem\n")
print("0.9998* 0.9999 / (0.001 * 0.0001)+(0.9998 * 0.9999 ≈ 0.99999989997  \n")
print("\n---------------------End--------------------------\n")
#%% load data

print("\n Q10: \n")
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

measlesSum = []
for row in range(len(measles)):
    measlesSum.append(np.sum(measles[row][1:]))
    
mumpsSum = []
for row in range(len(mumps)):
    mumpsSum.append(np.sum(mumps[row][1:]))
    
mumpsSumMonth = []
for col in range(len(mumps[0,1:])):
    mumpsSumMonth.append(np.sum(mumps[1,col+1]))

chickenPoxNew = []
chickenPoxNewPos = np.argsort(chickenPox[0:,0])
chickenPoxNew.append(chickenPox[chickenPoxNewPos])

[chickenPoxNew] = chickenPoxNew 
chickensSum = []
for row in range(len(chickenPoxNew)):
    chickensSum.append(np.sum(chickenPoxNew[row][1:]))

# close all existing floating figures
plt.close('all')

#%% Q9.a. plot annual total measles cases in each year

plt.figure()
plt.title('Fig 1: NYC measles cases')
plt.scatter(measles[0:,0], measlesSum[0:], marker=(5, 2))
plt.plot(measles[0:,0] , measlesSum[0:])
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.show()

print("\n Part A: Please look at graph \n")


#%% Q9.b bar plot average mumps cases for each month of the year

plt.figure()
plt.title('Fig 3: Average monthly mumps cases')
plt.bar(range(1,13,1) , mumpsSumMonth)
plt.xlabel('Month')
plt.ylabel('Average number of cases')
plt.show()

print("\n Part B: Please look at graph \n")


#%% Q9.c scatter plot monthly mumps cases against measles cases
mumpsCases = mumps[:, 1:].reshape(41*12) 
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('Fig 4: Monthly mumps vs measles cases')
plt.ylabel('Number of Meales Cases')
plt.scatter(mumpsCases,measlesCases)
plt.show()




#%% Q9.d plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('Fig 5: Monthly mumps vs measles cases (log scale)')
plt.loglog(mumpsCases, measlesCases, '.')
plt.ylabel('Number of Meales Cases')
plt.show()

print("\n Part D: Please look at graph \n")


#%% Answer to Q9.e

print("\n Part E:\n")

# complete this part here
answer = """we usually use liner for small incresing values , However, for logarithm scale we use 
exponentially increasing values and we use it for  displaying numerical data over a very wide range of values in a compact way"""

print('\n\nAnswer to Q9.e: ' + answer)

print("\n----------------------End-------------------------\n")