'''
 PROBLEM:

 "A clothing business find there is a linear relationship between the number of shirts,
 n, it can sell and the price, p, it can charge per shirt. In particular, historical
 data shows that 1,000 shirts can be sold at a price of $30, while 3,000 shirts can
 be sold at a price of $22. Find a linear equation in the form
 p(n) = mn + b that gives the price p they can charge for n shirts."








 SOLUTION:


'''

import matplotlib.pyplot as plt

x1 = 1000
y1 = 30
x2 = 3000 
y2 = 22

# Since the price per shirt decreases as the number of shirts increases, we know
# the slope is negative. The slope, m, tells us how much the price per shirt
# changes when the number of shirts sold changes by one unit.

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print(f"y = {m}x + {b}")  # y = -0.004x + 34,  where -0.004 is how much the price of the
#                           shirt changes when the number of shirts increases by one unit.
#                           and 34 represents the price they charge for 1 shirt.


# For the graph
xmin = 0
xmax = 5000
ymin = 0
ymax = 50

y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup
plt.axis([xmin,xmax,ymin,ymax])
plt.xlabel("Shirts")
plt.ylabel("Cost / One")

plt.grid(True)

plt.plot([xmin,xmax],[y3,y4], 'g')

plt.show()