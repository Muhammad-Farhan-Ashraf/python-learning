from time import *
from threading import *
class Heloo(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)
class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)
O1=Heloo()
O2=Hi()
O1.start()
sleep(0.2)
O2.start()
O1.join()
O2.join()
print("Thanks and By")
x=1
for _ in range(3):
    x+=x
    x-=1
print(x)
lis=[1,3,5,7,8,9,0,1,5,78,96]
n=30
def search(lis,n):
    l=0
    u=len(lis)-1
    while l<= u:
        mid=(l+u)//2
        if lis[mid]==n:
            return True
        else:
            if lis [mid]<n:
                l=mid+1
            else:
                u=mid-1
if search(lis,n):
    print("Found")
else:
    print("not found")
lii=[5,7,8,2,3]
print(sorted(lii))