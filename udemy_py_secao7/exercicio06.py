lista1 = []

for i in range(10):
    num = int(input(f"Insert the number {i}: "))
    lista1.append(num)
maior = max(lista1)
menor = min(lista1)

print(f'The max value on the list {lista1} is {maior} and the minus is {menor}')
