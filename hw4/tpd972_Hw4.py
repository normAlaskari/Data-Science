# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:49:39 2020

@author: Norman
"""
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

x =  np.array([2005, 2006, 2007, 2008, 2009])
x2 =  np.array([5,6,7,8,9])
y =  np.array([12 ,19 ,29 ,37, 45])


model = linear_model.LinearRegression()
model.fit(x.reshape(-1, 1),y)

a=model.intercept_
b=model.coef_
L =  a + b *x

plt.plot(x, L)
plt.scatter(x,y)
plt.show()

print("\n")
print("************* Q1 Part-a *************\n")
print ("Y= 𝛼 + β * X = \n")
print ("least square regression line is 'Y' = ", a , "+", *b ,"* X = ", "[" , *L , "]" , "\n")
print ("a =" , b ,"\n")
print ("b =" , L[0],"\n")



print("************* A End ****************\n")

print("************* Q1 Part-b *************\n")
def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 100
    #for more accurate results 
    #iterations = 5000
    n = len(x)
    learning_rate = 0.0000002
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

gradient_descent(x,y)  

print("""We will not get the same result for the alpha and beta using
      the gradient descent since the square regression line sloves 
      for the optimal sloution by simply finding where the
      slope of the curve equal to 0.In contrast gradient descent finds the
      minminum value by taking a guess untill it reaches the best value so
      depending on the input the slope and intercept might be diffrent
      In order to get similler results we would have to scale down our years. 
      However, since gradient descent guess untill it reaches the best value 
      It can get close to the true slope and intercept, but it will 
      never be the exact same""")
       
print("************* B End ****************\n")


print("************* Q1 Part-c *************\n")
data = {'year':[2005, 2006, 2007, 2008, 2009],
        'sales':[12 ,19 ,29 ,37, 45]}

#one way of preduction
"""
Note: This is the exact same result that you’d have gotten if you 
put the value in the place of 
the x in the y = 8.4 * 7 + 11.6 equation.
""" 
data_c = pd.DataFrame(data=data)
x = data_c.year
y = data_c.sales

model = np.polyfit(x, y, 1)
predict = np.poly1d(model)
year = 2012
pred = predict(year)

#=========================
#seconed way of preducting
preduction2 = L[0] + b * 7
#=========================


# This is just additional to calculate the accuracy of the model
r2 = r2_score(y, predict(x))


print("In 2012, t = 2012 - 2005 = 7")
print("The estimated sales in 2012 are: y = 8.4 * 7 + 11.6 =", pred,"\n")
print("seconed way used to estimated = " , *preduction2)
print("************* B End ****************\n")


print("--------------------------- Q1  End ---------------------------\n")

nHead = np.random.binomial(n=16, p=0.5, size=10**5)

print("************* Q2 Part-a *************\n")
plt.hist(nHead, bins=range(18), color='#0066CC')
plt.title("Q2a: Hisrogram")
plt.ylabel("Number of Coins")
plt.xlabel("Number of Heads")
plt.show()
print("Please look at Graph")
print("---------------------\n")

print("************* Q2 Part-b *************\n")

counts = plt.hist(nHead, bins=range(18), density=True, color='#0066CC')
plt.xlabel('k')
plt.ylabel('P(nHeads = k)')
plt.title('Probability Mass Function')
plt.show()
print("Please look at Graph")
print("---------------------\n")


print("************* Q2 Part-c *************\n")

ecdf = np.cumsum(counts[0])
plt.plot(counts[1][:-1], ecdf)
plt.xlabel('k')
plt.ylabel('P(nHeads <= k)')
plt.title('Cumulative Distribution Function')
plt.show()

print("Please look at Graph")

print("---------------------\n")



print("************* Q2 Part-d *************\n")

tcdf = scipy.stats.binom.cdf(range(17), 16, 0.5)
plt.figure()
plt.scatter(ecdf, tcdf)
plt.xlabel('Empirical CDF')
plt.ylabel('Theoretical CDF')
plt.title('Q2d: scatter plot')
plt.show()
print("Please look at Graph")

plt.plot(range(17), ecdf, '-o', range(17), tcdf, ':d')
plt.legend(('Empirical CDF', 'Theoretical CDF'))
plt.xlabel('k')
plt.ylabel('CDF')
plt.title('Q2d: line plot')
plt.show()

print("Please look at Graph")
plt.loglog(ecdf, tcdf, 'o')
plt.xlabel('Empirical CDF')
plt.ylabel('Theoretical CDF')
plt.title('Q2d: log log plot')
plt.show()
print("Please look at Graph")



print("--------------------------- Q2  End ---------------------------\n")







