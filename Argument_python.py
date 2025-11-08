"""Types of Argument in python"""
"""Positional argument"""
def sum (a,b):
    c=a+b
    print(c)
sum(5,6)
"""Keyword argument"""
def info(name,age,education):
    print(name)
    print(age)
    print(education)
info(age=34, education="Masters", name="Thomas")
"""Default argument"""
def requirement(name, age=18):
    print(name)
    print(age)
requirement("Ahmed")
"""variable length"""
"""here b took argument as tuple"""
def plus(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)
    print(type(a))
    print(type(b))
plus(2,3,50,7)
"""Keyworded Variable Length Arguments"""
"""Passing keyword and argument"""
def info(name,**data ):
    print(name)
    for i,j in data.items():
        print(i,j)
info("Ali", age=30,town="Bonn", state="NRW")
info("Ahmed", age=13)