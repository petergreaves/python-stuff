import numpy as np
import matplotlib.pyplot as plt

# some constants
planck_h = 6.626e-34
c = 2.998e8
#boltzman
k = 1.381e-23


# calculate a BB curve for the wavelenths and temperature provided
def bbCurve(wavelengths, temperature, verbose):
    # for each wavelength and temp combination, calculate
    # the result
    if verbose:
        print("With temperature", temperature, "wl=", wavelengths)
    intensities = []
    for w in wavelengths:
        partOneNumerator = (2 * planck_h * (c ** 2))
        partOneDenominator = (w ** 5)
        if verbose:
            print("partOneNumerator/partOneDenominator", partOneNumerator/partOneDenominator)
        expVal = planck_h * c / (w * k * temperature)
        if verbose:
            print("the exponent", expVal)
        partTwo=1 / (np.exp(expVal) - 1)
        if verbose:
            print("1/ e^the exponent -1)", partTwo)
        result =  partOneNumerator / partOneDenominator \
                 * partTwo
        if verbose:
            print("for w=", w, ", the result is", result)
        intensities.append(result)


    plt.xlabel('wavelength / mm')
    plt.ylabel('intensity / ?')
    plt.plot(lambda_range_metres, np.array(intensities))
    plt.show()
    return

# Define the wavelength range in millimetres
lambda_range=np.linspace(0.1,5.0,50,endpoint=True)
# convert to metres

temperature = 2
verbose=False
lambda_range_metres=lambda_range*1e-3
bbCurve(lambda_range_metres, temperature,verbose)
#for k in [1,2,3,4,5,6,7,8,9,10]:
    #bbCurve(wavelengths, k,verbose)
