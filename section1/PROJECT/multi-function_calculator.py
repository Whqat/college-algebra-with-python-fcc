'''

    For this challenge, you will be creating a multi-function-calculator.

    I've decided to create 3 different levels for this project where the first
    level is the easiest and the third is the hardest. I made it this way
    so that both python amateurs and python experts can do this project.


    Level 1: Amateur

    Create python functions that take input and do the following:

    Solve proportions
    Solve for x in equations
    Factor square roots
    Convert decimals to fractions and percents
    Convert fractions to decimals and percents
    Convert percents to decimals and fractions


    Level 2: Intermediate

    Define a different function for each of the following:

    Add, subtract, multiply, divide
    Detect prime numbers
    Generate prime factors of a number
    Simplify square roots
    Solve for a variable

    Each function should prompt the user with a question,
    take input, and output the answer.

    
    Level 3: Top G

    Define a class called "MultiFunctionCalculator" that has the following methods:

    Add, subtract, multiply, divide
    Detect prime numbers
    Generate prime factors of a number
    Simplify square roots
    Solve for a variable

    The class must have a method called "get_menu" which prints
    a numbered list of all it's methods and asks the user for input to choose
    which method they'd like to call by inputting the number of that method.
    After the user inputs a number, a unique description of the method should
    be printed and the method should be called.
    
    Here's an example of what I mean:

    calculator = MultiFunctionCalculator()
    calculator.get_menu()

    OUTPUT:

    Menu:
    1) add
    2) subtract
    3) multiply
    4) divide
    5) is_prime
    6) prime_factors
    7) simplify_sqrt
    8) solve_var

    Choose a function from 1-8: 5

    You chose 'is_prime: Checks if a number is prime.

    Enter number to check if prime: 13
    True
    



    Good luck G. I left my own solution down below. (LEVEL 3)

'''

import math, sympy

class MultiFunctionCalculator():

  def __init__(self): # on initialziation
    self.functions = {
      "add": {
          "description": "Returns the sum of the input numbers (Takes unlimited input of numbers)",
          "input": "Enter numbers to sum sepereated by a comma: "
      },
      "subtract": {
          "description": "Subtracts passed numbers from each other (Takes unlimited input of numbers)",
          "input": "Enter numbers to subtract sepereated by a comma: "
      },
      "multiply": {
          "description": "Multiplies all passed numbers together. (Takes unlimited input of numbers)",
          "input": "Enter numbers to multiply seperated by a comma: "
      },
      "divide": {
          "description": "Divides all input numbers by each other. (Takes unlimited input of numbers)",
          "input": "Enter numbers to divide seperated by a comma: "
      },
      "is_prime": {
          "description": "Checks if a number is prime.",
          "input": "Enter number to check if prime: "
      },
      "prime_factors": {
          "description": "Returns all prime factors of a number. (if any)",
          "input": "Enter number to check for prime factors: "
      },
      "simplify_sqrt": {
          "description": "Simplifies a square root expression.",
          "input": "Enter a square root (without the symbol) to simplify: √"
      },
      "solve_var": {
          "description": "Solves an equation for a variable.",
          "input": "Enter an equation and the symbol of the equation (i.e:   2*x+1, x): "
      }
  }
    # displaying the menu
  def get_menu(self):
    print("Menu:")
    for i, func in enumerate(self.functions):
      print(f"{i+1}) {func}")

    choice = int(input("\nChoose a function from 1-8: "))

    for i in range(len(self.functions)):
      if choice-1 == i:
        print(f"\nYou chose '{list(self.functions.keys())[i]}': {list(self.functions.values())[i]['description']}\n")
        q = input(list(self.functions.values())[i]["input"])
        func = list(self.functions.keys())[i]
        
        # calling function and passing input "q" (for question) as parameter
        if func == "add":
          para = [int(n) for n in q.strip().split(",")]
          print(self.add(*para))

        elif func == "subtract":
          para = [int(n) for n in q.strip().split(",")]
          print(self.subtract(*para))

        elif func == "multiply":
          para = [int(n) for n in q.strip().split(",")]
          print(self.multiply(*para))

        elif func == "divide":
          para = [int(n) for n in q.strip().split(",")]
          print(self.divide(*para))

        elif func == "is_prime":
          print(self.is_prime(int(q)))

        elif func == "prime_factors":
          print(self.prime_factors(int(q)))

        elif func == "simplify_sqrt":
          print(self.simplify_sqrt(int(q)))

        elif func == "solve_var":
          eq, symbol = q.strip().split(",")
          print(self.solve_var(sympy.sympify(eq), symbol)) # sympy.sympify 'unstrings' a string equation
          

  # the class methods
  def add(self, *args):
    return sum(args)

  def subtract(self, *args):
    result = args[0]
    for number in args[1:]:
      result -= number
    return result

  def multiply(self, *args):
    result = 1
    for number in args:
      result *= number
    return result

  def divide(self, *args):
    result = args[0]
    for number in args[1:]:
      result /= number
    return result

  def is_prime(self, n):
    if n == 1 or n == 0:
      return False
    for i in range(2,n):
      if n % i == 0:
        return False
    return True

  def prime_factors(self, n):
    return [i for i in range(1, n+1) if n%i == 0 and self.is_prime(i)]

  def simplify_sqrt(self, n):
    if math.floor(math.sqrt(n))**2 == n: # aka if sqrt of that number aint decimal we chillin
      return int(math.sqrt(n))

    for num in reversed(range(1, n)): # reversed to find the greatest one
      if n % num == 0 and math.floor(math.sqrt(num))**2 == num and num != 1:
        largest_perfect = num
        n1 = math.floor(math.sqrt(largest_perfect))  # perfect square
        n2 = math.floor(n / largest_perfect)         # his bro (pair)
        return f"{n1}√{n2}"
    return f"√{n}"

  def solve_var(self, eq, var: str):
    x = sympy.symbols(var)
    return sympy.solvers.solve(eq, x)


calculator = MultiFunctionCalculator()
calculator.get_menu()