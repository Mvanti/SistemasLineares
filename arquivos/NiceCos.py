# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:56:34 2023

@author: vanti
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-2*np.pi, 2*np.pi, 200)
f = np.cos(x)

ax.xaxis.set_major_locator(MultipleLocator(0.5*np.pi))
ax.yaxis.set_major_locator(MultipleLocator(0.5))

def format_func(value, tick_number):
    """Formatter for setting the xticks to multiples of \pi/2."""

    mult_pi_half = int(np.round(2 * value / np.pi))

    sign = "-" if mult_pi_half < 0 else ""

    if mult_pi_half == 0:
        return "0"
    elif abs(mult_pi_half) == 1:
        return '$' + sign + r'\frac{\pi}{2}' + '$'
    elif abs(mult_pi_half) == 2:
        return '$' + sign + r'\pi $'
    elif mult_pi_half % 2 > 0:
        return r'$\frac{' + str(abs(mult_pi_half)) + '\pi}{2}$'
    else:
        return r"${0}\pi$".format(mult_pi_half // 2)

ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))

ax.set_xlabel('$\omega t$')
ax.set_ylabel(r'$\cos(\omega t)$')
ax.grid()
ax.plot(x, f);