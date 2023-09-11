"""
 Factoring is a way of breaking down a number into smaller numbers.
 The smaller numbers are called the factors of the original number.

 Imagine you have a cookie and you want to share it with your friends.
 You can cut the cookie into smaller pieces so that everyone gets a fair share.
 The smaller pieces are the factors of the cookie.

 In math, we use the word "factor" to mean the same thing as "piece".
 So, when we say "factoring a number", we
 mean "breaking the number down into smaller pieces".

 For example, the number 6 can be factored into 2 and 3. This means that
 6 is made up of 2 and 3, and that 2 and 3 divide evenly into 6.
 (by divide evenly, I mean divides into a whole, non-decimal number)
 

 Here are some other examples of factors:

 -> The factors of 15 are: 1, 15, 3, 5 
    (1*15 = 15, 3*5 = 15)

 -> The factors of 16 are: 2, 8, 4, 1, 16
    (2*8, 4*4, 1*16)

 -> The factors of 24 are 1, 24, 3, 8, 4, 6, 2, 12
    (1*24, 3*8, 4*6, 2*12)



 If you have the fraction 6/15 and you want to simplify it, what you
 do is you find a common factor between 6 and 15, in other words, a number
 that they're both divisible by. In our case, there's only one number which is
 3. So the simplified version of the fraction would be 2/5 (divided both sides by 3)

 6/15 is the same exact thing as 2/5 as long as you divide BOTH sides.



 Another example is the equation y = 4x + 16. 4 and 16 both have the common factor
 of 4, in other words they're both divisible by 4, so you can simplify the
 equation y = 4x + 16 to y = x + 4, but this would actually be wrong because the
 value of x would change completely. So to avoid this we simplify/factorize it this way:

  ->   y = 4x + 16   ->  y = 4(x + 4)

  To explain that, when you have a number * a bracket, you can multiply
  each element in the bracket by that number and just remove that number.
  So 4(x + 4) is the same as 4x + 16.



  Let's learn how to factorize and simplify a square root.
   
  First, we have to understand what a perfect square is.
  A number that is a perfect square is a number that can be generated by
  squaring (^2) a number. For example, 16 is a perfect square because it
  can be generated by squaring the number 4 (multiplying it by itself).

  Now we move on.

  We all know the square root of 25 is 5.

  We can conclude from that that the square root of 24 is almost 5. (repeating decimals)

  But how do we simplify the square root of 24?

  -> √24  (If we break 24 down by factorization and atleast one of it's factors is a perfect square, we can factorize this easily)
  
  -> √6*4 (4 is a perfect square! √4 = 2, we simplify this like the following:)

  -> 2√6  (kick perfect square out after square rooting it, it becomes 2√6, we have simplified it!)

  
   
 Now let's talk about the modulus operator and how we can use it find the
 factors of a number.

 But first, let me introduce you to the floor division operator: "//"
 The floor division operator performs normal division then rounds the
 result down to the nearest integer if the result is a decimal.
    i.e:   10 / 3 = 3.33    BUT    10 // 3 = 3

 When we floor divide two numbers, we are essentially asking how many times the
 first number fits into the second number.
 For example, 12 // 5 is 2 (with a remainder of 2)
 This means that 5 fits into 12 two times, with 2 left over.

 The remainder is the number that is left over after the division is complete.
 In this case, the remainder is 2.

 The modulus operator (%) is used to find the remainder when one number
 is floor-divided by another. So, 12 % 5 = 2 means that the remainder
 when 12 is divided by 5 is 2.

 Now, let's talk about factors. To recap, a factor of a number is a number
 that divides evenly into that number. For example, 5 is a factor of 10
 because 10 is divisible by 5 (with no remainders of course)

 So, why is 5 not a factor of 12?
 Because 12 isn't divisible by 5, it returns a decimal.
 And also because 12 can't be floor-divided by 5 with no remainder.
 When we floor-divide 12 by 5, we get 2 with a remainder of 2.
 This means that 5 is not a factor of 12.

 Here are some more examples:

 -> 10 % 2 = 0
  This means that the remainder when 10 is floor-divided by 2 is 0. (because 2 can fit into 10 5 times and nothing is left over)
  So, 2 is a factor of 10.
 
 -> 15 % 3 = 0
  This means that the remainder when 15 is floor-divided by 3 is 0. (because 3 can fit into 15 5 times and nothing is left over)
  So, 3 is a factor of 15.
 
 -> 18 % 4 = 2
  This means that the remainder when 18 is floor-divided by 4 is 2. (because 4 can fit into 18 4 times and 2 is left over)
  So, 4 is not a factor of 18.

 

 So now that we understand how the modulus operator can help us find out if a number
 is a factor by another number by floor-dividing it and checking if there's a remainder,
 we should be ready to implement this in python!
"""    

