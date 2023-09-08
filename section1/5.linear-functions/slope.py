'''

 In algebra, the slope of a line is a measure of its steepness.
 It is calculated as the rise over run, which means the change
 in the y-coordinate divided by the change in the x-coordinate.
 The slope can be positive, negative, zero, or undefined.

 A positive slope means that the line goes up as you move to the right.
 A negative slope means that the line goes down as you move to the right.
 A zero slope means that the line is horizontal.
 An undefined slope means that the line is vertical.

 The slope formula is:

 m = (y2 - y1)/(x2 - x1)

 where:

 *m is the slope
 *y2 and y1 are the y-coordinates of two points on the line
 *x2 and x1 are the x-coordinates of two points on the line

                                                x1  y1     x2 y2
 For example, if the two points on the line are (1, 2) and (3, 5),
 then the slope is:

 m = (5 - 2)/(3 - 1) = 3/2

 This means that the line goes up 3 steps for every 2 steps you move
 to the right.

 The slope of a line is a useful concept in algebra and geometry.
 It can be used to:

 *Find the equation of a line          i.e: y=2x+1
 *Compare the steepness of two lines
 *Solve problems involving lines
 *Find the rate of change and predict certain outcomes (only in linear equations since they're consistent)

 The slope of a line can be used to find the equation of the line,
 and vice versa.

 If we have the slope and we want to find the equation of that slope
 we can use the "slope-intercept formula"
 
 The slope-intercept form of the equation of a line is:

    y = mx + b

 where:

 y is the y-coordinate of a point on the line
 x is the x-coordinate of a point on the line
 m is the slope of the line
 b is the y-intercept, which is the point where the line crosses the y-axis
 
 The y=mx+b formula can be used to get the value of any of the above

 Example: getting just the equation

 slope = 2        (m)
 y-intercept = 3  (b)

 y = mx + b

 y = 2x + 3     (The equation used/linear function)


 Example: getting b (y-intercept)

 Point on the line of the equation = (1,1)
 Another point on the same line = (2,4)

 y2 = 4
 y1 = 1
 x2 = 2
 x1 = 1

 slope = y2-y1 / x2-x1  =  4-1 / 2-1  =  3 / 1  =  3   (m)

 x = 1 (or 2)
 y = 1 (or 4)

 -> y = mx + b

 -> 1 = 3(1) + b

 -> 1 = 3 + b

 -> -2 = b   AKA   b = -2


 Here's a practical real-world example:

 Say you want to predict the number of people who have the flu
 by a specific year. Let's say that year 0 is the starting point,
 and year X is the year that you want to predict the number
 of people who have the flu.

 x-axis: year , y-axis: flu cases   (it's a convention to always put time as our x-axis)

 The data points that you have are (0, 10) and (3, 30).
 The first point tells you that there were 10 people who had the flu
 in year 0, and the second point tells you that there were 30 people
 who had the flu in year 3.

 The slope of the line will tell you how many more people are 
 expected to have the flu each year. In this case,
 the slope is (30 - 10) / (3 - 0) = 20/3.
 This means that you expect the number of people who have
 the flu to increase by 20/3 each year.

 Since we now have the slope (m), we can get the y-intercept (b),
 which is the point where the line intercepts the y-axis.

 You can get it through just using the given data points as your
 x and y  in  y = mx + b since you already have the slope:
 
 10 = 20/3*0 + b  -> 10 = 0 + b  ->  b = 10

 OR, since you understand that b represents the intercepted part of
 y-axis, you can extract it instantly by understand that when x is 0
 in a given point, that point is on the y-axis (intercepting it), and
 the first data point we have is (0,10) where x is 0 and y is 10 which
 means that the point is on the y-axis at coordinate 10 so it intercepts
 it at 10, therefor b = 10
 

 So, if you want to predict the number of people who
 will have the flu in year 5 (x=5), you can use the slope
 to calculate the value of y (cases) when x is equal to 5 (year).

 For example, if Y is 6, then you would calculate:

 -> y = mx + b
 -> y = 20/3 * 6 + 10
 -> y = 40

 This means that you predict that there will be 40 people who have the
 flu in year 6.

 Of course, this is just a prediction. The actual number of
 people who have the flu may not always follow this trend.
 However, the slope-intercept form can be a useful tool
 for making informed predictions about future outcomes.

 Here are some other things to keep in mind when using the
 slope-intercept form to predict certain outcomes:

 *The more data points you have, the more accurate your prediction
 *The more evenly-spaced the given data-points, the more accurate the prediction


 NOTE:
 If you know the slope of a line, you can plug it into
 the slope-intercept form of the equation to find the equation
 of the line. And if you know the equation of a line, you can plug it
 into the slope-intercept form to find the slope of the line.

 Time for python :)

'''

# Slope in python

# Let's start by creating a simple function to calculate the slope for us

def slope_of(y2,y1,x2,x1):  # Take y2 y1 x2 x1 as parameters (input)
    try:
        return (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return "Slope is undefined"

# Let's test it works:

print(slope_of(4, 1, 2, 1))   # 3.0  (3/1)
print(slope_of(5, 2, 3, 1))   # 1.5  (3/2)
print(slope_of(0, -2, 2, 0))  # 1    (2/2)
print(slope_of(1, 0, 1, 0))   # 1    (1/1)
print(slope_of(2, 5, 1, 1))   # Undefined (-3/0)


# Now let's merge what we just learned with matplotlib

# The point of this code is to show how to find the equation of a line
# and then plot the line on a graph. The code can be modified to find the
# equation of any line and to plot the line on any graph.

import matplotlib.pyplot as plt

# Our 2 data points
x = 1
y = 7
x2 = 2
y2 = 10

# Develop the equation y = mx + b
m = slope_of(y2, y, x2, x) # This gives us the rate of change
# To get b, we can isolate it in y=mx+b by subtracting both sides by mx
b = y - m*x          
print(f"y = {m}x + {b}")  # This is the equation

# For the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# For the line on the graph
y3 = m*-10 + b 
y4 = m*10 + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Plot the linear function as a red line
plt.plot([-2,3],[y3,y4],'r')

plt.show()