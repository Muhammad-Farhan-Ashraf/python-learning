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
