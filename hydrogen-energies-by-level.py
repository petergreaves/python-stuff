'''
Write a program that calculates the energy of the hydrogen atom for states with n = 1
to n=10, stores them in a list, and then prints the energy for a specific state required by the user.

The program should print a warning if the user asks for the energy of a state with n>10.
'''

# vars and constants

startQN=1
maxLevels=10
levelsList = []
energiesList = []
rydberg_const = 13.06
hydrogenZ=1

# initialise the levels
while startQN<=maxLevels:
    levelsList.append(startQN)
    energiesList.append(-(hydrogenZ**2) * rydberg_const/startQN**2)
    startQN += 1

# get a number from the user
# requiredQN = 0
requiredQN = int(input("What state do you want (1-10)? (-1 to quit) "))
if (requiredQN == -1):
    print("Bye!")
    exit(0)
elif (requiredQN<1 or requiredQN >10):
    print("Number for state must be between 1 and 10 inclusive, but you entered", requiredQN)
    exit(-1)
else:
    print("The energy state for state",requiredQN, "is", float(energiesList[requiredQN-1]), "eV")
