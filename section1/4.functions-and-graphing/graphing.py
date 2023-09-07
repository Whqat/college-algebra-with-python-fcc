'''

 In this lesson, we'll learn how to represent functions with graphs.

 Let's say we have the function 'f(x) = 2x + 3' and we want to represent
 it with a graph.

 Let's get some sample inputs in, and their value in f(x)

    x | f(x)
    0 | 3
    1 | 5
    2 | 7


 Now to draw these points on the cartesian coordinates plane,
 just draw a dot at (0,3) , (1,5), (2,7) and connect them all together


 If you actually drew that with pen and paper, you'll see that the points
 are actually *linear*. It's just one straight line. This type of
 function is called a "linear" function


 Now let's do this in python! (yes we can draw graphs in python lol)

'''

# Graphing functions with the "matplotlib" library 

# First, install the library with "pip install matplotlib" so you import it

# We're going import the pyplot sub-library from matplotlib as "plt", which means we dont have to type pyplot() we just do plt()
import matplotlib.pyplot as plt

# I want to draw a graph where the x-axis and the y-axis go from 0-5

# Start by defining the length of the axiis(?) as variables
x_min = 0
x_max = 5
y_min = 0
y_max = 5

# Then we initialize a graph
fig, ax = plt.subplots() #fig = figure, ax= axis
# I know it looks confusing but it's how you initialize a graph with matplotlib

# Set the graph's axiis using our min and max values
plt.axis([x_min, x_max, y_min, y_max])  # Don't forget to put them in a list []

# Show the graph
plt.show()


# What if we want to make it look more like a cartesian coordinates plane?

# For that, we can just use the plt.plot() function to draw a "+" shape:

#NOTE: If you don't comment out the previous plt.show() It'll pop-up 2 windows (you have to close the first for the second to show)

# We're going to make 2 perpendicular lines passing through the center, center = 5/2 = 2.5
c = 2.5 # c for center

#        x-axis  y-axis color
plt.plot([0,5], [c, c], "r")  # This draws a horizontal line passing through the center

                     # b for blue
plt.plot([c, c], [0,5], "b")  # This draws a vertical line passing through the center

# Before we use plt.show(), let's also draw a random dot on the graph

#         x    y    g = green, d = make the dot diamond-shaped (there's other shapes like o for circle)
plt.plot([4], [2], "gd")

plt.show() # Should be a "+" shape with a green dot at (4,2)
