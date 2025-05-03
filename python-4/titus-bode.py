#Program to calculate predictions of the Titius-Bode law
b=0.3 #First term of the sequence in AU
r=2 #The common ratio of the sequence
while True:
    n = input("Value of n in Titius-Bode law?")
    if n == "stop":
        break
    else:
        a=0.4+(b * r**(int(n)))
        print("Semi-major axis", a, "AU")