"""Prime numbers"""
print("Lets check prime numbers")
num=int(input("Please write number:" ))
if num<2:
    print("its not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("its not prime")
            break
    else:
            print("its prime")
