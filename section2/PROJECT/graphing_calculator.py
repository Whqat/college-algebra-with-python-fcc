'''

 For this challenge, you need to create a graphing calculator using Python.
 This challenge is not going to be a "piece of cake", it took me like 2 days
 to complete.


 LEVEL 1: AMATEUR

 Create a function for each of the following:

 - Display the graph for any "y=" equation input
 - Solve a system of two equations without graphing
 - Graph two equations and plot the point of intersection
 - Given a, b and c in a quadratic equation, plot the roots and vertex


 LEVEL 2: INTERMEDIATE

 Create a menu that has the following options:

 1) Display the graph for any "y=" equation input
 2) Solve a system of two equations without graphing
 3) Graph two equations and plot the point of intersection
 4) Given a, b and c in a quadratic equation, plot the roots and vertex

 Prompt the user with an input to choose which option he'd like, and depending on
 that choice, call a function that performs that option.


 LEVEL 3: TOP G

 Create a class 'GraphingCalculator' that has the method "get_menu()" as well as a
 method that performs each of the following:

 1) Display the graph for any "y=" equation input
 2) Solve a system of two equations without graphing
 3) Graph two equations and plot the point of intersection
 4) Given a, b and c in a quadratic equation, plot the roots and vertex

 When the get_menu method is called, it should display a menu of all the possible
 methods the function is capable of (just print the enumerated list of options above).
 It should then prompt the user with an input to choose which method from the menu
 he'd like to run. depending on his input, call that specific function.




 MY SOLUTION: (LEVEL 3)

'''

import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import math

class GraphingCalculator:
    def __init__(self):
        self.options = ["Display the graph and a table of values for any 'y=' equation input",
           "Solve a system of two equations without graphing",
           "Graph two equations and plot the point of intersection",
           "Given a, b and c in a quadratic equation, plot the roots and vertex"]

    def get_menu(self):
        print("MENU:\n-------------------------------------------------------------------")
        for i, o in enumerate(self.options):
            print(f"{i+1}) {o}")

        option = int(input("\nChoose a function from the menu: ") )

        if option == 1:
            self.graph_and_table()
        elif option == 2:
            self.solve_system()
        elif option == 3:
            self.graph_two()
        elif option == 4:
            self.plot_quad()


    def graph_and_table(self):
        eq = input("Enter an equation with variable 'x': y = ")
        #TABLE
        cols = ('x', 'y')
        table_x = 0
        table_y = sympify(eq.replace("x", str(0)))
        rows = [[table_x,table_y]]
        for a in range(1,11):
            equation = sympify(eq.replace("x", str(a)))
            rows.append([a, equation])

        plt.table(cellText=rows, colLabels=cols, cellLoc='center', loc='upper left')
        plt.show()
        #GRAPH
        xmin, xmax, ymin, ymax = 0, 10, 0, 10

        x = np.linspace(xmin,xmax)
        y = [sympify(eq.replace("x", str(i))) for i in x]
        plt.grid(True)
        plt.axis([xmin, xmax, ymin, ymax])
        plt.plot(x, y ,'r')
        plt.show()

    def solve_system(self):
        eq = input("Enter a system of 2 equations seperated by a comma: y = ")
        sep = eq.strip().split(",")
        x = symbols('x')
        first = sympify(sep[0])
        second = sympify(sep[1])
        print(first, second)
        sol = nonlinsolve([first, second], [x])
        print(sol.args)
        try:
            print("x =", sol.args[0][0])
            try:
                print("x =", sol.args[1][0])
            except:
                pass
        except IndexError:
            print("No solutions found")

    def graph_two(self):
        eq = input("Enter 2 equations with var 'x' equal to zero seperated by a comma: 0 = ")
        sep = eq.strip().split(",")
        x = symbols('x')
        line1 = sep[0]
        line2 = sep[1]
        xmin, xmax, ymin, ymax = 0, 100, 0, 100
        xvals = np.linspace(xmin,xmax,350)
        y1 = [sympify(line1.replace("x", str(i))) for i in xvals]
        y2 = [sympify(line2.replace("x", str(i))) for i in xvals]

        # Plot the lines
        plt.plot(xvals, y1, label=line1)
        plt.plot(xvals, y2, label=line2)

        # If intersects, plot the intersection.
        xlist = []   # Median of possible x's in range of tolerance (for intersection)
        ylist = []   # Median of possible y's in range of tolerance (for intersection)
        for i in range(len(y1)):
            if abs(y1[i] - y2[i]) <= 0.5: #0.5 is our tolerance value
                xp = xvals[i]
                yp = y1[i]
                xlist.append(xp)
                ylist.append(yp)
        else:
            if xlist and ylist:
                xm = np.mean(xlist)
                ym = np.mean(ylist)
                plt.plot([xm], [ym], 'ro', markersize=3, label=f"Intersection: ({round(xm, 2)}, {round(ym, 2)})")


        plt.axis([xmin,xmax,ymin,ymax])
        plt.grid(True)
        plt.legend()
        plt.show()


    def plot_quad(self):
        print("Equation: ax² + bx + c")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        xmin, xmax, ymin, ymax = -100, 100, -100, 100
        plt.axis([xmin,xmax,ymin,ymax])
        plt.grid(True)
        plt.plot([xmin,xmax], [0,0], 'b')
        plt.plot([0,0], [ymin,ymax], 'b')

        # Plot parabola
        x = np.linspace(xmin,xmax,300)
        y = a*x**2 + b*x + c
        plt.plot(x, y, 'k')

        # Plot roots
        discriminant = b**2-4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            plt.plot([root1], [0], 'rx', label="Root 1", markersize=4)
            plt.plot([root2], [0], 'rx', label="Root 2", markersize=4)
        elif discriminant == 0:
            root = (-b + math.sqrt(discriminant)) / (2*a)
            plt.plot([root], [0], 'rx', label="Root", markersize=4)

        # Plot vertex
        vx = -b/(2*a)
        vy = a*vx**2 + b*vx + c
        plt.plot([vx], [vy], 'm+', markersize=4, label="Vertex")

        plt.legend()
        plt.show()


calc = GraphingCalculator()
calc.get_menu()
