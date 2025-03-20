# Write a program using Python that does the following:
#
# 1. Prompts the user to input the name of a particular isotope and its half-life,  τ, in seconds
# 2. Prompts the user for an initial amount of the isotope (in grams) and an elapsed time (in seconds).
# 3. Calculates the amount of the isotope remaining after this elapsed time and displays the result.
# 4. Calculates the initial mass of the isotope (in grams) necessary to ensure that, after half a minute, 5 grams of it remain, and displays the result. 5
# Plots the amount of the isotope remaining as a function of time, from elapsed time
# 6. The program should then
# repeat the instructions from step 1, until the user chooses to halt the program.
# 7. When the user wishes to enter no more isotopes, the program should display the decay plots for all of the isotopes that were entered, in a single
# plot, and print out a list of all the isotopes studied.


import numpy as np
import matplotlib.pyplot as plt


def sigfigs(v, sfs):
    return np.format_float_positional(v, precision=sfs, unique=False, fractional=False, trim='k')


def getRemainingAtElapsedTime(isotopeDetails, t):
    print("t=",isotopeDetails["elapsedTime"])
    print("amount",isotopeDetails["amount"])
    print("hl",isotopeDetails["halfLife"])
    remaining = isotopeDetails["amount"] * (0.5 ** (t / isotopeDetails["halfLife"]))
    print("remaining=",remaining)
    return isotopeDetails["amount"] * (0.5 ** (t / isotopeDetails["halfLife"]))


def getInitialMass(isotopeDetails, elapsedTime, gramsRequired):
    initialMass = gramsRequired / (0.5 ** (elapsedTime / isotopeDetails["halfLife"]))
    return initialMass


def plot(isotopeDetails, t):
    t = np.linspace(0, 10, 11)
    print("t=",t)
    y = getRemainingAtElapsedTime(isotopeDetails, t)
    print("y=",y)
    #plt.title("Half life of isotope", isotopeDetails["isotopeName"])
    plt.plot(t, y)
    plt.show()


# grab some user input into a dict and return it
def getIsotopeDetails():
    isotopeName = input("Enter the isotope name, or q to quit:")
    if isotopeName == 'q':
        return {}
    else:
        halflife = int(input("Enter the half life (seconds):"))
        amount = int(input("Enter the starting amount (grams):"))
        elapsedTime = int(input("Enter the elapsed time (seconds):"))
    return {"isotopeName": isotopeName,
            "halfLife": halflife,
            "amount": amount,
            "elapsedTime": elapsedTime}


thisIsotopeDetails = getIsotopeDetails()

if thisIsotopeDetails == {}:
    print("Bye!")
else:
    # Calculate the amount of the isotope remaining after this elapsed time and display the result.
# print("1.", str(getRemainingAtElapsedTime(thisIsotopeDetails, thisIsotopeDetails["elapsedTime"])), "grams of",
    #      thisIsotopeDetails["isotopeName"], "remain after", str(thisIsotopeDetails["elapsedTime"]), "seconds")

    # Calculate the initial mass of the isotope (in grams) necessary to ensure that, after half a minute,
    #  5 grams of it remain, and display the result.
  #  print("2. When 30s have passed, if 5g remain, then the initial mass was",
    #      sigfigs(getInitialMass(thisIsotopeDetails, 30, 5), 2), "g to 2SF")

    # Plot the amount of the isotope remaining as a function of time, from elapsed time t=0 to t=10
    plot(thisIsotopeDetails, 10)
