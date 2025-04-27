import numpy as np
import matplotlib.pyplot as plt

# some constants
planck_h = 6.626e-34
c = 2.998e8
#boltzman
k = 1.381e-23

# Data from the COBE satellite
# The data is provided in two arrays below.

# Measured data: wavelength is in millimetres
measured_lambdas = np.array([4.405286344, 3.676470588, 3.144654088, \
                             2.754820937, 2.450980392, 2.004008016, 1.834862385, 1.377410468, \
                             0.881834215, 0.468823254], float)
# Measured data: intensity in W m**-2 m**-1 sr**-1
# these are the intensites we compare our calculated values to, using root mean square
measured_intensities = np.array([3.10085E-05, 5.53419E-05, 8.8836E-05, \
                                 0.000129483, 0.000176707, 0.000284786, 0.00034148, 0.000531378, \
                                 0.000561909, 6.16936E-05], float)

# where we put the temperature and calculated intensities for that temp
resultingTempIntensitiesAndRMSDs = []


# calculate intensities lambdas (in mm) given a temperature
# (a float) using the  ...  verbose=True will report its working in a detailed way
# returned value are the calculated intensities
def intensitiesForTemperature(lambdas_in_mm, temperature, verbose):
    # for each lambda and temp combination, calculate
    # the result
    if verbose:
        print("With temperature", temperature, "wl=", " and measured lambda=", lambdas_in_mm)
    calculated_intensities = []

    # convert to metres
    lambdas_in_m = lambdas_in_mm * 1e-3

    # let's calculate the intensities from the temperature and measured lambdas
    for l in lambdas_in_m:
        partOneNumerator = (2 * planck_h * (c ** 2))
        partOneDenominator = (l ** 5)
        if verbose:
            print("partOneNumerator/partOneDenominator", partOneNumerator / partOneDenominator)
        expVal = planck_h * c / (l * k * temperature)
        if verbose:
            print("the exponent", expVal)
        partTwo = 1 / (np.exp(expVal) - 1)
        if verbose:
            print("1/ e^the exponent -1)", partTwo)
        res = partOneNumerator / partOneDenominator \
              * partTwo
        if verbose:
            print("for w=", l, ", the result is", res)
        calculated_intensities.append(res)
    return calculated_intensities


# given two arrays,1 what is the root mean square deviation?
# return this as a float
def rootMeanSquareDev(measured, calculated):
    numberOfValues = len(measured)
    squareOfTheDeviations = (measured - calculated) ** 2
    rmsd = np.sqrt(sum(squareOfTheDeviations) / numberOfValues)
    return rmsd


def plotResult(x, y, title):
    plt.title(title)
    plt.xlabel("wavelength / mm")
    plt.ylabel("intensity / W m^−2 sf^-1 m^-1")
    plt.plot(x, y)
    plt.show()
    return


# storage for the result with the lowest root mean square deviation that
# we have found by repeated guesses
currentLowestRMSD = None

# main loop
while True:
    temperatureAsText = input("Enter a temperature between 1 and 10 K, or q to quit > ")
    # we decided to exit
    if temperatureAsText == 'q':
        # there is something to plot, so plot the result
        if len(currentLowestRMSD) > 0:
            plotResult(measured_lambdas * 1e-3, \
                       currentLowestRMSD["intensities"],
                       "Intensities by wavelength for temperature " + \
                       str(currentLowestRMSD["temp"]) + " K")
        else:
            print("Bye!")
            exit(0)

    # optimistically convert the temperature to a float
    temperature = float(temperatureAsText)

    # calculate the intensities for this temperature
    calculatedIntensities = intensitiesForTemperature(measured_lambdas, temperature, False)

    # calculate the root mean square deviation for these intensities, compared with
    # measured intensities
    thisRMSD = rootMeanSquareDev(measured_intensities, calculatedIntensities)

    # test the result to see if it is better (lower) that the current guess
    # the first time, we just store it because it is automatically the minimum so far
    if currentLowestRMSD is None:  # first one, so this will be the best guess so far
        print("Saving the first result with a root mean square deviation of", thisRMSD)
        currentLowestRMSD = {"temp": temperature, "rmsd": thisRMSD, "intensities": calculatedIntensities}
    # compare the new root mean square deviation to one we have already stored
    # if it is lowest, replace it ...
    elif thisRMSD < currentLowestRMSD["rmsd"]:
        print("Your latest guess has a lower root mean square deviation (" \
              , thisRMSD, \
              ") than currently stored, so we are saving it ... ")
        currentLowestRMSD={"temp": temperature, "rmsd": thisRMSD, "intensities": calculatedIntensities}
    # the root mean square deviation cannot be lower that the one we already have, so let's
    # discard it
    else:
        print("No change to lowest root mean square deviation we've found so far (", \
              currentLowestRMSD["rmsd"], \
              " at temperature",
              currentLowestRMSD["temp"]), \
            ")"
