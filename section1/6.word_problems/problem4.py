'''
 PROBLEM:

 "In 2004, a school's population was 1,700. By 2012, it had grown to
 be 2,500. Assume the population is changing linearly.

 Your mission:

 1) How much did the population grow between 2004 and 2012?

 2) What is the average population growth per year?

 3) Find an equation of the school "P", "t" years after 2004

 NOTE: matplotlib is not needed, you do not need to graph this.

 NOTE: You don't have to use any code for the first question








 SOLUTION:

 1) It went from 1700 to 2500, to get the growth we just subtract:

 -> 2500 - 1700 = 800


 2) The average population growth per year is basically the rate of change
 per AKA the slope, we'll solve this using python:

'''

x1 = 0 # 2004
y1 = 1700 # population in 2004
x2 = 8 # 2012
y2 = 2500 # population in 2012

m = (y2-y1) / (x2-x1) # rate of growth

print(m) # output: 100.0

# This means that the average population growth per year is 100


'''
 3) OK, let's write down what the question says again:
   "Find an equation of the population "P", "t" years after 2004"

   First thing we can extract from that is that we can use either
   of the y = mx + b equation OR create our own function: P(t)

   I'll do both (in order) because why not lol
'''

# Method 1:

b = y1-m*x1

print(f"y = {m}x + {b}") # This is the function

# Method 2:

def P(t):
    return 1700 + t*100
#   OR
#   return m*t + b   (mx+b)

# NOTE: Mathematically speaking, if you want to be 100% accurate, you would name
# the function "f(t)"" and return P. But that isn't important, we're using python,
# we can name our functions whatever in python, whereas in math they're all
# named "f".
# But just so you know, in math language this would be P = f(t) because it's
# what's returned from the function f(t)
