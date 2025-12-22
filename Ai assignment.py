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