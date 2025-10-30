a=7
b=8
print(a)
print(b)
print(a+b)
#swap
a=a+b
b=a-b
a=a-b
print(a)
print(b)
#swap by assign
a=76
b=65
a,b=b,a
print(a)
print(b)
#swap by xor
x=6
y=20
x=x^y
y=x^y
x=x^y
print(x)
print(y)
