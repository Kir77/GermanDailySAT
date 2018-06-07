# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyEMD import EMD
import matplotlib.pyplot as plt
import numpy as np

with np.load('/Applications/Documents/research/Germany/GermanyT.npz') as data:#open the dataset
#initialize
    lat=data['lat']
    lon=data['lon']
    T=data['T']
    tim=data['tim']
  
#assign EEMD to 'eemd' variable
emd=EMD()
#execute EEMD on T
IMFs=emd.emd(T[:,1,1])
nIMFs=IMFs.shape[0]+1
#plot results
plt.figure(figsize=(12,9))
plt.subplot(nIMFs,1,1)
plt.plot(tim,T[:,1,1],'r')

for n in enumerate(IMFs):
    plt.subplot(nIMFs,1,n+2)
    plt.plot(tim,IMFs[n],'g')
    plt.ylabel("IMF %i" %(n+1))
    plt.locator_params(axis='y',nbins=5)

plt.xlabel("Time [time]")
plt.tight_layout()
plt.savefig('/emd_example',dpi=150)
plt.show()

print('done')