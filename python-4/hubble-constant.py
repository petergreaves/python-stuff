import numpy as np
import matplotlib.pyplot as plt


# implementation of linear regression formula for 2 array
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


raw_data_in_lines = """
82.8	5420
89.1	6012
50.8	3319
450.8	30269
361.4	22387
79.4	4966
223.9	13804
138.0	9795
67.6	4102
236.6	15066
29.2	1991
39.1	2449
80.2	5117
115.9	7228
70.5	4842
170.6	10715
148.6	8670
243.2	14791
35.6	2500
56.5	3524
""".split("\n")


def parseRawDataToArrays():
    distances = []
    apparent_speeds = []
    for row in raw_data_in_lines:
        if row:
            thisDistance, thisSpeed = row.split("\t")
            distances.append(float(thisDistance))
            apparent_speeds.append(float(thisSpeed))
    return distances, apparent_speeds

# to arrays for the rmsd
xArray,yArray = np.array(parseRawDataToArrays())

linear_regression_result = linear_regression(xArray,yArray)
print("Hubble constant :",linear_regression_result["gradient"])
plt.plot(xArray, xArray*linear_regression_result["gradient"]+linear_regression_result["intercept"])
plt.plot(xArray, yArray, "*r")
plt.show()