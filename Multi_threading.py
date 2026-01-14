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