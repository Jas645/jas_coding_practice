import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

scan_rate = 0.2
E_start = -0.1
E_reverse = 0.6
t_total = (E_reverse-E_start)/scan_rate
freq = 10
Vamp = 0.15
t_interval = 0.000014
N = int((t_total)/t_interval)

t_ox = np.linspace(0, t_total, N)
t_red = np.linspace(t_total, 2*t_total, N)
t = np.concatenate((t_ox, t_red))

r_ox = np.linspace(E_start, E_reverse, N)
r_red = np.linspace(E_reverse, E_start, N)
r = np.concatenate((r_ox, r_red))

y = r + Vamp * np.sin(2*np.pi*freq*t)

if 2*N > 500000:
    raise ValueError("Error: Too many points!")
    
print (2*N)
    
       

plt.plot (t,y)
plt.show()
