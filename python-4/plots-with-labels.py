# Example program that includes axis labels in a plot

from numpy import array
import matplotlib.pyplot as plt

# Create two arrays
x_values = array([1,2,3,4,5,6,7],float)
y_values = array([1.9,2.1,3.6,4.2,4.9,5.7,6.4],float)

# PLot the points
plt.plot(x_values,y_values,'sr')
plt.xlabel('time / seconds')
plt.ylabel('position / metres')
plt.show()