import numpy as np
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd

'''
def csv_to_list(csv_file):
    csv_f = pd.read_csv(csv_file, header=1)
    csv = csv_f.values
    time = csv[:, 0]
    lattitude = csv[:, 1]
    longitude = csv[:, 3]
    print (time)
    print(lattitude)
    print(longitude)
'''

csv_f = pd.read_csv('Master.csv', header=1)
csv= csv_f.values
time= csv[:,0]
lattitude=csv[:,1]
longitude=csv[:,3]
#np.ndarray(csv_f).tolist()
#csv_f.tolist()
print (time)
print(lattitude)
print(longitude)
#try_this = csv_f.iloc[0:1912, 1:2]


#csv_to_list('Master.csv')
new_lattitude=[]
for gps in lattitude:
    whole=int(gps/100)
    minute=gps-(100*whole)
    total_degree=whole+(minute/60)

    new_lattitude.append(total_degree)

lattitude_mean= np.mean(new_lattitude)
print(lattitude_mean)

new_longitude=[]
for gps in longitude:
    whole=int(gps/100)
    minute=gps-(100*whole)
    total_degree=whole+(minute/60)

    new_longitude.append(total_degree)

longitude_mean= np.mean(new_longitude)
print(longitude_mean)
print(len(new_longitude))
