import sys
try :
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit()

try: 
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit()


print(f"{x} / {y} = {result}")