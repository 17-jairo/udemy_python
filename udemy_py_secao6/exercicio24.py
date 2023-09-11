num1 = int(input("Insert a positive number: "))
soma1 = 0
if num1 > 0:
    for divisor in range(1, num1 + 1):
        if num1 % divisor == 0:
            print(divisor)
            soma1 += divisor
    soma2 = (soma1 - num1)
    print(f"The sum of divisors is: {soma2}")

else:
    print("Please, insert a positive number!")


