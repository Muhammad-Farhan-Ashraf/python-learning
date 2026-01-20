x=5
y=6
try:
    print(x/y)
    inp = int(input("Write your number:"))
    print(inp)
except ZeroDivisionError as e:
    print("Helo: You can not divide a number by zero", e)
except ValueError:
    print("Value error")
finally:
    print("We have handel the errors")