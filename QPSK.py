import matplotlib.pyplot as plt
import numpy as np

# gets the ranges for the x values
t1 = np.arange(0, 1, 0.01)
t2 = np.arange(1, 2, 0.01)
t3 = np.arange(2, 3, 0.01)

# gets the values for the y-values
one1 = 2 * np.cos(4*np.pi*t1 + (np.pi/4))
zero = 2 * np.cos(4*np.pi*t2 - (3*np.pi/4))
one3 = 2 * np.cos(4*np.pi*t3 + (np.pi/4))

# plots the symbols:
plt.plot(t1, one1, color='C0')
plt.plot(t2, zero, color='C0')
plt.plot(t3, one3, color='C0')

# let's get the labels correct, please
plt.title("QPSK with 1/2 code rate: 1(1) 0(0) 1(1) repeated bits in parens")
plt.xlabel("Time in seconds")
plt.ylabel("Amplitude")

plt.show()
