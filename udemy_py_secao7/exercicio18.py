lista1 = []  # Create an empty list

# Ask the user to insert 10 numbers and store them in lista1
for i in range(10):
    num = int(input(f"Insert the number {i + 1}: "))
    lista1.append(num)

X = int(input("Insert the number that you want to check if is a multiple of in the list: "))  # Read X from the user
contador = 0  # Initialize a counter for multiples of X
lista2 = []  # Create an empty list to store multiples of X

# Iterate through the elements in lista1
for num in lista1:
    if num % X == 0:  # Check if num is a multiple of X
        lista2.append(num)  # If it is, add it to lista2
        contador += 1  # Increment the counter

# Print the original list, the count of multiples, and the list of multiples
print(f'The original list is {lista1}')
print(f'There are {contador} multiples of {X} and they are listed here: {lista2}')
