lista = []
num = 0
while len(lista) < 6:
    print(f"Insert the number (just even numbers are accepeted) {len(lista) + 1}: ")
    num = int(input())
    if num % 2 == 0:
        lista.append(num)
    else:
        print("Please insert just even numbers!")
        continue


print(f'The list is {lista}')











