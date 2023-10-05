lista1 = []  # Create an empty list

for i in range(10):  # Ask for the insertion of 10 numbers
    num = int(input(f"Insert the number {i + 1}: "))  # Prompt the user to input a number
    lista1.append(num)  # Add the entered number to the list

print(f'The list is {lista1}')  # Display the original list

# Iterate through the list to check for negative numbers
for num in range(len(lista1)):
    if lista1[num] < 0:  # If a number is negative
        lista1[num] = 0  # Replace it with 0

print(f"The list after changing the negative numbers is {lista1}")  # Display the modified list

