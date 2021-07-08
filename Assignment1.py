#Program to find Area of Circle
rad=float(input("Enter the radius of circle: "))
from math import pi
area=(pi*rad**2)
print(area)




#Program to find Extension Checker
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
