'''
 Proportion: two equal ratios
 i.e: 2/4 and 5/10   (They can both be simplified down to 1/2)

 You can get two proportional ratios out of fraction form by
 cross-multiplying the diagonals
 i.e:   2     5
        -  =  -     is the same as 2*10 = 4*5
        4     10

 This method can be used to easily find the value of variables as shown below:
        3     x
        -  =  -     ->  3*4 = 6x  ->  12 = 6x  ->  x = 12/6 = 2
        6     4

 A quicker way to solve the previous example is to just do (3 * 4) / 6 since we already know we're gonna divide by 6 (because it's opposing the variable x)
'''

# EXAMPLE IN PYTHON  ( GETTING UNKNOWN VARIABLE'S VALUE )

# Our Proportion:
#   n1    n2
#   -  =  -
#   d1    d2

# Let the unkown variable's value be 'x' (I chose n2, you can choose any number)
proportion = {
    'n1': 1,
    'd1': 2,
    'n2': 'x',
    'd2': 16
}

# Now let's create a function to find the unkown variable in our dictionary
# LOGIC: Search through our dictionary for any unknown variables (classified as 'x')
# If none are found, we'll return "No unkown variables are found"
# But if we find any, we'll do our quick cross multiplication method
def get_unkown_variable():
    # If you don't use .items(), it'll only iterate over the keys
    for key, value in proportion.items():
        if value == 'x':
            if key == "n1":
                return proportion['d1'] * proportion['n2'] / proportion['d2']
            elif key == "d1":
                return proportion['n1'] * proportion['d2'] / proportion['n2']
            elif key == "n2":
                return proportion['n1'] * proportion['d2'] / proportion['d1']
            elif key == "d2":
                return proportion['n2'] * proportion['d1'] / proportion['n1']

    return "No unkown variables found"

# Call the function and print the returned value
print(get_unkown_variable())





# BONUS: EXTRA PROBLEMS

# 1) Dealing With Repeating Decimals:

# Let's say we have a repeating decimal called "x"

x = 0.666666

# Now, let's say we want to know what fraction "x" represents
# You might've been able to guess and say it represents two thirds (2/3)
# But how do we verify that? There's a secret formula!

# It starts by multiplying x by 10, so let's store that as a variable

y = x * 10     # 6.66666

# Now, we can say that y = 10x, if we subtract 10x by x we should get a whole number = 9x

z = y - x   # z = 6.66666 - 0.666666 = 6

# Since we know z is 9x, and it's value is 6, we can convert that into the following equation:

# 9x = 6  ->   x = 6/9 = 2/3 (two thirds)!

# You might've asked: What's the idea behind this? What's so special about 9x?
# Well that's because any repeating decimal multiplied by 9 gives a whole number.

# To get the fraction form of a repeating decimal (let it be X):

# We have to get it first in an equation form by getting 10x
# Then you get 9x in an equation form  -> 9x = 10x - x  (in the above example, it was 9x = 6)
# And from there you just divide by 9 and simplify the fraction using division if necessarry


# 2) Currency Exchange rates

# Let's say you were given the exchange rate from USD to CAD

#  1.00 USD
#   -- 
#  1.29 CAD

# Since you know 1 USD = 1.29 CAD, you can also calculate the value of 1 CAD in USD with proportion:
                    
#                  ( let it be x)
#  1.00 USD          ?.?? USD
#   ----       =      ----          ->  x = 1 * 1 / 1.29  -> 0.76 USD
#  1.29 CAD          1.00 CAD

# You can also use this to calculate any exchange rate, whether it be mile to km or currencies or whatever.






