from numpy import *
arr=array([10,2,3,4,5])
arr_m=arr+5
print(arr_m)
for i in arr:
    print(i+5)
arr2=array([11,12,13,14,15])
arr3=arr+arr2
print(arr3)
print("Sum of array", sum(arr))
print("sqrt of array", sqrt(arr))
print("sort of array", sort(arr))
print("type of array", type(arr))
print("max of array", max(arr))
print("min of array", min(arr))
print(concatenate([arr,arr2]))
"""copying array with same id"""
arr4=arr
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))
"""copying array with different id or shallow copy"""
arr4=arr.view()
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))
"""copying array as deep copy"""
arr4=arr.copy()
arr[2]=11
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))
