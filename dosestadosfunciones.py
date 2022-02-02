# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:07:41 2022

@author: Alan Covarrubias
"""
import sympy as sp
import matplotlib.pyplot as plt
from scipy.constants import *
import numpy as np
u= sp.symbols('u')
n= sp.symbols('n')
t=sp.symbols('t')
K=sp.symbols('K')
epsilon=1
#n=100

s=lambda u: K*u/epsilon*(sp.log((n*epsilon/u)*(1-u/(n*epsilon)))
                         -n*epsilon/u*sp.log(1-u/(n*epsilon)))


#
K=1
n=20000

expr=(sp.diff(s(sp.Symbol('u')),u)**-1)-t
u_t=(sp.solve(expr,u)[0]).simplify()
t_u=(sp.solve(expr,t)[0]).simplify()
print('U(T)='+str(u_t))
print('T(U)='+str(t_u))



u_func=sp.lambdify(t,u_t)
t_func=sp.lambdify(u,t_u)


t=np.linspace(1,10,100)
u=np.linspace(1,1000,10000)
plt.figure(0)
plt.title('$U=U(T,N=%d)$' %n)
plt.plot(t,u_func(t))
plt.figure(1)
plt.title('$T=T(U, N= %d)$'%n)
plt.plot(u,t_func(u))
