import numpy as np
import matplotlib.pyplot as plt


# implementation of lineear regression formula for 2 array
# which we assume are symmetrical
def linear_regression(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_xsquared = sum(x ** 2)
    square_of_sumx = sum_x ** 2

    intercept = ((sum_y * sum_xsquared) - (sum_x * sum_xy)) \
                / (sum_xsquared - square_of_sumx)

    gradient = (sum_xy - (sum_x * sum_y)) \
               / (sum_xsquared - square_of_sumx)

    return {"intercept": intercept,
            "gradient": gradient}


x = np.array([0.053, 0.042, 0.029, 0.025, 0.017, 0.010, 0.008, 0.002], float)
F = np.array([3.55, 2.96, 2.31, 2.01, 1.50, 1.02, 0.697, 0.226], float)

# for testing the function gr should be 2, intercept = 1
# test_x=np.array([1, 2, 3], int)
# test_y=np.array([5, 15, 27], int)

result = linear_regression(x, F)
print("Using x=", x, ", y=", F)
print("Gradient=", result["gradient"], ", intercept=", result["intercept"])
plt.plot(x, x*result["gradient"]+result["intercept"])
plt.plot(x, F, "*g")
plt.show()
