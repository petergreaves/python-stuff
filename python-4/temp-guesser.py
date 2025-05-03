# This program prompts the user for a temperature.  It then calculates the root mean square
# deviation between a blackbody spectrum at the temperature and the measured data, and then
# reports the root mean square deviation value back to the user. The user can then enter either
# q to quit, or further guesses until a minimum value for the root mean square deviation value
# is found corresponding to the best fit temperature. On completion, the program plots the
# initial data points and a smooth blackbody curve for the best-fit temperature.
import numpy as np
import matplotlib.pyplot as plt

# some constants
planck_h = 6.626e-34
c = 2.998e8
k = 1.381e-23

# Data from the COBE satellite
# The data is provided in two arrays below.

# Measured data: wavelength is in millimetres
measured_lambdas = np.array([4.405286344, 3.676470588, 3.144654088, \
                             2.754820937, 2.450980392, 2.004008016, 1.834862385, 1.377410468, \
                             0.881834215, 0.468823254], float)
# Measured data: intensity in W m**-2 m**-1 sr**-1
# these are the intensities we compare our calculated values to, using root mean square
measured_intensities = np.array([3.10085E-05, 5.53419E-05, 8.8836E-05, \
                                 0.000129483, 0.000176707, 0.000284786, 0.00034148, 0.000531378, \
                                 0.000561909, 6.16936E-05], float)


# this function will calculate intensities from lambdas (in mm), given a temperature
# (a float), using Equation 4.4 from section 2.3 of the course materials
# verbose=True will report its working in detail
# the returned value is a list of calculated intensities (floats)
def intensitiesForTemperature(lambdas_in_mm, temp, verbose):
    # for each lambda and temp combination, calculate
    # the result

    if verbose:
        print("With temperature", temp, "and lambdas (mm)=", lambdas_in_mm)


    # convert to metres
    lambdas_in_m = lambdas_in_mm * 1e-3

    # what we return
    calculated_intensities = []

    # let's calculate the intensities from the temperature and lambdas
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


# this function, given two arrays, will return the root mean square deviation
# of the arrays as a float
def rootMeanSquareDev(measured, calculated):
    numberOfValues = len(measured)
    squareOfTheDeviations = (measured - calculated) ** 2
    return np.sqrt(sum(squareOfTheDeviations) / numberOfValues)


# helper function to handle plotting
def plotResult(x, y, temp, title):

    # get some smoother values for the best fit - these are mm...
    lambdas_for_best_fit_mm = np.linspace(0.1, 5.0, 100, float)

    # get the intensities for the best-fit range of wavelengths and temperature
    intensities_for_best_fit = intensitiesForTemperature(lambdas_for_best_fit_mm, temp, False)

    plt.title(title)
    plt.grid()
    plt.xlabel("wavelength / m")
    plt.ylabel("intensity / W m^−2 sf^-1 m^-1")

    # plot the measured values
    plt.plot(measured_lambdas*1e-03, measured_intensities, '*y')
    # the lambdas are in mm so convert to m for plotting
    lambdas_for_best_fit_m = lambdas_for_best_fit_mm * 1e-3
    # plot the best fit line
    plt.plot(lambdas_for_best_fit_m, intensities_for_best_fit, "b-")
    plt.legend(['Measured intensity values', "Best-fit for "+str(temp)+" K"], loc="upper right")
    plt.show()
    return

# a var for storage of the result with the lowest root mean square deviation
# we have found so far by repeated guesses
currentLowestRMSD = None

# main loop
while True:
    temperatureAsText = input("Enter a temperature between 1 and 10 K, or q to quit > ")
    # we decided to exit
    if temperatureAsText == 'q':
        # we are done
        finalTemp = float(input("Enter your final best guess for the temperature > "))
        finalResultIntensities= intensitiesForTemperature(measured_lambdas, finalTemp, False)

        # calculate the root mean square deviation for the intensity
        finalRMSD = rootMeanSquareDev(measured_intensities, finalResultIntensities)
        finalData = {"temp": finalTemp, "rmsd": finalRMSD, "intensities": finalResultIntensities}
        plotResult(measured_lambdas * 1e-3, \
                   finalData["intensities"],
                   finalData["temp"],
                       "Intensities by wavelength for temperature " + \
                       str(finalData["temp"]) + " K")
        print("Bye!")
        break
    else:
        # optimistically convert the temperature to a float
        temperature = float(temperatureAsText)

        # calculate the intensities for this temperature
        calculatedIntensities = intensitiesForTemperature(measured_lambdas, temperature, False)

        # calculate the root mean square deviation for these intensities
        # compared with the measured intensities
        thisRMSD = rootMeanSquareDev(measured_intensities, calculatedIntensities)

        # the first time, we just save it because it is a priori the minimum so far
        if currentLowestRMSD is None:  # first time
            print("Saving the first result with a root mean square deviation of " + str(thisRMSD) +\
                  " at T " + str(temperature) + " K")
            currentLowestRMSD = {"temp": temperature, "rmsd": thisRMSD, "intensities": calculatedIntensities}
        # test the root mean square deviation to see if it is lower
        # than the current guess we have saved before
        elif thisRMSD < currentLowestRMSD["rmsd"]:
            print("Your latest guess has a lower root mean square deviation ("\
                  , thisRMSD, \
                  ") than currently stored, so we are saving it ... ")
            currentLowestRMSD = {"temp": temperature, "rmsd": thisRMSD, "intensities": calculatedIntensities}
        # the root mean square deviation cannot be lower that the one we already have, so let's
        # discard it, and remind the user what the current root mean square deviation is
        else:
            print("No change to lowest root mean square deviation we've found so far (" +\
                  str(currentLowestRMSD["rmsd"]) + " at T " +\
                  str(currentLowestRMSD["temp"]) + " K)")

