"""use of conditions """
"""Even and odd number test"""
num=int(input("Please input the number:"))
reminder=num%2
print(reminder)
if reminder ==0:
    print("its Even number")
else:
    print("its odd number")
"""Nested if"""
num=int(input("Please input the number:"))
reminder=num%2
if reminder ==0:
    print("its Even number")
    if num>=0:
        print("its positive number")
    else:
        print("its negative number")

else:
    print("its odd number")
"""If,elif, else conditions"""
name=(input("Please input the name:"))
print("user name is", name)
age=int(input("please enter your age:"))
print("user ager is", age)
if age<17:
    print("Sorry you are not eligible for driving")
elif age>=18 and age<=60:
    print("You can apply for driving lic")
else:
    print("you are senior citizen, You can call Gov.t transport service")
print("we have checked all the conditions")
print("Thanks")