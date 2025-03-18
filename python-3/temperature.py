# This program adds a user provided increase to a set of
# temperatures in degrees Celsius

import numpy as np

temperature = np.array([17.5,12.1,23.0], float)

increase= float(input("What is the temperature increase?"))
# operates on all elements of the array, no iteration needed
new_temperature = temperature + increase

#print (new_temperature)
#temperature[1] += 0.1
#print("Updated by 0.1:", temperature[1])

temperature +=[0.1, 0.4, 0.3]
print(temperature)