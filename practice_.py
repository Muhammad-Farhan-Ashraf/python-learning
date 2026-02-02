"""Basic Practice (Variables, Loops, Conditions)"""
"Odd or Even Checker"
print("check the number Even or Odd")
number=int(input("Write your number: "))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")
n=int(input("Write your numer for addition "))
total=0
i=1
while i<=n:
    total+=i
    i+=1
print("Sum for ", n, "is", total)
dig=int(input(" Write a number for table:"))
for i in range(1,11):
    b=i*dig
    print(i, "*",dig,"=",b)
"""Reverse order"""
print("Reverse order table ")
for i in range(10,0,-1):
    print(f"{i} * {dig}={i * dig}")
"""Print multiplication tables from 1 to 3, each table up to 10"""
print("Loop inside loop")
for i in range(1,4):
    print(f"\ntable of ", i)
    for j in range(1,11):
        print(f"{i} * {j}= {j*i}")
"""Level 2: Lists and Strings
Maximum in a List with out using built in function"""
l=[100,4,6,87.54,85,90,55]
def maximum(nums):
    b=sorted(nums)
    print("Maximum value is ", b[-1])
maximum(l)
"""Ask the user for a string and print it backwards."""
string_check=input("Write here string: ")
rev=string_check[::-1]
print(rev)
"""Count the number of vowels in a user-input string"""
vowel_input=input("Write to check vowels: ").lower()
v_s=0
v_c=["a", "e", "i", "o", "u"]
for ch in vowel_input:
    for i in v_c:
        if ch==i:
            v_s+=1
print(v_s)
"""Find minimum without using built in function"""
l=[100,4,6,87.54,85,90,55]
def mini(nums):
    b=sorted(nums)
    print("Minimum value is ", b[0])
mini(l)
"""4️⃣ Write a function to find second largest number in a list"""
l=[100,40,60,870,54,85,90,55]
def s_mini(nums):
    b=sorted(nums)
    print("Second largest value is ", b[-2])
s_mini(l)
""""2️⃣ Check if a string is a palindrome"""
pali=input("Write a string: ")
rvalue=pali[::-1]
if rvalue==pali:
    print("yes its palindrome")
else:
    print("its not palindrome")
"""Count words in string"""
a="Lets count words in string"
print(a)
count=0
words=a.split()
print(words)
for ch in words:
    count+=1
print(count)
