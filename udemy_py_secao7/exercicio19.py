lista1 = []  # Create an empty list

# Ask the user to insert 10 numbers and store them in lista1
for i in range(50):
    num = (i+(5*i)) % (i+1)
    lista1.append(num)

print(lista1)
