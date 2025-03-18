totmass = 0		# total mass in kilograms

# The masses of each item are added up
while True:
    answer = input("Mass of item in kg?")
    if answer == "stop":
        break
    else:
        mass = float(answer)
        totmass = totmass + mass

# The appropriate acceleration due to gravity is determined

latitude= float(input("what is your latitude?"))

if latitude < 30:
    acc = 9.78   # acceleration in metres/(sec squared)
elif latitude < 60:
    acc = 9.81  # acceleration in metres/(sec squared)
else:
    acc = 9.83   # acceleration in metres/(sec squared)

weight = totmass * acc

print ("Total weight:", weight, "newtons")
