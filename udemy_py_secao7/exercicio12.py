lista = []
num = 0
while len(lista) < 5:
    print(f"Insert the score {len(lista) + 1}: ")
    num = int(input())
    lista.append(num)

media = sum(lista)/len(lista)
print(f'The list is {lista} and the max value is {max(lista)}, the minimum value is {min(lista)} and the average is '
      f'{media}')



