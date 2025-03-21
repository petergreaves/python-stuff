# Write a program using Python that does the following:
#
# 1. Prompts the user to input the name of a particular isotope and its half-life, τ, in seconds
# 2. Prompts the user for an initial amount of the isotope (in grams) and an elapsed time (in seconds).
# 3. Calculates the amount of the isotope remaining after this elapsed time and displays the result.
# 4. Calculates the initial mass of the isotope (in grams) necessary to ensure that,
# after half a minute, 5 grams of it remain, and displays the result. 5
# 5. Plots the amount of the isotope remaining as a function of time, from elapsed time
# 6. The program should then repeat the instructions from step 1, until the user chooses to halt the program.
# 7. When the user wishes to enter no more isotopes, the program should display the decay plots for
# all of the isotopes that were entered, in a single plot, and print out a list of all the isotopes studied.

import numpy as np
import matplotlib.pyplot as plt

# constants for plotting on the x axis
plotStart = 0
plotEnd = 10
plotGranularity = 110


# function to return a float to the required SFs
def sigfigs(v, sigfigs):
    return np.format_float_positional(v, precision=sigfigs, unique=False, fractional=False, trim='k')


# function to returns the remaining mass (g) for an isotope at time t (s)
def getRemainingMassAtElapsedTime(isotopeDetails, t):
    # print("t=", isotopeDetails["elapsedTime"])
    # print("amount", isotopeDetails["amount"])
    # print("hl", isotopeDetails["halfLife"])
    remaining = isotopeDetails["amount"] * (0.5 ** (t / isotopeDetails["halfLife"]))
    # print("remaining=", remaining)
    return isotopeDetails["amount"] * (0.5 ** (t / isotopeDetails["halfLife"]))


# function to return the initial mass (g) for an isotope if the specified gramsRequired (g)
# were to remain at elapsedTime (s)
def getInitialMass(isotopeDetails, elapsedTime, gramsRequired):
    return gramsRequired / (0.5 ** (elapsedTime / isotopeDetails["halfLife"]))


# function to plot isotope decay for all the isotopes in the list
# (if it is a list) or just the single isotope (if it isnt a list)
def plot(isotopeOrList):
    t = np.linspace(plotStart, plotEnd, plotGranularity)
    # the y axis values (grams)
    ys = []
    # list for the isotope names for the legend
    names=[]
    plt.xlabel("Time/s")
    plt.ylabel("Amount remaining/g")
    plt.title("Decay rate of isotopes, g/s")
    if isinstance(isotopeOrList, list):
        # the function was sent a list of isotopes
        # so iterate them and save the y values
        for i in isotopeOrList:
            ys.append(getRemainingMassAtElapsedTime(i, t))
            names.append(i["isotopeName"])
    else:
        # just a single isotop
        ys.append(getRemainingMassAtElapsedTime(isotopeOrList, t))
        names.append(isotopeOrList["isotopeName"])
    k=0
    print(names)

    for thisY in ys:
        plt.plot(t, thisY)
        k+=1
    plt.legend(names, loc="upper right")
    plt.show()


# function to get user input for the isotope into a dictionary and return it.
# if the user enters q for the isotope name, it just returns an empty dictionary
# so the caller can work out what to do
def getIsotopeDetails():
    isotopeName = input("Enter the isotope name, or q to quit:")
    if isotopeName == 'q':
        return {}
    else:
        halflife = float(input("Enter the half life (seconds):"))
        amount = int(input("Enter the starting amount (grams):"))
        elapsedTime = int(input("Enter the elapsed time (seconds):"))
    return {"isotopeName": isotopeName,
            "halfLife": halflife,
            "amount": amount,
            "elapsedTime": elapsedTime}


# function to do the end-of-program summary
def summarise():
    plot(allIsotopeDetails)
    # print all the isotope names (if any)
    if len(allIsotopeDetails) > 0:
        print("Thanks for using this app! The isotopes we studied were:")
        for isotope in allIsotopeDetails:
            print(isotope["isotopeName"])


# list for where we keep all the isotopes that were studied so
# we can iterate it at the end
allIsotopeDetails = []

# THE MAIN PROGRAM/ENTRY POINT
while True:
    # get the isotope details
    thisIsotopeDetails = getIsotopeDetails()
    # empty isotope means that it is time to quit, so
    if thisIsotopeDetails == {}:
        summarise()
        break
    else:
        # Calculate the amount of the isotope remaining after this elapsed time and display the result.
        print("1.", str(sigfigs(getRemainingMassAtElapsedTime(thisIsotopeDetails, thisIsotopeDetails["elapsedTime"]),2)),
              "grams (to 2SF) of",
              thisIsotopeDetails["isotopeName"], "remain after", str(thisIsotopeDetails["elapsedTime"]), "seconds")

        # Calculate the initial mass of the isotope (in grams) necessary to ensure that, after half a minute,
        # 5 grams of it remain, and display the result.
        print("2. When 30s have passed, if 5g remain, then the initial mass was",
              sigfigs(getInitialMass(thisIsotopeDetails, 30, 5), 2), "g to 2SF")

        # Plot the amount of the isotope remaining as a function of time,
        # from elapsed time t=0 to t=10
        plot(thisIsotopeDetails)

        # save this isotope to the list
        allIsotopeDetails.append(thisIsotopeDetails)

