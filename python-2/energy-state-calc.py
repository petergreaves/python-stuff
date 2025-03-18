# This program calculates the energy (in eV) of the
# state of a hydrogen atom with a given principal quantum


# Rydberg constant in eV
ryd_constant=13.6

# the allowed atomic number range (mix, max)
allowedAtomicNumberRange = range(1, 118+1)

# ask user for principal quantum number as "principalQNumber_given"
principalQNumber_given = input("What is the principal quantum number? ")
# optimistically convert to an int as "principalQNumber"
principalQNumber= int(principalQNumber_given)

if principalQNumber > 0 :
    atomicNumber =int(input("What is the atomic number (Z)? "))
    if atomicNumber in allowedAtomicNumberRange:
        energy = -(atomicNumber**2)*ryd_constant/(principalQNumber**2)
        print ("The energy of the hydrogen-like ion with state =",
               principalQNumber, "and Z =",
               atomicNumber, "is",
               energy, "eV")
    else:
        print (atomicNumber, "is not a valid atomic number - the range is [",
               allowedAtomicNumberRange.start, ",",
               allowedAtomicNumberRange.stop-1, "]")
else:
    print ("That's not a physically possible principal quantum number")