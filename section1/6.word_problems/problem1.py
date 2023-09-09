'''
 In this chapter, we'll use python to solve mathematical
 word-problems related to what we've learned

 I highly encourage trying to solve the problems on your own before
 seeing the solution as it'll really help you understand why things
 were a certain way and it'll also challenge your knowledge thusfar.

 We're going to use pretty much all we've learned till now. I highly recommend
 going back to chapter 5 and really making sure you grasp the concept
'''


'''
 Problem 1)

 A town's population increases at a constant rate. In 2010 the population
 was 55,000. By 2012, it was 76,000. If this trend continues, predict
 the population in 2016.





 SOLUTION: 



'''

'''
 THOUGHT-PROCESS:

 In the problem, we are given the population of a town in 2010 and 2012.
 We are told that the population is increasing at a constant rate,
 so we can assume that the population in 2014 and 2016 is also
 increasing at a constant rate.

 We can use the slope equation to find the rate of change of the population. The slope equation is:

 m = (y2 - y1) / (x2 - x1)
 where m is the slope, y1 is the population in 2010, y2 is the population in 2012, x1 is 2010, and x2 is 2012.

 Plugging in the values from the problem, we get:

 m = (76 - 55) / (2 - 0) = 10.5
 This means that the population is increasing by 10,500 people per year.

 We can use the slope equation to predict the population
 in 2014 and 2016. To do this, we need to find the y-value
 for x = 4 (2014) and x = 6 (2016). NOTE: 2010 = 0, 2011 = 1, 2012 = 2, etc.

 For x = 4, the y-value is:

 -> y = mx + b = 10.5(4) + 55 = 97

 For x = 6, the y-value is:

 -> y = mx + b = 10.5(6) + 55 = 118

 Therefore, the population in 2014 is predicted to be 95,000
 and the population in 2016 is predicted to be 115,000.

 Now let's do this in python
'''

# A common theme in these word problems is taking the "measurable"
# things and putting them at the x and y axis.

# In our case, I'll put "time" as our x-axis and "population" as y-axis

import matplotlib.pyplot as plt
import numpy as np
import sympy # OPTIONAL

# I'm going to start counting the years this way for readability:
# 0 for 2010, 2 for 2012, 4 for 2014, 6 for 2016 (These are our x values)

# And for the population we'll just put the first two digits:
# 55 for 55,000, 76 for 76,000  ( These are our y values )

x1 = 0    # 2010
y1 = 55   # 55,000

x2 = 2    # 2012
y2 = 76   # 76,000

m = (y2 - y1) / (x2 - x1)  # The rate of change is 10.5 AKA 10,500 a year
b = y1 - m*x1   # intercepted part of y-axis

print(f"y = {m}x + {b}")  # Our equation

xmin = 0   #Time
xmax = 10
ymin = 0   # Population
ymax = 130  

# Setting start and end points for the y-axis (for x-axis it'll just be default min and max 2010-2020)
y3 = m*xmin + b  # xmin = 0 = 2010, y3 = 55   ( START )
y4 = m*xmax + b  # xmax = 10 = 2020, y4 = 160  ( END )

# Basic setup  
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0], "b")
plt.plot([0,0],[ymin,ymax], "b")
#^This isnt a "+" shape because we passed 0,0 and not the center/median

ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.grid(True)
ax.set_xticks(np.arange(xmin,xmax,1))   # 1 step for x-axis
ax.set_yticks(np.arange(ymin,ymax,10))  # 10 steps for y-axis (because max is 130 duh)

plt.plot([xmin,xmax], [y3,y4], 'orange')

# You can plt.show() now, the following is optional:

# We can actually draw a dot on the graph right
# where the population at 2016 is using the equation we got.

# We're going to use sympy to get the value of y (population) at
# point 6 in the x-axis (2016):

#NOTE: Please take a look at the 2nd chapter if you don't know how sympy works

y = sympy.symbols("y")

#                   mx+b = y
equation = sympy.Eq(m*6+b, y)

#              round/approximate to nearest integer         [0] because solve() returns a list
dot_position = round(sympy.solvers.solve(equation, symbols=y)[0])

#        2016   population   blue circle     markersize=3 for small circle
plt.plot([6], [dot_position], "bo", markersize=2)

print(f"Predicted population in 2016: {dot_position},000")

plt.show()