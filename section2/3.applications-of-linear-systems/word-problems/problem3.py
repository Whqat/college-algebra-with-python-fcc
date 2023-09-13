'''
 PROBLEM:

 Determine whether the numbers given by the pair equations below are parallel,
 perpendicular, or neither

 1. 4x - 7y = 10            2. 3y + x = 12
    7x + 4y = 1                -y = 8x + 1





 SOLUTION:

 We're going to graph these with python and see if they're parallel, perpendicular,
 or neither.

'''

# Surprisingly, we don't even need matplotlib to graph these!

# We can actually use sympy to plot one-variable expressions, meaning we can plot
# these systems of equations 4x-7y=10 and 7x+4y=1 OR, better yet, 4x-7y-10 = 0 and 7x+4y-1 = 0.
# You don't have to make them equal to zero but it's just easier to pass to
# sympy that way.
# We can literally plot these two lines with dummy x values and sympy will get the
# y values for us and we will be able to tell if the two lines are intersecting,
# parallel, or neither.

from sympy import symbols, linsolve
from sympy.solvers import solve
from sympy.plotting import plot


x, y = symbols("x y")

# First pair
eq1 = 4*x - 7*y - 10    # Notice we brought the 10 in and flipped it's sign so the equation is equal to zero by default which is simpler for sympy to handle
eq2 = 7*x + 4*y - 1

solution = linsolve([eq1, eq2], (x, y))

for a in range(len(solution.args)):    # If you don't use .args it'll return some weird "FiniteSet"
    x_solution = solution.args[a][0]
    y_solution = solution.args[a][1]
    print(f"Solution:  x = {x_solution},   y = {y_solution}") # we're not gonna use these values, just printing them out because why not

# We want to know if the lines are intersecting we dont need to know what the lines
# actually so we'll just use dummy x values and then use the expression from y1 and y2 as y values

y1 = solve(eq1, y)
y2 = solve(eq2, y)

print(y1, y2) # [4*x/7 - 10/7], [1/4 - 7*x/4]  (yes sympy can graph these expressions)

# Before we use sympy's built-in plot funcitons, read this:

"""
plot(*args: Any, show: bool = True, **kwargs: Any) -> Plot
Plots a function of a single variable as a curve.

Parameters
args :
    The first argument is the expression representing the function of single variable to be plotted.

    The last argument is a 3-tuple denoting the range of the free variable. e.g. (x, 0, 5)
    (Accepts a second argument if you want to plot two equations)
"""
x = symbols("x")
xmin = -10
xmax = 10

plot(y1[0], y2[0], (x, xmin, xmax), ylim=(xmin, xmax))

# The value of variable "x" in the expressions of y1 and y2
# will be between xmin and xmax (our dummy values for x)

# If you dont make sure the ylim is the same as xmin and xmax,
# the graph may appear incorrectly.

# As you can see the lines are perpendicular

# Now just change the two equations eq1 and eq2 to see if the other pair
# is perpendicular or parallel



