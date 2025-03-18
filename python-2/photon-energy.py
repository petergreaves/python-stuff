'''
Write a program that uses a function to calculate the frequency of a photon emitted or absorbed when a hydrogen atom changes
its quantum state from n=4 to n=1. Use h=4.1315×10^-15 eV for the value of Planck’s constant.
'''

plancksConstant = 4.1315e-15 #eV
speedOfLight = 2.99e8 # m s^-1

# We define the function that calculates the energy of a state
# of the hydrogen atom with principal quantum number n
def energy(quantumNumber):
    # Rydberg constant in eV
    ryd_constant = 13.06
    energy = - ryd_constant / (quantumNumber * quantumNumber)
    return energy


def getPhotonFrequency(startingQState, endQState):
    energyDiff=abs(energy(startingQState) - energy(endQState))
    return energyDiff/plancksConstant

# the actual program

defaultStartQS=4
defaultEndQS=1

userDefinedStart=0
userDefinedStart=input("Enter starting level (def = 4) ")

if not userDefinedStart:
    userDefinedStart=defaultStartQS
else:
    userDefinedStart=int(userDefinedStart)

userDefinedEnd=0
userDefinedEnd=input("Enter ending level (def = 1) ")
if not userDefinedEnd:
    userDefinedEnd=defaultEndQS
else:
    userDefinedEnd=int(userDefinedEnd)

freq=getPhotonFrequency(userDefinedStart, userDefinedEnd)

print("The frequency of a photo emitted or absorbed when a hydrogen atom changes its quantum state from n=",
      userDefinedStart,
      "to n=", userDefinedEnd,
      "is", freq, "Hz")
print("Which, coincidentally, has a wavelength of ", float(speedOfLight/freq*1e9), "nm")

