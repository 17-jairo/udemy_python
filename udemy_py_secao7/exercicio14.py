lista1 = []

for i in range(10):
    num = int(input(f"Insert the number {i + 1}: "))
    lista1.append(num)

number_not_repeated = set()  # Create an empty set to store non-repeated numbers.
num_dupli = set()  # Create an empty set to store duplicated numbers.

for num in lista1:  # Iterate through the 'lista1' list.
    if num in number_not_repeated:  # Check if the number is already in the 'number_not_repeated' set.
        num_dupli.add(num)  # If it's a duplicate, add it to the 'num_dupli' set.
    else:
        number_not_repeated.add(num)  # If it's not a duplicate, add it to the 'number_not_repeated' set.

non_repeated_numbers = number_not_repeated.difference(num_dupli)  # Find non-repeated numbers using set difference.

# Print the original list and the non-repeated numbers.
print(f'The numbers are {lista1}')
print(f'These are the numbers not repeated: {list(non_repeated_numbers)}')  # Printing and transforming the set in a list
print(f'These are the number duplicated {list(num_dupli)}')












