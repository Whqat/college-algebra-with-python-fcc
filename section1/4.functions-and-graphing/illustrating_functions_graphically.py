# Let's now use matplotlib to represent our functions graphically
import matplotlib.pyplot as plt

# Same setup as last time, I just changed x and y min and max values
x_min = -10
x_max = 10
y_min = -10
y_max = 10

c = 0 #center is gonna be zero since min is -10 and max is 10

fig, ax = plt.subplots()

plt.axis([x_min, x_max, y_min, y_max]) # Setting x and y axis

# Now we draw our cartesian coordinates plane
#         -10      10     0 0   red
plt.plot([x_min, x_max], [c,c], "r")
#         0  0    -10     10    red
plt.plot([c,c], [y_min,y_max], "r")

# Now let's create our function and represent it in our graph

def f(n):  # Name it whatever you want, I went with f(n)
    return 0.5*n + 1  # Feel free to change this
    

for x in range(10):  # Get some sample inputs, I went with 0-9
    y = f(x) # y will represent the new value of x when passed through the function
    plt.plot([x], [y], 'bo') # draw a blue dot for each coordinate

plt.show() # As you can see, All the dots line-up. This means our function is "linear"

# In the next lesson, we'll illustrate our function as a line instead of a dot




