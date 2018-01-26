import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# -----section 02_08: sine waves and complex sine waves-----
# a*sin(2*pi*f*t + theta) with 3 orthogonal parameters: a, f, theta

srate = 500
time = np.arange(0., 2., 1./srate)

freq = 1
ampl = 2
phas = np.pi / 3

sinwave = ampl * np.sin(2 * np.pi * freq * time + phas)

plt.plot(time, sinwave, 'k')
plt.xlabel('Time (sec.)')
plt.ylabel('Amplitude (a.u.)')
plt.show()

coswave = ampl * np.cos(2 * np.pi * freq * time + phas)

plt.plot(time, coswave, 'r', label='cosine')

complex_sinewave = ampl * np.exp(1j * (2 * np.pi * freq * time + phas))

plt.plot(time, np.real(complex_sinewave), label='real')
plt.plot(time, np.imag(complex_sinewave), label='imag')
plt.xlabel('Time (sec.)'), plt.ylabel('Amplitude')
plt.title('Complex sine wave projections')
plt.legend()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(time,np.real(complex_sinewave),np.imag(complex_sinewave))
ax.set_xlabel('Time (s)'), ax.set_ylabel('Real part'), ax.set_zlabel('Imag part')
ax.set_title('Complex sine wave in all its 3D glory')


# -----section 02_09: dot product-----
v1 = [1, 2, 3]
v2 = [3, 2, 1]

dp = sum(np.multiply(v1, v2))
dp2 = np.dot(v1, v2)

srate = 500
time = np.arange(0., 2., 1./srate)

freq1 = 5;    # frequency in Hz
freq2 = 5;    # frequency in Hz

ampl1 = 2;    # amplitude in a.u.
ampl2 = 2;    # amplitude in a.u.

phas1 = np.pi/2; # phase in radians
phas2 = np.pi/2; # phase in radians

sinewave1 = ampl1 * np.sin( 2*np.pi * freq1 * time + phas1 );
sinewave2 = ampl2 * np.sin( 2*np.pi * freq2 * time + phas2 );

# compute dot product
dp = np.dot(sinewave1,sinewave2);

# print result
print('dp =',dp)


