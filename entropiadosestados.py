# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 12:11:31 2022

@author: Alan Covarrubias
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import *
############parametros

epsilon=1

def s(u,n):
    return k*u/epsilon*(np.log((n*epsilon/u)*(1-u/(n*epsilon)))
                        -n*epsilon/u*np.log(1-u/(n*epsilon)))

u=np.linspace(1,20000,20)

n=np.linspace(20001,20001*2,20)
U,N = np.meshgrid(u,n)
S=s(U,N)

fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('U')
ax.set_ylabel('N')
ax.set_zlabel('S')
ax.scatter(n[0]*epsilon/2,n[0],s(n[0]*epsilon/2,n[0]),c='Red',s=5**2)
ax.plot_surface(U, N, S, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('S=S(U,N)')




