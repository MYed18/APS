# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:12:00 2026

@author: marti
"""
import matplotlib.pyplot as plt
import numpy as np

#%%  Definimos función 
def mi_funcion_sen(vmax=1, dc=0, ff=1, ph=0, nn=1000, fs=1000):
    n_vector = np.arange(nn)
    tt = n_vector / fs
    
    xx = vmax * np.sin(2 * np.pi * ff * tt + ph) + dc
    return(tt, xx)

#%% Parámetros generales 
N = 1000       # cantidad de muestras
vmax = 1.5     # amplitud
dc = 0         # nivel arbitrario (offset)
ff = 5         # frecuencia de la senoidal 
ph = 0         # fase
ff= 2001        #frecuencia
fs=1000

#%%  graficos
tt, xx = mi_funcion_sen(vmax=vmax, dc=dc, ff=ff, ph=ph, nn=N, fs=fs)
    
plt.figure()
plt.plot(tt, xx)
plt.title(f'Señal muestreada a ff = 2001 Hz')
plt.xlabel('Tiempo [segundos]')
plt.ylabel('Amplitud [Volts]')
plt.show()