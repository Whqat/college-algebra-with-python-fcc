'''

 In this lesson, we'll look at how to solve systems of equations without graphing.

 If you don't remember, a system of equations is a basically a set of two
 or more equations that have the same variable. (i.e: x = 2y, x = y^2)

 Let's look at the following example:

 y = 3x + 10,    y = 4x

 These two y's have the same value except we don't know what the actual alue is.
 Since we know that the two y's are equal to each other, we can have their
 current values (3x+10, 4x) equate in an equation:

 -> 3x + 10 = 4x

 If you notice, we can subtract 3x from both sides (3x-3x = 0, 4x-3x = 1x = x)

 -> 10 = x

 -> y = 3(10) + 10 = 40

 OR

 -> y = 4(10) = 40



 When we're using sympy, the easiest way for us to solve systems of equations
 will be to make both the equations equal to zero and then just pass it to sympy:


 y = 3x + 10,     y = 4x

 -> 3x + 10 - y = 0         (Brought the isolated "y" in and flipped it's sign)

 -> 4x - y = 0              (Brought the isolated "y" in and flipped it's sign)

 NOTE:
    2 systems of equations are parallel when their slopes are equal & y-intercepts are different
    2 systems of equations are perpendicular when the product of their slopes is -1

 Let's transfer over to python.

'''

import sympy

x, y = sympy.symbols('x y')

# Equation set equal to zero


first = 3*x + 10 - y    # 3x + 10 - y = 0
second = 4*x - y    # 4x - y = 0  

#NOTE: When we pass these equations to sympy, they'll be equal to 0 by default.

print(sympy.linsolve([first, second], (x, y))) # output: (10, 40)