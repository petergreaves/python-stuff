'''a program that calculates the kinetic energy of an object for a mass provided by the user and the following speeds: 1.0 m s^-1
 , 2.0 m s^-1, 3.0 m s^-1, 4.0 m s^-1

 The kinetic energy of an object is equal to half its mass multiplied by the square of its speed
'''

# initialisation
# a var for mass (a float)
mass = 0.0
# a list containing the speeds, initialised with given values
speeds = [1.0, 2.0, 3.0, 4.0]
# a list for the kinetic energies that we have calculated in the for loop
energies = []
# and an index var which we use in the reporting section
k = 0

# get the user's input of mass
# to do : write a functional that makes sure what we get
# into the mass var is a float.  for now, just assume it is and trim it
mass = float(input("Enter the mass (kg) : ").strip());

# iterate the speeds, calculating the kinetic energy each time
# and storing it in the energies list
for speed in speeds:
    energies.append((mass / 2 * speed ** 2))

# iterate the energies list and report it out
for e in energies:
    print("Kinetic energy for mass", mass,"is", e, "N at speed", speeds[k], "m s^-2")
    k += 1

# done