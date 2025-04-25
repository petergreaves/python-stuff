import numpy as np

x = np.array([0.053, 0.042, 0.029, 0.025, 0.017, 0.010, 0.008, 0.002], float)
F = np.array([3.55, 2.96, 2.31, 2.01, 1.50, 1.02, 0.697, 0.226],float)

print("The sum of x is",sum(x))
print("The number of elenents in F is", len(F))
print("The ratio of x/F", x/F)

