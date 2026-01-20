name=input("Please write your name:")
age=int(input("Your age:"))
favorite_color=input("Your favorite color:")
print("user name is ", name)
print("user age is ", age)
print("user favorite color is", favorite_color)
length=5
width=3
rec_area=length*width
print("Rectangle area is ", rec_area)
c=int(input("current temperature in cal:"))
f=c*9/5+32
print("temperature in Far",f)

number=int(input("mention a number : "))
if number>0:
    print("Its positive number")
elif number==0:
    print("Its equal to zero")
else:
    print("its negative number")
"""Grading system"""
score=float(input("write marks to check grades score:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("your grade is ", {grade})

### practice
x=float(input(" First number: "))
y=float(input(" Second number: "))
operator= input(" choose operations(+,-,*,/:) ")
if operator=="+":
    print(x+y)
elif operator=="-":
    print(x-y)
elif operator=="*":
    print(x*y)
elif operator=="/":
    if y==0:
        print("Error")
    else:
        print(x/y)
def comparison():
    a=float(input("write number"))
    b=float(input("write sec number"))
    if a==b:
        print("equal" )
    elif a!=b:
        print("Not equal")
    elif a>b:
        print("a is greater then b")
    else:
        print("B is greater ")
comparison()
def log():
    onum=45
    snum=50
    if onum>=snum:
        print("first number is greater")
    elif onum<=snum:
        print("second number is greater")
log()
