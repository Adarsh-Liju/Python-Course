import math#immporting math module
x1 = float(input("Enter the x1 value: "))#input x1 value
y1 = float(input("Enter the y1 value: "))#input y1 value
x2 = float(input("Enter the x2 value: "))#input x2 value
y2 = float(input("Enter the y2 value: "))#input y2 value
print("The value of x1 ",x1,"\nThe value of x2 ",x2,"\nThe value of y1 ",y1,"\nThe value of y2 ",y2)#displaying x1,x2,y1,y2 values
dist=math.sqrt(((y2-y1)**2)+((x2-x1)**2))#calculating distance between them
print("Distance between the two points is : ",dist)#displaying distance value

