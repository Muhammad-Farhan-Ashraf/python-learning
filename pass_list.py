def test(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
#lst= [1, 5, 8, 5, 3, 8, 5, 12, 5, 8]
user_input=input("Enter numbers separated by spaces: ")
lst = list(map(int, user_input.split()))

even, odd=test(lst)
print("Even numbers are",even)
print("Odd numbers are", odd)
