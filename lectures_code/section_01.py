import numpy as np

# create a complexe number with 1j
z = 4 + 1j * 3

# extract the real and imaginary parts of the complexe number
z_real = np.real(z) # or z.real
z_imag = np.imag(z) # or z.imag

# calculate the magnitude of a complexe number
z_mag = np.abs(z)

# calculate the angle of the complexe number
z_angle = np.angle(z)

