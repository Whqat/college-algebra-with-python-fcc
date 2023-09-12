'''
I'm going to show you how to use graphing to figure out if it's cheaper
to pay per session or buy a gym membership if you only go 2 times a week.

We're going to be graphing systems of equations:

A system of equations is a set of two or more equations that have
the same set of variables. The variables in a system of equations can be solved
for simultaneously to find the values that make all the equations true.

Systems of equations can be used to model many real-world problems, such as:

The cost of buying a gym membership vs. paying per session
The number of hours it takes to drive to two different cities
The number of students in a class who passed and failed an exam

Let x = time in weeks
Let y = money paid so far

Let's say the cost of a single gym session is $10, and the cost of a monthly
membership is $30. We can represent this with the following system of equations:

cost_per_session = 10 * 2x      # 2x means twice a week, so if x is 1 (week1) this means that we will have paid $20 in week 1, if we're in week 2 then its 10 * 4 which is 40, so by week 2 we will have paid $40
cost_of_membership = 30 * x/4   # x/4 because a month is approximately 4 weeks, so it's $30 every 4 weeks

Or, since we're going to be using the cost as y and time in weeks as x:

y = 10 * 2x  and  y = 30 * x/4

We can graph these equations as a system of lines.

The point where these two lines intersect is the solution to the system.
This point represents the number of gym sessions where the cost of
paying per session is equal to the cost of buying a membership.

Let's draw these lines in python


'''

# MONTHLY MEMBERSHIP: 50$
# COST PER SESSION: 10$

# We will evaluate which is better by comparing the cost paid so far for each
# week and decide what saves the most money in the long term.

import matplotlib.pyplot as plt
import numpy as np

xmin = 0     # time in weeks
xmax = 15    # 15 week period 
ymin = 0     # amount of money paid
ymax = 150   # $150 budget over 15 weeks

sessions_per_week = 1   # make this whatever you want

# Define the array of x values once (instead of having to plot "[xmin,xmax]"" we just pass "x")
x = np.linspace(xmin,xmax)

plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.xlabel("Time In Weeks")
plt.ylabel("Money Paid So Far")
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.xticks(np.arange(xmin,xmax, 1))
plt.yticks(np.arange(ymin,ymax, 10))

# line 1
y1 = 50*x/4 # Assuming a month is 4 weeks, our cost will be 50$ every 4 weeks
plt.plot(x, y1, label="Monthly Membership")

# line 2
y2 = 10*sessions_per_week*x
plt.plot(x, y2, label="Pay-Per-Session")

plt.grid(True)

plt.legend()  # Displays the labels

plt.show()

# As you can see, pay-per-session is better if we're going once a week. But
# if we're going more than once a week, getting the monthly membership is better.
