lista1 = []

for i in range(10):
    num = int(input(f"Insert the number {i}: "))
    lista1.append(num)
lista2 = []
for im in lista1:
    if im % 2 == 0:
        lista2.append(im)
print(f"The numbers are {lista1}")
print(f"The even numbers are {lista2}")
print(f'The list have {len(lista2)} numbers')
