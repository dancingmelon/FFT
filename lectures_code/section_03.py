from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.fftpack
import random
from mpl_toolkits.mplot3d import Axes3D

# -----section 03_12: discrete Fourier Transform-----

srate = 1000
time = np.arange(0., 2., 1./srate)
pnts = len(time)
signal = 2.5 * np.sin(2*np.pi*4*time) + 1.5 * np.sin(2*np.pi*6.5*time)

plt.plot(time, signal)

fourTime = np.array(range(0, pnts))/pnts
fCoefs = np.zeros((len(signal)), dtype=complex)

for fi in range(0, pnts):
    csw = np.exp(-1j*2*np.pi*fi*fourTime)
    fCoefs[fi] = np.dot(signal, csw) / pnts

ampls = 2 * np.abs(fCoefs)

hz = np.linspace(0, srate/2, num=math.floor(pnts/2.)+1)

plt.stem(hz, ampls[range(0, len(hz))])
plt.xlabel('Frequency (Hz)'), plt.ylabel('Amplitude (a.u.)')
plt.xlim(0,10)

# -----section 03_13: converting indices to frequencies-----
pnts = 16
fourTime = np.arange(0, pnts) / pnts
fi_all = np.arange(0, pnts)

for fi in fi_all:
    csw = np.exp(-1j * 2*np.pi*fi*fourTime)

    loc = np.unravel_index(fi, [4, 4], 'F')
    plt.subplot2grid((4, 4), (loc[1], loc[0]))
    plt.plot(fourTime, np.real(csw), 'bo-')
    plt.plot(fourTime, np.imag(csw), 'ro-')

# -----section 03_15: scaling Fourier coefficient-----

srate  = 1000 # hz
time   = np.arange(0.,1.5,1/srate)  # time vector in seconds
pnts   = len(time)   # number of time points
signal = 2.5 * np.sin( 2*np.pi*4*time )

fourTime = np.arange(0, pnts) / pnts
fCoefs = np.zeros(len(signal), dtype=complex)

for fi in range(0, pnts):
    csw = np.exp(-1j*2*np.pi*fi*fourTime)
    fCoefs[fi] = np.dot(csw, signal)

fCoefs = fCoefs / pnts
ampls = np.abs(fCoefs)
ampls[1:] *= 2

hz = np.linspace(0, srate/2, num=math.floor(pnts/2) + 1)

plt.plot(hz, ampls[0:len(hz)])
plt.xlabel('Frequency (Hz)'), plt.ylabel('Amplitude (a.u.)')
plt.xlim(0,10)

# -----section 03_16: interpret phase values-----

srate = 1000
time = np.arange(0., 2., 1/srate)
npnts = len(time)

signal1 = 2.5 * np.sin(2*np.pi*10*time + 0)
signal2 = 2.5 * np.sin(2*np.pi*10*time + np.pi/2)

fourTime = np.arange(0, npnts) / npnts
signal1X = np.zeros(len(signal1), dtype=complex)
signal2X = np.zeros(len(signal2), dtype=complex)

for fi in range(0, npnts):
    csw = np.exp(-1j*2*np.pi*fi*fourTime)

    signal1X[fi] = np.dot(csw, signal1) / npnts
    signal2X[fi] = np.dot(csw, signal2) / npnts

hz = np.linspace(0, srate/2, num=math.floor(npnts/2) + 1)

signal1Amp = np.abs(signal1X[0:len(hz)])
signal1Amp[1:] *= 2

signal2Amp = np.abs(signal2X[0:len(hz)])
signal2Amp[1:] *= 2

signal1phase = np.angle(signal1X[0:len(hz)])
signal2phase = np.angle(signal2X[0:len(hz)])

plt.subplot2grid((3, 2), (0, 0))
plt.plot(time, signal1)

plt.subplot2grid((3, 2), (0, 1))
plt.plot(time, signal2, 'k')

plt.subplot2grid((3, 2), (1, 0))
plt.stem(hz, signal1Amp)
plt.xlim([0, 20])

plt.subplot2grid((3, 2), (1, 1))
plt.stem(hz, signal2Amp, 'k')
plt.xlim([0, 20])

plt.subplot2grid((3,2), (2,0))
plt.stem(hz, signal1phase)
plt.xlim([0, 20])

plt.subplot2grid((3,2), (2,1))
plt.stem(hz, signal2phase, 'k')
plt.xlim([0, 20])


# -----section 03_18: Amplitude vs. power-----

srate = 1000
time  = np.arange(0,.85,1/srate)
npnts = len(time)
signal = 2.5*np.sin(2*np.pi*10*time)

fourTime = np.arange(0, npnts) / npnts
signalX = np.zeros(len(time), dtype=complex)

for fi in range(0, npnts):
    csw = np.exp(-1j*2*np.pi*fi*fourTime)
    signalX[fi] = np.dot(csw, signal)

hz = np.linspace(0, srate/2, num=math.floor(npnts/2) + 1)
signalAmp = np.abs((signalX/npnts)[0: len(hz)])
signalAmp[1:len(hz)] *= 2
signalPow = signalAmp**2

plt.plot(hz, signalAmp, 'bo')
plt.plot(hz, signalPow, 'ro-')
plt.plot(hz, 10*np.log10(signalPow), 'ks-' )
plt.xlim([0,20])
plt.ylim([-30, 10])

# Parseval's theorem (conservation of energy)
np.sum(signal**2) - np.sum((np.abs(signalX))**2) / len(signalX) < 0.000001














