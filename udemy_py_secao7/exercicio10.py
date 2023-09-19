lista = []
num = 0
while len(lista) < 15:
    print(f"Insert the score {len(lista) + 1}: ")
    num = float(input())
    if 0 < num:
        lista.append(num)
    else:
        print("Please insert just positive numbers!")
        continue

media = sum(lista)/len(lista)
print(f'The list is {lista}')
print(f'A average is {media}')

