# Data Input
num1 = int(input("Insert the first number: "))
num2 = int(input("Insert the second number: "))
# Counting
soma = 0
multi = 1
# looping
for numb in range(num1, num2 + 1):
    if numb % 2 == 0:
        soma += numb

    else:
        multi *= numb

# printing
print(f" A soma dos numeros pares é {soma}")
print(f" A multiplicação dos numeros impares é {multi}")


