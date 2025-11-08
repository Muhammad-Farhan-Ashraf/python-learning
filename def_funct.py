def day():
    print("Hello")
    print("Guten tag")
day()
def calculator():
    number=int(input("Write number here: "))
    for i in range(1,11):
        result=i*number
        print(i,"*", number, "=", result)
calculator()
def multiply(x,y,z):
    a=x*y*z
    print(a)
multiply(3,4, 6)
def update(x):
    x=8
    print(x)

a=10
update()
print(a)