# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 00:37:11 2023

@author: vanti
"""

import numpy as np
import matplotlib.pyplot as plt


def showConvolution(f1, f2, t0):
    
    # Cria função revertida e deslocada
    f_shift = lambda t: f2(t0-t)
    prod = lambda tau: f1(tau) * f2(t0-tau)

    # Plota as curvas 
    plt.plot(t, f1(t), label=r'$f_1(\tau)$')
    plt.plot(t, f_shift(t), label=r'$f_2(t_0-\tau)$')
    plt.fill(t, prod(t), color='r', alpha=0.5, edgecolor='black', hatch='//') 
    plt.plot(t, prod(t), 'r-', label=r'$f_1(\tau)f_2(t_0-\tau)$')
    plt.grid(True); plt.xlabel(r'$\tau$'); plt.ylabel(r'$x(\tau)$') 
    plt.legend(fontsize=10) 
    plt.show() 

Fs = 50  # frequência de amostragem
T = 5    # faixa d etempo de interesse
t = np.arange(-T, T, 1/Fs)  # amostras de tempo

f1 = lambda t: np.maximum(0, 1-abs(t))
f2 = lambda t: (t>0) * np.exp(-2*t)


fig=plt.figure(figsize=(10,7))

t0=-1
plt.subplot(411)
showConvolution(f1, f2, t0)

t0=-0.5
plt.subplot(412)
showConvolution(f1, f2, t0)

t0=0.5
plt.subplot(413)
showConvolution(f1, f2, t0)

t0=1
plt.subplot(414)
showConvolution(f1, f2, t0)

# f1 = lambda t: np.maximum(0, 1-abs(t))
# f2 = lambda t: (t>0) * np.exp(-2*t)

# Fs = 50  # our sampling frequency for the plotting
# T = 5    # the time range we are interested in
# t = np.arange(-T, T, 1/Fs)  # the time samples

# plt.plot(t, f1(t), label='$f_1(t)$')
# plt.plot(t, f2(t), label='$f_2(t)$')
# plt.legend()
# plt.grid()