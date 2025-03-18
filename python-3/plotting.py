import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,8, 8)
print(x)

y1 = np.exp(0.3*x)
y2 = 6*np.exp(-x**2)

plt.plot(x,y1)
plt.plot(x,y2)
plt.title("couple of exponential function plots")
