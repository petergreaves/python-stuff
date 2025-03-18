from math import sin, pi

latitude = float(input("What is the latitude in degrees?"))
latitudeInRadians = latitude * pi / 180  # latitude in radians
acceleration = 9.78 * (1 + (0.0053 * (sin(latitudeInRadians)) ** 2))
print("Acc. due to gravity:", acceleration, "metres/(sec squared)")

totalMass = 0
items = []
i = 0;
while True:
    answer = input("Mass of item in kg?")
    if answer == "stop":
        break
    else:
        answerAsFloat = float(answer);
        items.append(answerAsFloat)
        totalMass += answerAsFloat
print("Total mass:", totalMass, "kilograms")

weight = totalMass * acceleration
print("Total weight:", weight, "newtons")
print("item weights ... ")
for i in items:
    print(i * acceleration, "newtons")

