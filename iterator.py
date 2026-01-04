nums=[5,78,6,9,45]
for i in nums:
    print(i)
#Iterator usage
it=iter(nums)
print(it.__next__())
print(it.__next__())
# Create own objects
class Onebyone:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=15:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
c1=Onebyone()
for i in c1:
    print(i)