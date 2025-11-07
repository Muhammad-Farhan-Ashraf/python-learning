from numpy import *
arr=array([[1,2,3,4],
           [5,6,7,8]]
          )
print(arr)
"dimension of array"
print(arr.ndim)
print(arr.dtype)
print(shape(arr))
print(arr.size)
"""Convert multiple dimension to single dimension array"""
arr2=arr.flatten()
print(arr2)
arr3=array([[2,3,4,5,6,7],
            [11,12,13,14,15,16]
            ])
print(arr3.reshape(1,3,4))
"""convert array to matrix"""
mat=matrix(arr3)
print(mat)
m=matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
"""Diagonal of matrix"""
print(diag(m))
"""Multiply matrix"""
m1=matrix('2 3 4 ; 5 6 7; 8 9 10')
m2=matrix('2 3; 4 5; 6 7')
m3=m1*m2
print(m3)