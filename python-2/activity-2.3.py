'''

Write a program that:

1. calculates the frequency and wavelength of a photon emitted or absorbed when a hydrogen-like ion changes its quantum state
2. requires the user to provide the atomic number of the ion and the principal quantum number of the initial and final states
3. tells the user whether the photon is emitted or absorbed.
'''

# constants
plancksConstant = 4.1315e-15  #eV
speedOfLight = 2.99e8  # m s^-1
rydbergsConstant = 13.6  # Rydberg constant in eV


# We define the function that returns the energy of a state
# of the hydrogen atom with Z value ZValue and principal quantum number quantumNumber
def getEnergyForZAndQuantumNumber(Z, quantumNumber):
    energy = - (Z ** 2 * rydbergsConstant / (quantumNumber ** 2))
    #  print(energy)
    return energy


# We define the function that returns the frequency of a photon based on the level diff and atomic number
# of the hydrogen-like ion
def getPhotonFrequency(startingQState, endQState, ZValue):
    energyDiff = getEnergyForZAndQuantumNumber(ZValue, startingQState) - getEnergyForZAndQuantumNumber(ZValue,
                                                                                                       endQState)
    return abs(energyDiff / plancksConstant)


# a simple function to calc vavelength based on c / freq
def getWavelengthForFrequency(frequency):
    return float(speedOfLight / freq)


# the program
# Print the energy for the ion, calculated using the function
defaultStartQS = 4
defaultEndQS = 1
defaultAtomicNumber = 1  #hydrogen

userProvidedStart = input("Enter starting level (def = 4) ")
if not userProvidedStart:
    userProvidedStart = defaultStartQS
else:
    userProvidedStart = int(userProvidedStart)

userProvidedEnd = 0
userProvidedEnd = input("Enter ending level (def = 1) ")
if not userProvidedEnd:
    userProvidedEnd = defaultEndQS
else:
    userProvidedEnd = int(userProvidedEnd)

userProvidedAtomicNumber = 0
userProvidedAtomicNumber = input("Enter atomic number of the hydrogen-like ion (def = 1) ")
if not userProvidedAtomicNumber:
    userProvidedAtomicNumber = defaultAtomicNumber
else:
    userProvidedAtomicNumber = int(userProvidedAtomicNumber)

freq = getPhotonFrequency(userProvidedStart, userProvidedEnd, userProvidedAtomicNumber)

# need to calculate if the change in state is "up" or "down" and iwc the photon
# is going to be absorbed or emitted - assume emitted for a default

resAsString = "emitted" if userProvidedStart > userProvidedEnd else "absorbed"
# print the results
print("A photon was", resAsString, "with frequency (Hz):", freq, " and wavelength (nm):",
      getWavelengthForFrequency(freq) * 1e9)
