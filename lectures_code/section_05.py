import numpy as np
import math
import matplotlib.pyplot as plt
import random
import timeit
import scipy.fftpack
from mpl_toolkits.mplot3d import Axes3D
from __future__ import division

# -----section 05_23: fast fourier transform-----


pnts = 1000
signal = np.random.randn(pnts)

# slow version
tic = timeit.default_timer()
fourTime = np.arange(0,pnts)/pnts
fCoefs   = np.zeros(len(signal), dtype=complex)
for fi in range(0,pnts):
    csw = np.exp( -1j*2*np.pi*fi*fourTime )
    fCoefs[fi] = np.dot(signal,csw)
toc = timeit.default_timer()
t1 = toc-tic

# fast version
tic = timeit.default_timer()
fCoefsF = scipy.fftpack.fft(signal)
toc = timeit.default_timer()
t2 = toc-tic

plt.bar([1,2],[t1,t2])
plt.title('Computation times')
plt.ylabel('Time (sec.)')
plt.xticks([1,2], ['loop','FFT'])
plt.show()

## fft still need normalizations

srate = 5000
time  = np.arange(0,1.9,1/srate)
npnts = len(time)

# signal
signal = 2*np.sin(2*np.pi*6*time)

# Fourier spectrum
signalX = scipy.fftpack.fft(signal)

hz = np.linspace(0, srate/2, math.floor(npnts/2) + 1)

# amplitude
ampl = np.abs(signalX[0:len(hz)]) / npnts
ampl[1:] *= 2

plt.stem(hz, ampl)
plt.xlim([0, 10])

# -----section 05_23: inverse fast fourier transform-----

srate = 1000
time  = np.arange(0,3,1/srate)
pnts  = len(time)

# create multispectral signal
signal  = np.multiply( (1+np.sin(2*np.pi*12*time)) , np.cos(np.sin(2*np.pi*25*time)+time) )

# fft
signalX = scipy.fftpack.fft(signal)

# reconstruction via ifft
reconSig = scipy.fftpack.ifft(signalX)

plt.plot(time, signal)
plt.plot(time, reconSig, 'r')

