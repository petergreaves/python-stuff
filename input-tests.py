'''name = input("What's your name? ")

print ("Nice to meet you,", name)

year = input("In what year were you born? ")

print ("Your age is", 2024 - int(year))

totmass = 10  # total mass in kilograms
latitude = int(input("enter the latitude in degrees (N or S) as a whole number: "))

if latitude < 60 and latitude >= 30:
    acc = 9.81  # acceleration in metres/(sec squared)
elif latitude < 30:
    acc = 9.78  # acceleration in metres/(sec squared)
else:
    acc = 9.83  # acceleration in metres/(sec squared)

weight = totmass * acc

print ("Total weight at latitude", latitude, "is", weight, "newtons")
'''
totmass = 0 # total mass in kilograms

while True: # While loop, continue forever as always true
    answer = input("Mass of item in kg? ") # Ask user for mass, user can enter stop
    if str(answer).strip().lower() == "stop": # If input is stop
        break # Exit loop
    else:
        mass = float(answer) # Convert answer to float
        totmass = totmass + mass # Add to total mass

print ("Total mass:", totmass, "kilograms")
