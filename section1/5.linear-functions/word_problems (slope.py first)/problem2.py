'''
 PROBLEM 2:

 "The number of people afflicted by the common cold in the winter
 months dropped steadily by 50 each year since 2004 until 2010.

 In 2004, 875 people were inflicted.

 Find the linear function that models the number of people
 afflicted by the common cold C as a function of the year: "t".

 When will no one be afflicted?"
 





 



 SOLUTION:



'''

# The year is gonna be our x-axis and the amount of people inflicted
# will be the y-axis

import matplotlib.pyplot as plt
import numpy as np
import sympy

# We'll start counting the years from 0

x1 = 0    # 2004
y1 = 875  # inflicted

x2 = 6    # 2010
y2 = 575  # inflicted  875 - (50*6) = 575  (because there's a 6 year difference where each year it drops by 50)

#NOTE: Since we need two points to get the slope and we were given only
# one, we had to get another one. I chose to get the point representing
# 2010 but you can get the point for 2005 and just make x2 = 1 and 
# y2 = 875 - 50 = 825

m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print(f"y = {m}x + {b}")  # Our equation

xmin = 0   # Years
xmax = 20  # feel free to change this  
ymin = 0   # Cases
ymax = 900 # feel free to change this


y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup  
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0], "b")
plt.plot([0,0],[ymin,ymax], "b")

ax.set_xlabel("Year")
ax.set_ylabel("Cases")
ax.grid(True)

plt.plot([xmin,xmax],[y3,y4], 'y') # y for yellow

# You can plt.show() it now and it should work as expected. But I want to print the year
# where no one will be afflicted, for that, we'll use our equation with sympy

# We want to get the year when the cases are 0, in other words: get x when y is 0:

x = sympy.symbols("x")

#                   mx + b = y (y = cases = 0)
equation = sympy.Eq(m*x + b, 0)

# give me value of symbol "x" from that equation
solution = sympy.solvers.solve(equation, x)[0] #[0] because solve() returns list, dont ask why it returns a list.

# solution returns 18, we want the year so we'll add 2000 and subract 4 because 2004 is starting point
solution_in_year_format = round((solution + 2000) - 4) # we round it because we dont want decimals

print(f"By {solution_in_year_format}, no one will have a common cold")

# Let's also put a little dot there:
#       x (year)  y (cases)
plt.plot([solution], [0], 'ro', markersize=3)  # ro for red circle

plt.show()

# Now, this solution works well, but there's a more efficient way to 
# do this. I'll leave that solution in "problem2ALTERNATIVE.py"


