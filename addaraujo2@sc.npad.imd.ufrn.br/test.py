from v0 import *
import pandas as pd
import time

t0 = time.time()
SHAPE_FOLDER = '/home/adelsondias/Repos/newcastle/air-quality/shape/Middle_Layer_Super_Output_Areas_December_2011_Full_Extent_Boundaries_in_England_and_Wales/'
DATA_FOLDER = '/home/adelsondias/Repos/newcastle/air-quality/data_30days/'
metadata0, sfeat, sensors0 = load_data(SHAPE_FOLDER, DATA_FOLDER)
print('data loaded -',time.time()-t0)

variables =  {
        'sensors':['NO2','Temperature','O3','CO'],
        'exogenous':['primary','trunk','motorway','traffic_signals','day','dow','hour']
}

sensors, metadata = resampling_sensors(sensors0, metadata0, variables, 'H')
print('sensors resampled -',time.time()-t0)
print(sensors.shape)
zx, zi = ingestion(sensors, metadata, sfeat, variables, 5, 'NO2', 'randomized')
zx.to_csv(DATA_FOLDER+'zx.csv')
zi.to_csv(DATA_FOLDER+'zi.csv')
print('ingestion completed -',time.time()-t0)
