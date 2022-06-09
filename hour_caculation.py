import pandas as pd
from numpy import sin, cos, arccos, pi, round
import numpy as np

VANTOC = 40

data = pd.read_csv("province.csv", encoding= 'utf-8')

def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2, unit = 'miles'):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    
    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)

        
latLong = data[["lat", "lng"]]
data[["lat", "lng"]].values[:2]

result = []
for i,valw in enumerate(latLong.values):
    distanceList = list()
    for j, valh in enumerate(latLong.values):
        ret = getDistanceBetweenPointsNew(*valh, *valw, "kilometers")
        distanceList.append(ret)
    result.append(np.array(distanceList))

result = np.array(result)/ VANTOC
provinces = data["Tỉnh"].to_numpy()

result = np.append(np.expand_dims(provinces, axis=1), result, axis=1)
provinces = np.append(np.array(["Tỉnh"]), provinces)

data = pd.DataFrame(result, columns= provinces).reset_index(drop=True)
print(data)
data.to_csv("hour_matrix.csv", index= False)