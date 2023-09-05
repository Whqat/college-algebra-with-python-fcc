'''

 Solving For X: Finding the value of the unknown variable

 In this lesson, we'll learn how to solve for x using python!

 If you're not very familiar with solving algebraic equations, here's
 a quick guide:

 Whatever you see in the equation, you generally want to do the opposite
 in order to find the value of the unknown variable.

 Here are some examples:

 1)  x + 3 = 5

 In order to solve this, it'd be nice if x was alone on one side,
 meaning that instead of x + 3 = 5 if would be x = something that we can calculate

 So let's start by simply stating "x = (something)"

 ->  x = (something)

 In order to get the value of that something, we have to look at
 the full equation:  x + 3 = 5

 It'd be nice if we can remove that '+ 3' because it'll be much easier to calculate
 The way we do that is by subtracting 3 from each side of the equation:

 -> | x + 3| = 5  |  -> x + 3 - 3 = x, 5-3 = 2
    |  (-3)| (-3) |

 -> x = 2
 
 Let's look at one more example to really hammer it in

 2)  x - 2 = 10

    We would like x to be alone, so we'll add 2 on each side
    (The reason we're adding and not subtracting this time is
    because it's -2 and not +2. If you remember we said earlier you
    should generally be doing the opposite of what the equation gives)


 -> x - 2 = 10     ->     x - 2 + 2 = x, 10+2 = 12
     (+2)  (+2)


 -> x = 12

 Same thing goes for multiplication and division, if the number next
 to x's symbol is multiplication, we should divide. If it's division, we should multiply.

 NOTE: In mathematics, when a number is multiplied by x, the multiplication
 symbol is usually not written
 i.e: 3x  ==  3*x

 NOTE: x multiplied by 1 is usually written as "x" and not "1x"

 Now let's complicate things a little, what if there were two
 numbers on x's side, meaning there were 2 symbols?

 Here's what I mean:  4x + 6 = 22   (4x is multiplication, + 6 is addition)

 This is actually not complicated at all, we'll do exactly what we did
 before but in two steps.

 As a rule of thumb, in equations where you're finding unknown variables
 you should get rid of the +'s and -'s before the *'s and /'s, which
 is contrary to what we always used to do in mathematics, which is starting
 with the multiplication. But as I said earlier, you generally want to
 do the opposite. So let's start with getting rid of the + 6

 ->  4x + 6 = 22  -> 4x + 6 - 6 = 4x, 22 - 6 = 16
        (-6) (-6)
 

 ->  4x = 16      -> 4x/4 = x, 16/4 = 4
     (/4) (/4)

 ->  x = 4
`1
 
 Now we'll learn how to solve for x using python

'''

# Solving for x with python

# We'll need to import a library called "sympy" which automatically
# solves for x and returns the unknown variables value

# You have to pip install it first with "pip install sympy" in your terminal

import sympy

# You have to declare the variable 'x' as a sympy symbol in order for sympy to understand
x = sympy.symbols("x")

# Equation  (The other side of the equation is equal to zero by default)
eq = 2*x - 4    #NOTE: We used 2*x instead of 2x because python can't understand 2x

print("x = ", sympy.solvers.solve(eq, x))   # Should be equal to 2

# If you want to learn more about sympy and how to use it, you can read the docs at (https://docs.sympy.org/)


