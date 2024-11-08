# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:11:49 2024

@author: vanti
"""


import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

x=[-10,0,0,5,5,10]
y=[0,0,1,1,1,1]
z=[0,0,0,0,-1,-1]

plt.subplot(1,2,1)
plt.plot(x,y, color='b',label='$u(t)$')
plt.plot(x,z,color='r', label='$-u(t-5)$')
plt.xlabel(r'$t \in $ ($-\infty,\infty) $')

plt.legend()

x=[-10,0,0,5,5,10]
y=[0,0,1,1,0,0]

plt.subplot(1,2,2)
plt.plot(x,y,label='$u(t)-u(t-5)$')
plt.xlabel(r'$t \in $ ($-\infty,\infty) $')

plt.legend()





plt.show()