'''
 Functions in mathematics are similar to python functions

 Unlike python though, functions are usually called just "f", while
 in python you can name a function literally anything

 A mathematical function also takes in parameters (inputs) in parenthesis
 i.e: f(x)

 Here's an example of a mathematical function:

 Declaring the function

 -> f(x) = 2x + 3

 Passing an input (parameter in python)

 -> f(4) = 2 * 4 + 3  (2 * 4 can also be written as 2(4) in mathematics)


 Now let's apply this in python!

'''

# Declaring mathematical functions in python

# We're going to create a function and call it using a for loop and we want to print
# the inputs and outputs in a nice format:
#   x | f(x)
#   1 | 2            (when x is 1, f(x) is 2)
#   4 | 6            (when x is 4, f(x) is 6)
#   etc...

# So let's start by printing this before we get into the loop stuff because we only want this printed once
print("x | y")

def f(x):
     y = 4*x + 3  # function equivalent to f(x) = 4x + 3
     print(x, "|", y)

# Call the function and pass numbers from 1-3 as the parameters (input)
for n in range(1, 4):
     f(n)   

#     Output:
#      x | y     
#      1 | 7          when x is 1, y is 7
#      2 | 11         when x is 2, y is 11
#      3 | 15         when x is 3, y is 15



# Okay, now is the time you create a function that converts a decimal to a fraction.
# My solution will be down below. Go do it now or else... else I ain't finna do nothing


def decimal_to_fraction(decimal):
   
    # If passed decimal isn't a float, tell em he stupid for not passing a decimal
    if type(decimal) != float:
        return " You didnt even pass me a decimal bro\n"

#   NOTE: "\n" Creates a new line, this is not necessary and is just for readability

    # We'll get the length of decimal places by converting the passed decimal to a string
    # and finding the position of the "." and counting the length of digits after it
    decimal_str = str(decimal)
    index_of_dot = int(decimal_str.find("."))

#   length of decimal places
    exponent = int(len(decimal_str[index_of_dot:]) - 1)  # "- 1" because python counts the "." in len()
    
    # Top of fraction
    numerator = int(decimal * 10**exponent) # Parsing to int because its float by default (because float * float)
    
    # Bottom of fraction
    denominator = int(10**exponent)

    percentage = int(decimal * 100)

    return f" Fraction: {numerator}/{denominator} \n Percentage: {percentage}%\n"


print(decimal_to_fraction("cool string"))  # not a decimal
print(decimal_to_fraction(69))             # not a decimal

print(decimal_to_fraction(0.123)) 
print(decimal_to_fraction(0.234))  
print(decimal_to_fraction(0.9499))


#        Output:
#
#      You didnt even pass me a decimal bro
#
#      You didnt even pass me a decimal bro
#
#      Fraction: 123/1000
#      Percentage: 12%
#
#      Fraction: 234/1000
#      Percentage: 23%
#
#      Fraction: 9499/10000
#      Percentage: 94%