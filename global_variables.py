""""global variables"""
a=10
def check():
    a=int(input("Write your number: "))
    print("User input is ", a)
check()
print(a)
"""use global variable inside function"""
a=10
def check():
    global a
    a=int(input("Write your number: "))
    print("User input is ", a)
check()
print(a)
"""Use global and local variable in function"""
a=10
print(id(a))
def check():
    a=5
    x=globals()["a"]
    globals()["a"]=15
    print(id(x))
    print(a)
check()
print(a)
