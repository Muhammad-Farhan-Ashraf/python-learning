"""Numbers & Math Operations
Task: Basic Calculator (without using eval)
Create a program that:
Asks the user for two numbers
Asks for an operation (+, -, *, /, //, %, **)
Performs the operation
Handles division by zero gracefully."""
print("Basic calculator")
x=int(input("please write your first number:"))
y=int(input("please write your second number:"))
z=input("Please provide the operator:")
if z=="+":
    c=x+y
    print(c)
elif  z=="-":
    c=x-y
    print(c)
elif  z=="*":
    c=x*y
    print(c)
elif z=="/":
    if y==0:
        print("Error")
    else:
        c=x/y
        print(c)
elif z=="//":
    if y==0:
        print("Error")
    else:
        c = x // y
        print(c)
elif z=="%":
    if y==0:
        print("Error")
    else:
        c = x % y
        print(c)
else:
    print("Invalid operator")

"""Task: Word Analyzer
Take a sentence as input and print:
Number of words
Number of characters (excluding spaces)
Count of vowels and consonants
The sentence reversed"""
print("Word Analyzer")
user=input("Write your thoughts: ")
words=user.split()
word_count=len(words)
char_count=len(user.replace(" ",""))
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for ch in user:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
reversed_sentence = user[::-1]
print("user sentence",user)
print("numbers of words",word_count)
print("Number of characters", char_count)
print("vowels", vowel_count)
print("Consonants", consonant_count)
print("Reversed", reversed_sentence)
"""
1. Add element  
2. Remove element  
3. Search element  
4. Display list  
5. Exit
"""
m_lis=[]
x=input("write to add: ")
items=x.split(",")
items = [i.strip() for i in items]
m_lis.extend(items)
print("Liat after adding", m_lis)
y=input("write to remove: ")
if y in m_lis:
    m_lis.remove(y)
    print("List after removing", m_lis)
else:
    print("Item not founded in list")
search=input("Write to search:")
