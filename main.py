import matplotlib.pyplot as plt
import numpy as np

def energy_function(x):
    return x ** 2

x = np.linspace(-5, 5, 1000)
y = energy_function(x)

plt.plot(x, y)
plt.show()