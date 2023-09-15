lista1 = []
for num in range(1, 11):
    num1 = int(input(f"Insert the number {num}: "))
    lista1.append(num1)

lista2 = []
for item in lista1:
    quadrado = item ** 2
    lista2.append(quadrado)

print(lista1)
print(lista2)

