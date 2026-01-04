x=3
y=4
print(x+y)
a="Hello "
b="world"
print(int.__add__(3,5))
print(str.__add__(a, b))
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return self.value + other.value
        else:
            return "Addition not supported"


x = Number(4.7)
y = Number(4)

print(x + y)
class Student:
    def sum(self,a,b,c):
        s=a+b+c
        print(s)
x=Student()
x.sum(5,4,5)
#Method Overriding
class Father:
    def show(self):
        print("its my father assets ")
class child(Father):
    def show(self):
        print("My assets")
a=Father()
a.show()
b=child()
b.show()

