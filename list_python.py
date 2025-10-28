#list
nums=[25,12,65,98,30]
print(nums)
#specific index
print(nums[3])
#list string
fruit=["Apple", "Orange", " Banana", "Cheery"]
print(fruit)
#list of different data type
values= ["Farhan", 57, "Ali",5,76," Asharf"]
print(values)
#add item in list
values.append("Thomas")
print(values)
#insert
values.insert(3,"77")
print(values)
#Delete value in list
values.remove(76)
print(values)
print(values.pop(5))
#extend list
number= [1,5,7,3]
print(number)
number.extend([54,23])
print(number)
#minimum value
print("minimum value in list",min(number))
#maximum value func
print("maximum value in the list", max(number))
#sort
number.sort()
print("sort out numbers", number)