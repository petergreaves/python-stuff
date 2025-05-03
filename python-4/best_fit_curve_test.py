import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline  # For smooth curve

# Sample data: 10 float values each
x = np.array([0.5, 1.1, 2.0, 3.3, 4.4, 5.5, 6.2, 7.8, 8.9, 10.0])
y = np.array([1.0, 2.5, 1.8, 3.6, 2.2, 5.5, 4.3, 6.0, 5.1, 7.8])

# Create smooth x-values for interpolation
x_smooth = np.linspace(x.min(), x.max(), 300)

# Use spline interpolation for a smooth curve
spline = make_interp_spline(x, y, k=3)  # k=3 for cubic spline
y_smooth = spline(x_smooth)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(x_smooth, y_smooth, label="Smooth Best Fit Curve", color='blue')
plt.scatter(x, y, color='red', label="Data Points")
plt.title("Best Fit Curve Through Points")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()
