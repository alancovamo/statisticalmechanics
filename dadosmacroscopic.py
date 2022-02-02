# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:41:57 2022

@author: Alan Covarrubias
"""
import matplotlib.pyplot as plt
from numpy import *

x=[i+1 for i in range(6)]

sums=[]

for i in x:
    for j in x:
       sums.append(i+j) 
       
bins= arange(2,14) - 0.5       
plt.hist(sums,bins,rwidth=0.8) 
plt.xlabel('Estado macroscopico dado_1+dado_2')
plt.ylabel('Numero de estados microscopicos')
plt.xticks(ticks=[i for i in range(1,14) ]) 
#plt.grid(True)     
       