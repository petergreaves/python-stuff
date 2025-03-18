# This program calculates the energy diff between two states of a
# hydrogen atom

# We define the function that calculates the energy of a state
# of the hydrogen atom with principal quantum number n
def energy(quantumNumber):
    # Rydberg constant in eV
    ryd_constant = 13.6

    energy = - ryd_constant / (quantumNumber * quantumNumber)
    return energy


# ask user for the two principal quantum numbers
pqn1 = int(input("What is the first principal quantum number?"))
pqn2 = int(input("What is the second principal quantum number?"))
# Print the energy, calculated using the function
if pqn1 == pqn2:
    print("The levels are the same, so there is no difference.")
    exit(-1)
elif pqn1 < 1 or pqn2 < 0:
    print("Levels must be 1 or higher")
    exit(-2)
else:
    print("Energy difference between of hydrogen states", pqn1, "and", pqn2, "is", energy(pqn1) - energy(pqn2), "eV")
