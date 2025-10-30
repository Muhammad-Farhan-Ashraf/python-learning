"""How to import build in function of Math in python"""
#This command will create error as we have not import math function
"""x=5
print(sqrt(5))"""
import math
x=16
print("Square root of x is" ,math.sqrt(x))
print(math.exp(x))
#power function
print("Power of x is ", math.pow(x,2))
#floor value
y=6.9
print(math.floor(y))
#ceil value
print(math.ceil(y))
#absolute value
y=abs(-6.9)
print(y)
#minimum value
z=[54,65,34,78,6,90,61]
print(min(z))
#Maximum value
print(max(z))
#impoert math as some other name
import math as m
print(m.sin(90))
print(m.cos(45))
#Import some functions of math
from math import sqrt, pow, tan
print(sqrt(64))
print(pow(4,5))
print(tan(180))
#pi value
print(math.pi)



