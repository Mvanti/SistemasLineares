# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:11:49 2024

@author: vanti
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def triangle(eps):
    pts = np.array([[-1*eps,0], [eps,0], [0,1/(eps)]])
    p = Polygon(pts, closed=True, fc=None)
    ax = plt.gca()
    ax.add_patch(p)
    ax.set_xlim(-3,3)
    ax.set_ylim(0,2)

    ax.set_xlabel('t(s)')
    ax.set_ylabel(r'$\Delta(t)$')


fig=plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.title(r'$\|\epsilon\|=2$')
eps=2
triangle(eps)



plt.subplot(1,3,2)
plt.title(r'$\|\epsilon\|=1$')
eps=1
triangle(eps)


plt.subplot(1,3,3)
plt.title(r'$\|\epsilon\|=0.5$')
eps=0.5
triangle(eps)


plt.show()