'''
 In this lesson, we'll look at converting decimals to fractions and
 fractions to decimals. I'm going to assume you have basic knowledge
 about decimals and know what is a tenth, a hundredth, and a thousandth

 If we have the decimal 0.234 for example. Since we know that the last
 digit of the decimal is a thousandth, then we know that in order to
 conver this decimal to an integer, we'd have to multiply it by a thousand,
 and if we want to conver it back we'd divide it by a thousand, which is
 234/1000 which is:

   234
   ---    And there you go, it's now a fraction
   1000


 A simpler way to put it is just to divide it the decimal by it's "length"
 which in our case was a thousand

 If we have repeating decimals, we already know how to do this from the first
 lesson. A faster way to do that though, is to just divide the repeating
 decimal by 9, so if the decimal is 0.55555555, the fraction form would
 be 9/5:

    9
    -
    5

 But there's an exception for this case. We can't always just divide the
 repeating decimal by 9, let's look at this example:

 Repeating decimal: 0.090909090909

 If you remember, we used to get the 10x so that the number on the left side
 isnt zero, then we used to subtract the value of 10x by the value of x
 which in our case would be:

 10x = 0.9090909090
   x = 0.0909090909
 -------------------
  9x = 0.8181818181 ???

 If you remember, the reason we want 9x is to get a whole number we
 can actually solve in an equation, i.e: 9x = 6
 But in this case, we got a decimal, and that both the tenth
 position in the decimal was a zero, so we didn't get an actual
 number on the left side of the decimal which ruined our equation.

 Here, you can't just memorize stuff, you have to understand that we were
 multiplying by 10 to have a real number on the left side that's not equal to zero
 i.e: x = 0.4444444   ->   10x = 4.44444
 But in the case of 0.09090909, we'd have to multiply by 100 to get
 the nine on the left side of the decimal:

   x = 0.090909090909
   
   100x = 9.0909090909

   Now we subract 100x by x to get a single integer:

   100x - x = 99x = 9.0909090 - 0.9090909 = 9

   Therefor, 99x = 9

   Now we have an equation we can solve:

   Divide each side by 99 so the x is alone (so it becomes x = "something")
   x = 9/99

   9/99 can be simplified down 1/11 since they're both divisible by 9

   Therefor, the fraction form of x is 1/11:

      1
      -
      11
   


   Now let's learn a bit about percentages

   To calculate the percentage of a decimal/fraction, you first have to
   understand that the integer 1 is 100%, and 0 is 0%.

   We can then conclude that 0.5 is 50%, 0.55 is 55%, 0.67 is 67%

   So you see, the first two decimal places are the percentage

   So if we have the fraction 234/1000, we can convert that easily into
   a decimal by understand that the decimal form will be a thousandth
   of 234, which is 0.234

   To convert that decimal now to a percentage we just take
   the first to decimal places (tenth and hundredth) and there you go!

   0.234 in % = 23.4%


  We'll soon be converting fractions to decimals and decimals to fractions
  by writing our very own function, but we first have to understand how
  exponents can help us convert:

  TABLE OF EXPONENTS
----------------
  10^10 = 100  
  10^100 = 1000
  10^1 = 10
  10^0 = 1
  10^-1 = 0.1
  10^-2 = 0.01
----------------
  Converting to decimal to fraction using exponents:

  decimal = .33

  numerator = decimal * 10^length-of-decimals -> 0.33 * 10^2
  -> 0.33 * 100 = 33  (This is the first number in the fraction)
  
  denominator = 10^length-of-decimals -> 10^2 = 100 (Second number in the fraction)

  Therefor, fraction of .33 = 33/100

  Here, we can call the length-of-decimals the "exponent" since it's the
  exponent of 10 in our method

  Now let's do this in python!

'''
#NOTE: # The exponent operator in python is **, not ^

# Converting decimal to fraction using python

# The input function will return our decimal in a string format
decimal_in_string_format = input("Enter a decimal to convert: ")

# To perform mathematical operations, we have to convert it into a
# "float" which is basically a decimal in python:

decimal = float(decimal_in_string_format)

# Now let's define the length of the decimals in a variable
# But first, you have to understand that python will count the dot
# in the decimal in the computed length, meaning that the
# length of .33 will be computed as 3 and not 2 because python counts
# the ".", therefor, we'll have to subtract the computed length by 1

# We have to convert the returned length into an integer using int()
# to perform mathematical operations on it (len returns a string)
exponent = int(len(decimal_in_string_format) - 1)
 # ^^ In python, you can't use len() on floats,
 # so we used it on the string of the decimal

# Now let's get the numerator and the denominator like we did earlier

# We'll parse it to int because it'll be a float by default
# since we're multiplying two floats (if decimal is .33, numerator would've been 33.0 instead of just 33)
numerator = int(decimal * 10**exponent) 

# Denominator is going to be the 10^length-of-decimal-places
denominator = int(10**exponent)

# We can also get the percentage (the first two decimal places)
# by multiplying the decimal by 100, which will push the first two
# decimal places to the left side (before the ".")

percentage = decimal * 100

print(f"Fraction: {numerator}/{denominator}")
print(f"Percentage: {percentage}%")

# Now this only works if the input decimal starts with "." and not with "0",
# and that's because the len() function will compute 0 as part of the length.

# You can deal with that by writing a function that checks if the first
# digit in the input is 0, and if it is, just remove the 0. That's your HW LOL