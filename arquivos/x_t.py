# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:56:34 2023

@author: vanti
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np



fig, ax = plt.subplots()

x = np.linspace(-10, 10,21)
f=np.zeros(np.size(x))
f[10]=1
f[7]=(4+x[7])/4
f[8]=(4+x[8])/4
f[9]=(4+x[9])/4
# f[11]=f[9]
# f[12]=f[8]
# f[13]=f[7]

fc=np.zeros(np.size(x))

fc[9]=f[8]
fc[10]=f[10]
fc[11]=f[12]

fe=np.zeros(np.size(x))

fe[10]=1
fe[4]=(6+x[4])/6
fe[5]=(6+x[5])/6
fe[6]=(6+x[6])/6
fe[7]=(6+x[7])/6
fe[8]=(6+x[8])/6
fe[9]=(6+x[9])/6
fe[11]=fe[9]
fe[12]=fe[8]
fe[13]=fe[7]
fe[14]=fe[6]
fe[15]=fe[5]
fe[16]=fe[4]
ax.set_xlabel('$t$')
ax.set_ylabel('$ 1/\epsilon $')
ax.grid()
ax.plot(x, f);
# ax.plot(x, fc,label="$x_c(y)$");
# ax.plot(x, fe,label="$x_e(t)$");

plt.legend(loc="upper right")