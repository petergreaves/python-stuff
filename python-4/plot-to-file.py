# Example program that plots a set of points using matplotlib
# and saves the figure in a file in PNG format

from numpy import array
import matplotlib.pyplot as plt

# Create two arrays
x_values = array([1,2,3,4,5,6,7,8],float)
y_values = array([0.3,1.2,2.7,3.6,4.2,4.6,5.2,7.4],float)

# Plot the points
plt.plot(x_values,y_values,'>b')

plt.savefig("figure.png")