# In this final lesson, we'll learn to customize or matplotlib graph
# to make it look even cooler!

# Let's start with a normal setup

import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

x = np.linspace(-7, 7) # numpy array so we can draw a line from -7 to 7

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Some new stuff:
ax.set_xlabel("our horizontal x axis")  # Label the x axis
ax.set_ylabel("our vertical y axis")  # Label the y axis
ax.set_title("cool graph lol") # Label the graph
ax.grid(True)  # make it hit the griddy

# The following allows us to change the step value of our axis values
# i.e: if x-axis = -10, -9, -8, etc., using step of 2 makes it go -10, -8, -6, etc...
ax.set_xticks(np.arange(xmin, xmax, 2))
ax.set_yticks(np.arange(ymin, ymax, 2))

# Now let's draw our cool line

y = 2*x + 1 #create y array (automatically does the for loop because numpy is cool)

plt.plot(x, y, label="y=2x+1") # create a line
plt.plot(x, y*2, label="cool line")  # create second line because why not
# ^^Notice both the lines will intersect at the x-axis
# because their x values are the same
plt.plot([3], [7], "ko", label="KO dot") # black round dot

plt.legend() # This creates a box at the top-right of the screen to display our labels

plt.show()