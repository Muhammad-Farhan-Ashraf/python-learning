"""Array use"""
from array import *
value=array("L",[9,7,8,6,9,9,0,0],)
print(value)
for i in range(8):
    print(value[i])
num=array('f', [3,6,9,4,0.6])
print(num)
print(type(num))
"""Input from user for array value"""
val=array('f',[])
n=int(input(" Enter the length of array: "))
for i in range(n):
    a=int(input("Input your next value: "))
    val.append(a)
print(val)
"""Search in Array and print index numbder"""
ser=int(input(" Enter the value to search:"))
x=0
for m in val:
    if m==ser:
        print(x)
        break
    x+=1

