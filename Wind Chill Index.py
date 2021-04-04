import math as m
spe=float(input("Input wind speed in km/hr : "))
ti=float(input("Input air temperature in Degrees Celsius: "))
wchill=13.12+0.6215*ti-11.37*m.pow(spe, 0.16)+0.3965*ti*m.pow(spe, 0.16)
print("The wind chill index is", int(wchill))