import numpy as np

theta = float(input("Angle in degrees?"))
theta_rad = np.pi * theta/180
result = np.sin(theta_rad)

print ("sine of", theta,"is", result)