number = 12

# Find all factors of 12
for n in range(1,13): # Python will stop counting at 12
    if 12 % n == 0:
        print(f"{n} is a factor of 12.") # 1, 2, 3, 4, 6, 12 are factors of 12.

# Now I want you to try to implement the same logic with a fraction
# to try and simplify it. Go do it on your own now then check the solution below.



# SOLUTION:
def factorize_fraction(numerator, denominator):
   factor = None   # temporarily 
   smaller_number = min(numerator, denominator) # This will be the end of our range in our loop since any number % a number greater than it is always going to output the smaller number AKA 12 % 13 = 12, 12 % 15 = 12, etc.

   # Find greatest common factor
   for n in reversed(range(1, smaller_number+1)): # Reversed to get the GREATEST factor
      if numerator % n == 0 and denominator % n == 0:
         factor = n
         simplified_numerator = numerator // factor      # If you use / instead of // you'll get an integer ending with .0 so might as well remove it using floor division
         simplified_denominator = denominator // factor
         print(f"Fraction before simplification: {numerator}/{denominator}")
         print(f"Fraction after simplification: {simplified_numerator}/{simplified_denominator}")
         print(f"Common factor: {factor}") # 12
         return [simplified_numerator, simplified_denominator]

   return False

factorize_fraction(12, 24)

# Now that we're done with that, you remember that decimal-to-fraction function
# we wrote? Yeah, it was pretty bad because if you input a decimal that
# converts into a fraction with large numbers it won't simplify it.

# Now let's re-create the function but this time with simplifcation by
# getting the common factor and dividing our numerator and denominator by it.

# If you don't remember how the following code works, I suggest taking
# a look at the original code in chapter 4 "algebraic_functions.py" where I explain it in detail.
def decimal_to_fraction(decimal):
   
    if type(decimal) != float:
        return " You didnt even pass me a decimal bro\n"

    decimal_str = str(decimal)
    index_of_dot = int(decimal_str.find("."))

    exponent = int(len(decimal_str[index_of_dot:]) - 1) # length of decimal points after the dot
    
    numerator = int(decimal * 10**exponent) # Parsing to int because its float by default (because float * float)
    denominator = int(10**exponent)

    percentage = int(decimal * 100)

    simplified = factorize_fraction(numerator, denominator)

    if simplified:
      numerator = simplified[0]
      denominator = simplified[1]


    return f" Fraction: {numerator}/{denominator} \n Percentage: {percentage}%\n"


# decimal = float(input("\nEnter a decimal to convert: ")) # I added \n to seperate it from all the prints above

# print(decimal_to_fraction(decimal)) # Works everytime!




# Next level... Factorizing a square root with python.

# I want you to try this on your own before looking at the code below, because
# if you don't, you'll find yourself very confused.

# I warn you again, don't try to read the code before you try to implement
# this on your own. It took around an hour to come up with this and I myself would
# find this code confusing as if I saw it for the first time if I look at it tomorrow.

# As long as you come up with a working solution, you should be OK.

import math
# Number to factorize
def factorize_sqrt(n):
    print("\nInput:", n)

    if math.floor(math.sqrt(n))**2 == n:
        print("Square root:", int(math.sqrt(n)), "(Perfect)")
        return

    list_of_factors = [] #gonna be a list of tuples 

    for maybe_factor in range(1,n+1):
        if n % maybe_factor == 0:
            pair = sorted((maybe_factor, n//maybe_factor))
            list_of_factors.append(pair)

    list_of_factors = [tuple(v) for v in dict(list_of_factors).items()] # remove duplicates
    print("Factors:",list_of_factors) # [(1,12), (2,6), (3, 4)]

    for pair in list_of_factors:
        for number in pair:
            if math.floor(math.sqrt(number))**2 == number and number != 1: # if number is perfect square
                print(number, "is a perfect square")
                try:
                    his_bro = pair[pair.index(number)+1]
                except Exception:
                    his_bro = pair[pair.index(number)-1]
                print(f"Factorized: {int(math.sqrt(number))}√{his_bro}\n")
                return
    print("This can't be factorized further because none of it's factors is a perfect square\n")

factorize_sqrt(12)  # 2√3
factorize_sqrt(24)  # 2√6
factorize_sqrt(33)  # "This can't be factorized further because none of it's factors is a perfect square"
factorize_sqrt(25)  # 5 
factorize_sqrt(54)  # 3√6
factorize_sqrt(868) # 2√217