# check kepler's third law, represented as the fact that the
# square of a planet's period divided by the cube of its semimajor axis
# is approximately equal to k / M where k = 4 pi^2 and M is the mass of the Sun
# we use planetary data from Table 2.1 of Topic 7

# and make two assertions:
# 1. the ratio of each planet's period squared / the cube its semimajor axis is approximately equivalent, and
# 2. that ratio is approximately equal to  k / M where k = 4 pi^2 and M is the mass of the Sun

import numpy as np

# some constants
# mass of the Sun in kg
massOfSun = 1.989e30
# G constant in m^3 kg^-1, s^-2
G = 6.67408e-11
# Kepler's constant, if that is what we call it
keplersC = (4.0 * (np.pi ** 2.0))

# arrays for each planet's names and data, which we create symmetrically
planetNames = np.array(["Mercury", "Earth", "Jupiter", "Neptune", "Pluto"])
planetSMAs = np.array([0.39, 1, 5.2, 30.07, 39.48], float)
planetPeriods = np.array([0.24, 1, 11.9, 165, 248], float)

# a function to convert years to seconds
def yearsToSeconds(ys):
    seconds = np.empty(ys.size)
    i = 0
    for y in ys:
        seconds[i] = y * 60 * 60 * 24 * 365
        i += 1
    return seconds

# a function to convert AUs to metres
def AUsToMetres(AUs):
    metres = np.empty(AUs.size)
    j = 0
    for au in AUs:
        metres[j] = au * 1.496e11
        j += 1
    return metres

# calc the result of P^2/a^3 for each planet
# using P^2 / a^3, and store in a new array
planetPeriodToDistanceRatios = (yearsToSeconds(planetPeriods) ** 2) / (AUsToMetres(planetSMAs) ** 3)

# calc the k/M ratio
kMRatio = (keplersC / G) / massOfSun;
print("1. Ratio of k/M:", kMRatio)

# report the planet results by iterating the planets names
# and pulling out the relevant ratio from the array of results
print("2. Ratio for each planet [difference from k/M ratio as %]... ")
k = 0
for planet in planetNames:
    diff = round(abs((planetPeriodToDistanceRatios[k] - kMRatio) / planetPeriodToDistanceRatios[k] * 100), 2)
    print(planet, "=", str(planetPeriodToDistanceRatios[k]), "[+/-", diff, "% of k/M]")
    k += 1
print("********************")
print("Concluding that the planets ratios approximately match each other, validating Kepler's 3rd law, and")
print("that each ratio approximately matches k/M.")
print("********************")
