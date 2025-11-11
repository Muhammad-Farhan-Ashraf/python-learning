"""Find factorial by recursion"""
def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

result=fac(5)
print(result)

"""Recursion of function and set limit """
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15)
i=1
def count():
    global i
    a=1
    b=2
    c=a+b
    print(c, i, "times")
    i+=1
    count()
count()
