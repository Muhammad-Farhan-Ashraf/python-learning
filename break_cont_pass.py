""""Break, Continue and pass"""
"use of break statment"
items= 5
order=int(input("plese select number of items for order:"))
i=1
while i<=order:
    print("Ordered")
    x=i
    i += 1
    if i>5:
        print("out of stock")
        break
print("Sorry we have only",x,"items" )
"""Continue Statment"""
items=5
order=int(input("plese select number of items for order:"))
i=1
while i<=order:
    if i==6:
        print("Sorry no further order")
        print("we tested continue and break loop jointly")
        break
    print("Ordered")
    i += 1
    if i==6 :
        print("out of stock")
        continue

"""Pass statment"""
print("lets find number not divisible by 3 and 5")
#n=int(input("Please write number: "))
for i in range(20):
    if i%3==0 or i%5==0:
        pass
    else:
        print(i)
print("END")