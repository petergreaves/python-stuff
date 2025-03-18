# Calculate the product of the mass (in kg) and the
# speed (in m/s) of a  set of objects

import numpy as np

mass = np.array([3.1,0.98,2.6,154], float)
speed = np.array([0.21,1.63,0.88,0.76], float)

momentum = mass*speed

print ('momentum is',momentum,'in kg m/s')

ke=0.5 * mass*(speed**2)
print ('kinetic energy is',ke,'in J')

