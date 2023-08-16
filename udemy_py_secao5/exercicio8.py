import math
num1 = float(input("Insert the first grade: "))
num2 = float(input("Insert the second grade: "))
number = [num1, num2]
if 0 <= num1 <= 10 and 0 <= num2 <= 10:
    soma = math.fsum(number)
    medin = soma / len(number)
    print(f"A média é {medin:.2f}")
else:
    print("Os valores inseridos não são validos.")





