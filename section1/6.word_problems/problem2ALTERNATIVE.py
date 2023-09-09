# ADVANCED ALTERNATIVE

# Don't feel down if you don't understand this, this is a more advanced solution.

# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the linear function that models the number of people afflicted by the common cold
def C(t):
  """
  This function takes the year as input and returns the number of people afflicted by the common cold.

  Args:
    t: The year (an integer)

  Returns:
    The number of people afflicted by the common cold (an integer)
  """

  # The number of people afflicted by the common cold decreases by 50 each year.
  return 875 - (50 * t)

# Create a list of years, starting from 0:20 (2004:2024)
years = np.arange(0, 30)

# Calculate the number of people afflicted by the common cold for each year
colds = C(years)

print("years", years, "\ncolds", colds)

# Plot the number of colds vs. the year
plt.plot(years, colds)

# Add labels to the axes

plt.xlabel("Year")
plt.ylabel("Number of Colds")
plt.grid(True)
plt.axis([0,30, 0,900])
# Add a title to the plot
plt.title("Number of People Afflicted by the Common Cold")

# Plot is ready to be show, you can use plt.show() now.

# OPTIONAL:
#----------------------------------------------
# Find the year when no one will be afflicted (approximation)
lowest_number_of_colds = int(min(abs(colds)))
year = np.where(colds == lowest_number_of_colds)[0][0] + 2000 - 4

# Print the year
print("No one will be afflicted in the year", year) # approximates to 2013 while other solution approximated to 2014 (answer is 2013.5)
#----------------------------------------------

# Show the plot
plt.show()

