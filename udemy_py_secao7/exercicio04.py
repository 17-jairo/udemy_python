lista1 = []
for item in range(8):
    valor = int(input(f"Insert the number {item + 1}: "))
    lista1.append(valor)
print(lista1)
X = int(input("Insert a number between 0 and 7: "))
Y = int(input("Insert a number between 0 and 7: "))
soma = 0
if 0 <= X <= 7 and 0 <= Y <= 7:
    soma = lista1[X] + lista1[Y]
    print(f"The list is: {lista1}")
    print(f'The number in the position {X} is {lista1[X]}')
    print(f'The number in the position {Y} is {lista1[Y]}')
    print(f'A soma de X e Y é: {soma}')
else:
    print("Your number is incorrect, insert a number BETWEEN 0 and 7!")



