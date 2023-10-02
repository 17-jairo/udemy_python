lista1 = [] # Create a empty list

for i in range(10): # Ask for insert 20 numbers
    num = int(input(f"Insert the number {i + 1}: "))
    lista1.append(num)

real_values = set() # Empty set to put the real numbers (without repeated)
removed_values = set() # Empty set to put the repeated numbers

for num in lista1: # Em seguida, ele usa dois conjuntos (real_values e removed_values) para rastrear os números únicos e
    # os números que foram removidos (repetidos), respectivamente
    if num in real_values:
        removed_values.add(num)
    else:
        real_values.add(num)

print(f'The list of numbers are {lista1}')
print(f'The repated numbers are {removed_values}')
print(f'The list without the repeated numbers are {real_values}')

