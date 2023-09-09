'''
 PROBLEM:

 "The town of Tola has population of 40,000 and produces
 13 tons of garbage each week. Express this information in terms of
 the function f and explain the meaning of f(5) = 2"










 SOLUTION:



'''

# We can go ahead and do the same basic setup and solve it by getting
# the slope and use population as x-axis and garbage as y-axis where
# our two datapoints would be (0,0) and (40,13)
#                             ^^ 0,0 because when population is 0 garbage/weeks would obviously be 0

# But I'm going to solve it another way by creating a function f where
# G = f(P)  ( garbage = value of function f when population is it's parameter )

# The reason I'm solving it this way is because I want to show you all the different
# ways you can solve these problems. If you don't get this solution, it's fine.

import matplotlib.pyplot as plt

def f(population):
    garbage_per_person = 13 / 40  # Calculate the average garbage produced per person
    G = garbage_per_person * population  # Calculate the total garbage produced
    return G  # G = f(P)

# Generate population values from 0 to 100
population_values = range(0, 101) # xmin-xmax

# Calculate garbage production for each population value
garbage_values = [f(population) for population in population_values]

# Basic configurations
plt.title("Garbage Production in Tola")
plt.xlabel("Population")
plt.ylabel("Garbage (tons)")
plt.grid(True)
plt.axis([0,100, 0,50])  # feel free to change this

# Plot the data
plt.plot(population_values, garbage_values)

plt.show()

# We were also asked to explain the meaning of "f(5) = 2" which basically means
# that if the population is 5000, 2 tons of garbage is produced per week.