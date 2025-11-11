user_input = int(input("enter the value:"))
n = user_input
def fibo(n):

    a=0
    b=1
    if n==1:
        print(a)
    elif n<=0:
        print("please write valid number")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c >= 100:
                break
            print(c)

fibo(n)
def fact(d):
    f=1
    for i in range(1,d+1):
        f=f*i
    return f
d=int(input("Write number for factorial: "))
result=fact(d)
print(result)