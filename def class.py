class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("The user details are ", self.name, self.age)
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
f1=person("Ali", 6)
f2=person("Rehan",65)
if f1.compare(f2):
    print("age is same")
else:
    print("Age is different")
f1.myfunc()
f2.myfunc()
class car:
    wheels=4
    def __init__(self):
        self.model="BMW"
        self.mil=10
        self.fuel="electric"
c1=car()
print(c1.model,c1.mil,car.wheels)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Name", self.name)
        print("Age", self.age)
c1=student("ali",35)
c1.info()
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        if self.b==0:
            return "Can not divided by zero"
        return self.a/self.b
    def all(self):
        print("Addition", self.add())
        print("Subtraction", self.subtract())
        print("Multiplication", self.multiply())
        print("Division", self.divide())

a1=calculator(60,0)
a1.all()