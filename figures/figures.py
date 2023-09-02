#!/usr/bin env python

# imports
import numpy as np
import matplotlib.pyplot as plt
import os

# create sin wave

my_wave = np.sin(np.pi * np.linspace(1, 15, 100))

plt.plot(my_wave)
plt.title('Sin Wave')
direct = str(os.getcwd())
plt.savefig(direct + '/figures/sinewave.png', format='png')
