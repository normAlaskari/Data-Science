# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:29:46 2020

@author: Noor Alaskari
"""


import pandas as pd
import matplotlib.pyplot as plt


print("------------------------ Graph 1 -------------------------------")
data = pd.read_csv("fdata.csv")


dates = ['3','4','5','6','7']
Datez = data["Date"] 
Open = data["Open"] 
High = data["High"]
Low = data["Low"]
Close = data["Close"]

plt.plot(dates, Open, 'tab:blue',
         dates, High, 'tab:orange',
         dates, Low , 'tab:red',
         dates, Close , 'y-',)
# add a title
plt.title("financial data of Alphabet Inc")
# add a label to the y-axis
plt.legend(["Open","High","Low","Close"])

# add a label to the x-axis
plt.xlabel("Date")

plt.show()

print(" please see graph ubove\n")

print("------------------------ Graph 2 -------------------------------")


plt.plot(Datez, Close , 'r-o')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.title('Closing stock value of Alphabet Inc.') 
# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
plt.tick_params(which='both', # Options for both major and minor ticks
                top='off', # turn off top ticks
                left='off', # turn off left ticks
                right='off',  # turn off right ticks
                bottom='off') # turn off bottom ticks
plt.minorticks_on()
plt.show()

print(" please see graph ubove\n")

print("------------------------ Graph 3 -------------------------------")


Pg = [ "Java", "Python", "PHP", "JavaScript", "C#", "C++"]
Popularity=[ 22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(Pg, Popularity , color = "blue")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.title('Closing stock value of Alphabet Inc.') 
# naming the x axis
plt.xlabel('Languages')
# naming the y axis
plt.ylabel('Popularity')
plt.tick_params(which='both', # Options for both major and minor ticks
                top='off', # turn off top ticks
                left='off', # turn off left ticks
                right='off',  # turn off right ticks
                bottom='off') # turn off bottom ticks
plt.minorticks_on()
plt.show()

print(" please see graph ubove\n")

print("------------------------ Graph 4 -------------------------------")

languages = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']

x_pos = [i for i, _ in enumerate(languages)]
plt.barh(x_pos, Popularity, color='g')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of Programming Language")
plt.yticks(x_pos, languages)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


print(" please see graph ubove\n")

print("------------------------ Graph 5 -------------------------------")


weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 
weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 
weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]


plt.scatter(weight1, height1, marker='*', color= "r")
plt.scatter(weight2, height2, marker='*', color= "g")
plt.scatter(weight3, height3, marker='*', color= "b")
plt.xlabel('weight')
plt.ylabel('height')
plt.title('Group wise Weight vs Height scatter plot')
plt.show()

print(" please see graph ubove\n")



