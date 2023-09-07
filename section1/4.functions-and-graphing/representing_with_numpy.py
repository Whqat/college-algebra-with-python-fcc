# Now we'll learn to use numpy arrays to represent our functions

# Numpy arrays allows us to do all the things we were doing before but
# without having to use for loops. It'll create an array which is similar
# to a python list that'll contain all our x values and y values (function values)


import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# Creating an array with x values between -9 and 9 (We'll use this to draw our line)
x = np.linspace(-3, 3)
# This will fill the array with enough values (including decimals)
# between -3 and 3 that'll allow us to draw a line (print it and see the chaos for yourself)


fig, ax = plt.subplots()

plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Let's create our function now (y array)
y = 2*x +1  # We dont have to create a for loop because numpy is cool

# Notice we don't have x and y between "[]" because they already are, thanks to numpy

plt.plot(x,y, 'pink') 

plt.show()