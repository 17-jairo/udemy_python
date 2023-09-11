soma = 0
for numero in range(1, 1000):
    if numero % 3 == 0 or numero % 5 == 0:
        print(numero)
        soma += numero
print(f"The sum of the divisors is {soma}")
