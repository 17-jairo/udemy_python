num1 = int(input("Insert a positive number: "))

if num1 > 0:
    for divisor in range(1, num1 + 1):
        if num1 % divisor == 0:
            print(divisor)
            divisor += 1

else:
    print("Please, insert a positive number!")
