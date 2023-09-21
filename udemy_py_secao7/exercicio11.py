lista1 = []
conta = 0
soma = 0
for i in range(10):
    num = int(input(f"Insert the number {i +1}: "))
    lista1.append(num)
    if num < 0:
        conta += 1
    elif num > 0:
        soma += num
print(lista1)
print(conta)
print(soma)

