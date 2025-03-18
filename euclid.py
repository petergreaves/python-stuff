# Euclid's greatest common divisor algorithm
# Ask user to input two integers, and work out and report the greatest common divisor
n = 0
m = 0
# prompt for first integer. as long as this less than 0,
# keep asking
while n <= 0:
    n = int(input("First integer (greater than 0): "))

# prompt for second integer. as long as this is less than 0,
# keep asking
while m <= 0:
    m = int(input("Second integer (greater than 0): "))



while (n != m):
    if (n > m):
        n = n - m
     #  print("n=",n)
    else:
        m = m - n
    #   print("m=",m)

print("The greatest common divisor of the integers provided is", n)
