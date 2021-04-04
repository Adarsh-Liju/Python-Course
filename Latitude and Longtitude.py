import math as ma
print("Input coordinates of two points:")
slat=ma.radians(float(input("Starting latitude: ")))
slon=ma.radians(float(input("Ending longitude: ")))
elat=ma.radians(float(input("Starting latitude: ")))
elon=ma.radians(float(input("Ending longitude: ")))
dist=6371.01*ma.acos(ma.sin(slat)*ma.sin(elat)+ma.cos(slat)*ma.cos(elat)*ma.cos(slon-elon))
print("The distance between the two places is : ",dist)
