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
class BankAccount:
    def __init__ (self,account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print("Deposit", amount)
    def withdraw(self,amount):
        if amount> self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
    def show_balance(self):
        print("Current balance", self.balance)
name=input("Enter name:  ")
balance=float(input("Enter balance:  "))
acc1=BankAccount(name,balance)
acc1.deposit(100)
acc1.withdraw(300)
acc1.show_balance()

class Rectengale:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length*self.width
        print (" Area" , area)
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print("Perimeter", perimeter)
rec=Rectengale(4,5)
rec.area()
rec.perimeter()
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def car_info(self):
        print("brand name: ", self.brand)
        print("car model:", self.model)
        print("year:", self.year)
    def car_age(self, current_year):
        age=current_year-self.year
        print("Car age", age)
current_year=int(input("write current year"))
c=Car("BMW",2020,2010)
c.car_info()
c.car_age(current_year)
class python:
    def execute(self,ide):
        ide.execute()
class Editor:
    def execute(self):
        print("spell check")
        print("Age filter")
ide=Editor()
a=python()
a.execute(ide)