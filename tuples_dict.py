#tuple
tup=(92,5,8,8,33,77)
print(tup)
#tuple value can not change
#sAcess values
print(tup[1])
#count the specific value
print(tup.count(8))
#set
set={1,5,4,78,39,9}
print(set)
#Duplicate value
duplicate_set={1,4,34,54,34,65,7}
#set will exempt duplicate values
print(duplicate_set)
"""Dictionary in Python"""
diction={1:"Farhan", 2:"Ashraf", 3:"Ali", 5:"Thomas"}
print(diction)
# call by key
print(diction[1])
#missing key and value
print(diction.get(4,"Chris"))
#merge key and values
candidate=["Ali", "Thomas", "Chris","Nick"]
score=[54,65,34,44]
data=dict(zip(candidate,score))
print(data)
#call by key values
print(data["Ali"])
#add new value
data["Harsh"]=78
print(data)
#Dictionary in Dictionary
subject={"Ali":"Math","Thomas":{"Math","Physics"},"Harry": {"Economics","Chemistry"}}
print(subject)
#call by key
print(subject["Ali"])
print(subject["Harry"])