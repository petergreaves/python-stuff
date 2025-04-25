import numpy as np

# given two arrays what is the root mean square deviation?
def rootMeanSquareDev(measured,calculated):

    numberOfValues = len(measured)
    squareOfTheDeviationsdeviations = (measured-calculated)**2
    rmsd = np.sqrt(sum(squareOfTheDeviationsdeviations)/numberOfValues)
    return rmsd

a = np.array([2, 9.042, 10.029], float)
b = np.array([3.5, 12.96, 14.31], float)

result=rootMeanSquareDev(a, b)
print("Using a=",a, ", b=", b)
print("the root mean square deviation is =",result)