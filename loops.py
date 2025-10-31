"""While loops"""
count=1
name="Farhan"
while count<=10:
    print(count, name)
    count=count+1
print("tested while loop")
"""Nested while loop"""
add=1
count=15
while add<=8:
    print("Increment by one", add)
    while count>10:
        print(count, "its inner loop")
        count=count-1
    add=add+1
print("good bye")
"""For loop"""
name="Thomas Jefferson"
for i in name:
    print(i)
list=["Ammar", "Hasan",2,65,"Abdul"]
for i in list:
    print(i)
for i in range(1,21):
    if i%3!=0:
     print(i)
print("its for loop with condition of if")
print("practice  ")
