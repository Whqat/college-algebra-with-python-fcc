'''

 PROBLEM:


 "Car sales in Warrington for the first half of the 2009 year were down 46.733% from
 2008, when 1500 new cars were sold.

 How many car sales were there in 2009? (Approximately)"








 SOLUTION:

 So, in 2008, 1500 cars were sold. In the first half of 2009, car sales were down
 by 46.733%. Our objective is to find the approximate number of car sales in 2009.

 For that, we'll just multiply 1500 by 46.733%. But we have to convert 46.733% to
 it's original form. If you remember, we said that percentages are from 0 - 1, where
 1 is 100%, 0 is 0%, and 0.5 is 50%.

 -> Sales in 2009  =  1500 * (1 - 0.46733)   =  ~800 car sales.



 Let's graph this assuming this trend continues of sales going down 46.733% every year
 and find the year where 0 cars will be sold. (This is un-realisitc of course, we're
 just practicing.)

'''

import matplotlib.pyplot as plt

x1 = 0      # 2008
y1 = 1500
x2 = 1      # Year 2009
y2 = 800


# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)   
b = y1 - m*x1

print(f"y = {m}x + {b}")   # y = -700.0x + 1500.0


# For the graph
xmin = 0
xmax = 20
ymin = 0
ymax = 2000

y3 = m*xmin + b
y4 = m*xmax + b

# Basic setup
plt.axis([xmin,xmax,ymin,ymax])
plt.xlabel("Year")
plt.ylabel("Car Sales")

plt.grid(True)

plt.plot([xmin,xmax],[y3,y4], 'g')

plt.show()