import numpy as np
import matplotlib.pyplot  as plt
# two arrays
x = np.array([0.053, 0.042, 0.029, 0.025, 0.017, 0.010, 0.008, 0.002], float)
F = np.array([3.55, 2.96, 2.31, 2.01, 1.50, 1.02, 0.697, 0.226],float)

# straight line
# Define the values of the gradient and the intercept
gradient = 66
intercept = 0.20

# Plot the points
plt.plot(x,F,'*g')

# which gives us an array for y of 66x + 0.2
plt.plot(x,x*gradient+intercept)
plt.show()