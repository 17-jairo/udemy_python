import math
num1 = int(input("Insert a real number: "))
num2 = int(input("Insert the base: "))
if num1 < 0:
    print("Number not valid!")
else:
    log = math.log(num1, num2)
    print(f"the logarithm is {log:.2f}.")
