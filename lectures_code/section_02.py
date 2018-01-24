import numpy as np
import matplotlib.pyplot as plt

# -----section 02_06: complex numbers-----

# create a complex number with 1j
z = 4 + 1j * 3

# extract the real and imaginary parts of the complex number
z_real = np.real(z)  # or z.real
z_imag = np.imag(z)  # or z.imag

# calculate the magnitude of a complex number
z_mag = np.abs(z)

# calculate the angle of the complex number
z_angle = np.angle(z)

# -----section 02_07: Euler's formula e^ik = cos(k) + isin(k)-----

# exp() curve
x = np.linspace(-3, 3, num=50)
plt.plot(x, np.exp(x), label='y=e^x')
plt.axis([min(x), max(x), 0, np.exp(x[-1])])
plt.grid(True)
plt.legend()
plt.xlabel('x')

# cos(k) and sin(k) on the unit circle

k1 = np.pi / 3
k2 = np.pi / 2
euler1 = np.exp(1j*k1)
euler2 = np.exp(1j*k2)
x = np.linspace(-np.pi, np.pi, num=100)

plt.plot(np.cos(x), np.sin(x))

# two method to get the real and imaginary parts of e^ik
plt.plot(np.cos(k1), np.sin(k1), 'ro')
plt.plot(euler2.real, euler2.imag, 'ro')

plt.axis('square')
plt.grid(True)
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')

m = 20
compnum = m * euler1

mag = np.abs(compnum)
phs = np.angle(compnum)

plt.polar([phs, phs], [0, mag])

