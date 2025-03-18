# Euclid's greatest common divisor algorithm

# Ask user to input two integers
n= int(input("First integer"))
m= int(input("Second integer"))

while (n != m):
    if (n > m):
        n=n-m
    else:
        m=m-n

print ("The greatest common divisor of the integers provided is",n)