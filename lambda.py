f=lambda a,b : a+b
result=f(3,10)
print(result)
"""use of filter in lambda"""
nums=[1,4,23,65,7,98,9,3,6,4,3,21]
even=list(filter(lambda n:n%2==0, nums))
print(even)
"""use of map function in lambda"""
dobule=list(map(lambda n: n*2, even))
print(dobule)

"""use of reduced function in lambda"""
from functools import reduce
sum=reduce(lambda a,b:a+b, nums)
print(sum)
