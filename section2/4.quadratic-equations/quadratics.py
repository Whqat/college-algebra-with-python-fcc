"""
 Now, let's talk about Quadractics.

 The word "Quad", means "square".
 
 So x^2 (x squared) is a representation of a quadratic.

 You may be wondering, where does the "square" fit in? why is it ^2 and not ^4 if it's
 squared? What does "square" have to do with this? Isn't a square 4 sided?

 The idea behind this is that when you want to get the area of a square you
 multiply the length of it's sides by itself, meaning you exponentiate the side length
 by 2. Later on this just got referred to as "squaring" a number, which just means
 multiplying it by itself or exponentiating it by 2. That's where the notion of 
 quadratics comes from.

 When we graph a quadratic function, it's not gonna be a straight line like a linear
 function. It's going to be a "parabola" or a "U" shape.

 NOTE: When a negative number is squared, it becomes a positive value (i.e: -5^2 = 25)

 The general form of a quadratic function is as follows:

 y = Ax^2 + Bx + C

 As long as A has a value != 0, then the equation is a quadratic.

 If the value of A is positive, the graph will look like a 'U' shape. (smile)
 If the value of A is negative, the graph will look like a reverse 'U' shape. (frown)


 Question:

 "I dont understand what these quadratic functions represent. What are all
 these variables in y = Ax^2 + Bx + C? What do they represent?"

 Answer:

 A is the coefficient of the x^2 term. This term is called the quadratic term
 because it is the term that contains the square of the variable x.
 The coefficient A determines the shape of the parabola. If A is positive,
 the parabola is opened upwards. If A is negative, the parabola is opened downwards.

 B is the coefficient of the x term. This term is called the linear term because
 it is the term that contains the linear term of x. The coefficient B determines the
 direction of the parabola. If B is positive, the parabola opens to the right.
 If B is negative, the parabola opens to the left.

 C is the constant term. This term is called the constant term because it does not
 contain the variable x. The constant term C determines the y-intercept of the parabola.
 The y-intercept is the point where the parabola crosses the y-axis.

 x is the variable. This is the input of the function. The value of x can be any real number.

 y is the output of the function. This is the value of the function at a given input.
 The value of y is determined by the quadratic equation.

 
 A parabola does not end. It extends infinitely in both directions, although it may
 get closer and closer to the x-axis as the x-values become larger and larger.
 This is because the quadratic equation y = Ax^2 + Bx + C is a polynomial
 equation, and polynomial equations have infinitely many solutions.

 In other words, for any non-zero value of x, there is a corresponding value of
 y that satisfies the quadratic equation.
 Therefore, the parabola extends infinitely in both directions.

    NOTE: Both sides of the parabola are always symmetrical
    
 The vertex of the parabola is going to be the very top or bottom of the parabola,
 depending on whether the parabola is smiling or frowning.

 The equation for the x-coordinate vertex of an equation = -b/2a, where:

 -b is the negative (or positive if it's negative) value of the coefficient of x.
 2a is double the value of the coefficient of x^2

 To get the y-coordinate vertex you can just plug the value of the x-coordinate
 vertex into the equation.


 If you know the equation crosses the x-axis at some point,
 you can equate the quadratic formula to zero when you want to find the values
 of x that make the quadratic expression equal to zero. This is useful for finding
 the roots of a quadratic equation, which are the values of x that make the quadratic
 equal to zero. (i.e: y = Ax^2 + Bx + C  ->  0 = Ax^2 + Bx + C).

 But there's a better way to do this, you're almost always never going to know if it
 crosses the x-axis or not, therefor it's generally better to use the following
 equation:
    
 x = (-b ± √(b² - 4ac)) / 2a     (this is known as the quadratic formula)

 where:

 a is the coefficient of the x² term
 b is the coefficient of the x term
 c is the constant term

 You can use this to find the roots of ANY quadratic equation. If you noticed, there's
 a ± sign because we're going to add AND subtract. The reason for that is when a
 negative number is squared, it turns into a positive number.  x^2 = 16 -> x = ±4

    NOTE: In the quadratic formula, b² - 4ac is known as the "discriminant".
    The discriminant is a part of the quadratic formula that tells us the number and
    type of solutions to a quadratic equation.
    
    If the discriminant is positive, then the quadratic equation has two real solutions.
    If the discriminant is zero, then the quadratic equation has one real solution.
    If the discriminant is negative, then the quadratic equation has 0 real solutions.

    That's why it's generally better to get the discriminant first before trying to
    solve the entire equation. Because if the discriminant is negative then there's
    no point in moving forward.


    NOTE: The opposite of squaring is square rooting. Which means if you have
    the equation  x^2 = 16  you 'unsquare' the x by square rooting 16, so x = 4.


 To recap, there are only really two formulas you need to know:

 Vertex :  -b/2a
 Roots  :  (-b ± √(b² - 4ac)) / 2a  


 Moving to python.

"""
# Solving a quadratic equation

import math

# Coefficient values
a = 1
b = 5
c = 6


# Vertex

vx = -b/2*a     # x-coordinate of the vertex, we'll plug this into Ax^2 + Bx + C to get the y-coordinate of the vertex
vy = a*(vx**2) + b*vx + c   #  A(vx^2) + B(vx) + C

print(f"Vertex: ({vx}, {vy})") # Vertex: (-2.5, -0.25)

# Roots of the equation

discriminant = b**2 - 4*a*c # Get the discriminant first, because if it's negative we just stop calculating everything.

if discriminant >= 0: # if d not negative
    # (-b ± √(b² - 4ac)) / 2a
    root1 = (-b + math.sqrt(discriminant)) / 2*a
    root2 = (-b - math.sqrt(discriminant)) / 2*a

    if discriminant == 0:   # if disciminant is equal zero, there's only one root, and that root is the vertex of the parabola.
        print(f"Root: (x = {root1})")

    else:
        print(f"Roots: (x = {root1}, x = {root2})") # Roots: (x = -2.0, x = -3.0)

else:
    print("This quadratic equation has no real roots.")
