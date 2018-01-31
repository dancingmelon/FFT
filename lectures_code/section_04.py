# -----section 04_20: Inverse discrete Fourier transform-----
import numpy as np
import math
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

srate = 1000
time = np.arange(0., 2., 1 / srate)
pnts = len(time)
signal = 2.5 * np.sin(2 * np.pi * 4 * time) + 1.5 * np.sin(2 * np.pi * 6.5 * time)

fourTime = np.arange(0, pnts) / pnts
fCoefs = np.zeros(len(time), dtype=complex)

for fi in range(pnts):
    csw = np.exp(-1j * 2 * np.pi * fi * fourTime)
    fCoefs[fi] = np.dot(csw, signal)

ampls = np.abs(fCoefs) / pnts
ampls[1:] *= 2

hz = np.linspace(0, srate / 2, num=math.floor(pnts / 2) + 1)

plt.stem(hz, ampls[0:len(hz)])
plt.xlim([0, 10])

reconSignal = np.zeros(len(signal), dtype=complex)

for fi in range(0, pnts):
    csw = fCoefs[fi] * np.exp(1j * 2 * np.pi * fi * fourTime)
    reconSignal += csw

reconSignal /= pnts

plt.plot(time, signal, label='original')
plt.plot(time, np.real(reconSignal), 'ro', label='reconstructed')
plt.legend()

srate = 1000
time = np.arange(0, 3, 1 / srate)
pnts = len(time)

signal = (1 + np.sin(2 * np.pi * 12 * time)) * np.cos(np.sin(2 * np.pi * 25 * time) + time)

plt.plot(time, signal)

fourTime = np.array(range(0, pnts)) / pnts
fCoefs = np.zeros(len(signal), dtype=complex)

# here is the Fourier transform...
for fi in range(0, pnts):
    csw = np.exp(-1j * 2 * np.pi * fi * fourTime)
    fCoefs[fi] = np.sum(np.multiply(signal, csw)) / pnts

hz = np.linspace(0, srate, num=pnts)

reconSignal = np.zeros(len(signal), dtype=complex)

for fi in range(0, pnts):
    # create coefficient-modulated complex sine wave
    csw = fCoefs[fi] * np.exp(1j * 2 * np.pi * fi * fourTime)

    # sum them together
    reconSignal = reconSignal + csw

    if fi < 300 or fi > 2700:
        # set up plot
        pl.cla()  # wipe the figure
        plt.subplot2grid((2, 1), (0, 0))
        plt.plot(time, signal, label='Original')
        plt.plot(time, np.real(reconSignal), label='Reconstruction')
        plt.legend()

        plt.subplot2grid((2, 1), (1, 0))
        plt.plot(hz[0:fi], 2 * np.abs(fCoefs[0:fi]))
        plt.xlim([0, hz[-1]])

        # show plot
        # display.clear_output(wait=True)
        # display.display(pl.gcf())
        # ttime.sleep(.01)

# -----section 04_21: Inverse Fourier transform for bandstop filtering-----

srate = 1000
time = np.arange(0, 2 - 1 / srate, 1 / srate)
pnts = len(time)

# signal
signal = np.sin(2 * np.pi * 4 * time) + np.sin(2 * np.pi * 10 * time)

fourTime = np.arange(0, pnts) / pnts
fCoefs = np.zeros(len(signal), dtype=complex)

for fi in range(0, pnts):
    # create complex sine wave
    csw = np.exp(-1j * 2 * np.pi * fi * fourTime)

    # compute dot product between sine wave and signal
    fCoefs[fi] = np.dot(signal, csw) / pnts

# frequencies in Hz
# hz = np.linspace(0, srate / 2, int(np.floor(pnts / 2.0) + 1))

hz = np.linspace(0, srate, pnts)

fCoefsMod = np.copy(fCoefs)

freqidx = np.argmin(np.abs(hz - 10))
fCoefsMod[freqidx] = 0
fCoefsMod[-freqidx] = 0

plt.plot(hz, np.abs(fCoefsMod), 'r')
plt.plot(hz, np.abs(fCoefs))

reconMod = np.zeros(len(signal), dtype=complex)
for fi in range(0, pnts):
    csw = fCoefsMod[fi] * np.exp(1j * 2 * np.pi * fi * fourTime)
    reconMod = reconMod + csw

plt.plot(time, signal)
plt.plot(time, np.real(reconMod))

