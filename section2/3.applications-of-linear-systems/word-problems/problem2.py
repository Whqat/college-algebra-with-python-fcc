'''
 PROBLEM:

 "Jessica is walking home from a friend's house. After 2 minutes she
 is 1.4 miles from home.

 Twelve minutes after leaving, she is 0.9 miles from home.

 What is her rate in miles per hour?"








 SOLUTION:

 We're going to graph this with python.

 We have our two data-points: (2, 1.4), (12, 0.9)

 But since we need the miles per *hour* we're going to convert the minutes to
 hours via dividing it by 60.


'''

import matplotlib.pyplot as plt
import numpy as np

x1 = 2/60   # 2 mins
y1 = 1.4    # 1.4 miles away
x2 = 12/60  # 12 mins
y2 = 0.9    # 0.9 miles away

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print(f"y = {m}x + {b}")    # y = -3x + 1.5, since we know the slope is -3, we can conclude that we're getting closer by 3 miles every hour. so the speed is 3 miles/hour


# For the graph
xmin = 0
xmax = 3
ymin = 0
ymax = 3

y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup
plt.axis([xmin,xmax,ymin,ymax])
plt.xlabel("Time in Hours")
plt.ylabel("Miles")

plt.xticks(np.arange(xmin,xmax,0.2))
plt.yticks(np.arange(ymin,ymax,0.2))
plt.grid(True)

plt.plot([xmin,xmax],[y3,y4], 'r')

plt.show()