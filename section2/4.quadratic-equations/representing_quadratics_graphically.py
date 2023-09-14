import matplotlib.pyplot as plt
import numpy as np
import math

a = 1
b = 5
c = 6

print(f"y = {a}x² + {b}x + {c}") # Our quadratic equation

# Vertex
vx = -b/(2*a) 
vy = a*(vx**2) + b*vx + c 
print(f"Vertex: ({vx}, {vy})")

xmin = -10
xmax = 10
ymin = -10
ymax = 10

x = np.linspace(xmin,xmax) # np.linspace allows us to create a smooth curve by providing
#                          multiple points to plot. you can verify this by passing the
#                          number of points as a third parameter, 50 is the default.

# Basic setup
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Graph the parabola
y = a*x**2 + b*x + c 
plt.plot(x, y) 

# Plot the vertex point as a dot
plt.plot([vx],[vy], 'ro', markersize=3) 

# Find and plot the roots
discriminant = b**2 - 4*a*c 
if discriminant>=0: 
    # Find roots
    root_1 = (-b + math.sqrt(discriminant))/(2*a) 
    root_2 = (-b - math.sqrt(discriminant))/(2*a) 
    # Plot roots as dot
    plt.plot([root_1, root_2],[0,0], 'ko', markersize=3) 
    print("Roots: x =", root_1, "and x =", root_2)

plt.show() 