lista = []

for i in range(5):
    num = int(input(f'Insert the number {i+1}: '))
    lista.append(num)
print(f'The list is {lista}')
print(f"The position of the maximum number ({max(lista)}) is {lista.index(max(lista))} and the position of the minimum "
      f"value ({min(lista)}) is {lista.index(min(lista))}")




