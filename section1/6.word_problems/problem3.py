'''
 PROBLEM:

 
 "You're given a graph of a company's earnings where:

 x-axis represents time in years since 1980 (0 = 1980)
 y-axis represents profit in thousands (meaning 1 = 1k, 1k = 1m, 10k = 10m)

 In the given graph, the points (5, 10000) and (25, 4000) are connected, you
 have no data before year 5 or after year 25

 Meaning that from 1985 to 2005, profits went down from 10m/year to 4m/year
 Which means that, each year, the profits went down by 2m
 
 Your mission is the following:
 
        1) Find the linear function y, where:
           -> y depends on x, the number of years since 1980
        
        2) Find and interpret the y-intercept (b)
        
    Good luck G"






 
 SOLUTION:


'''
# Year is x-axis, profits is y-axis

import matplotlib.pyplot as plt
import numpy as np

# first given datapoint
x1 = 5      
y1 = 10000
# second given datapoint
x2 = 25
y2 = 4000

m = (y2 - y1) / (x2 - x1) #slope
b = y1 - m*x1 #y-intercept

print(f"y = {m}x + {b}")  # The linear function (we completed first task wooho)
print(f"y-intercept = {b}") # completed second task, now we just gonna draw it

xmin = 0 
xmax = 40     # you can change this
ymin = 0   
ymax = 14000  # you can change this


y3 = m*xmin + b  # the value of y in our linear function if x is 0
y4 = m*xmax + b  # the value of y in our linear function if x is 40

# Basic setup  
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0], "r")
plt.plot([0,0],[ymin,ymax], "r")

ax.set_xlabel("Year")
ax.set_ylabel("Cases")
ax.set_xticks(np.arange(xmin, xmax, 2))    #optional (readability)
ax.set_yticks(np.arange(ymin, ymax, 1000)) #optional (readability)
ax.grid(True)

# draw the FULL LINE
plt.plot([xmin,xmax],[y3,y4], 'b')

plt.show()

# We could have also done this by defining a linear function "y" that takes in a
# year (x) and returns the predicted profits of the company of that year x:

#  def y(x):
#    return 10000 - 2 * x    ( -2*x because company going down 2000 a year in profits)