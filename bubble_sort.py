def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] >nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[25,34,64,1,6,8,2]
sort(nums)
print(nums)
s="abc"
res=""
print(len(s))
for i in range(len(s)):
    for j in range(i):
        res+=s[j]
print(res)
from numpy import random
#x=random.randint(100,(5))
x=random.randint(100, size=(5))

print(x)
import numpy as np
y=np.array([5,7,5,3,4,6,7,8,9])
z=y
x=np.random.randint(100, size=[2,6])
y=random.choice([1,4,3,6], p=[0.1,0.1,0.4,0.4], size=(10))
print(y)
random.permutation(z)
print(z)