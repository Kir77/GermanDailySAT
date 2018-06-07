# -*- coding: utf-8 -*-
"""
load nc-file(python2.7)
"""
import numpy as np
import netCDF4 as nc

data=nc.Dataset('/home/qmdeng/Downloads/tg_0.25deg_reg_v17.0.nc') #open the dataset
#initialize
lati=data.variables['latitude'][86:120]
longi=data.variables['longitude'][181:223]
Tg=data.variables['tg'][:,86:120,181:223]
time=data.variables['time']
print(lati[0])
print(lati[-1])
print(longi[0])
print(longi[-1])
lat=np.asarray(lati)
lon=np.asarray(longi)
T=np.asarray(Tg)
tim=np.asarray(time)
np.savez('GermanyT.npy',lat,lon,T,tim)