'''

 PROBLEM: 

 "A gym membership with two personal training sessions costs $125, while
 the same gym membership with five personal training sessions costs $260.
 
 What is cost per session?"









 SOLUTION:

 
'''

# If we can find the equation y = mx + b, we'll be able to know the cost per
# session. Where m represents the cost of a single session and b represents the
# cost of the membership. x represents the number of sessions, y represents total cost
# for the number of sessions. If we were to write this as a function it'd be:
# f(n) = cost-per-session*n + cost-of-membership. # Where n is the number of personal
# training sessions you'd like to have with your membership.

import matplotlib.pyplot as plt
import numpy as np

x1 = 2
y1 = 125
x2 = 5 
y2 = 260

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print(f"y = {m}x + {b}")   # y = 45.0x + 35.0,  where 45 is cost-per-session and 35 is gym membership cost


# For the graph
xmin = 0
xmax = 10
ymin = 0
ymax = 500

y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup
plt.axis([xmin,xmax,ymin,ymax])
plt.xlabel("Sessions")
plt.ylabel("Total Cost")

# plt.xticks(np.arange(xmin,xmax,0.2))
# plt.yticks(np.arange(ymin,ymax,0.2))
plt.grid(True)

plt.plot([xmin,xmax],[y3,y4], 'r')

plt.show()

# As you can see, the graph starts at point 35 in the y-axis because that's the cost
# of the membership. You're going to pay the membership anyways regardless of how
# many training sessions you have. That's why we add b to the equation y = mx.