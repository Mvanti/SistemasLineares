# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:11:49 2024

@author: vanti
"""


import matplotlib.pyplot as plt
import numpy as np



fig=plt.figure(figsize=(10,7))

t=np.linspace(-10,10,100)

s=0
omega=1.257

y=np.exp(s*t)*np.cos(omega*t)

plt.subplot(2,1,1)
plt.plot(t,y, color='b')
plt.xlabel('$ \sigma = 0$')

y1=np.exp (-0.5*t)
y2=np.exp(0.5*t)
plt.subplot(2,3,4)

plt.plot(t,y1,label='$\sigma $ < $ 0$')
plt.plot(t,y2,color='r',label='$\sigma $ > $ 0$')
plt.legend()
plt.xlabel('$\omega = 0$')

y1=np.exp (-0.08*t)*y

plt.subplot(2,3,5)

plt.plot(t,y1)
plt.xlabel('$\sigma $ < $ 0$')

y1=np.exp (0.08*t)*y

plt.subplot(2,3,6)

plt.plot(t,y1)
plt.xlabel('$\sigma $ > $ 0$')





plt.show()