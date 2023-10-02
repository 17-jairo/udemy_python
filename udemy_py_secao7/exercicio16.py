lista1 = []  # Create an empty list

for i in range(5):  # Ask for insert 5 numbers
    num = int(input(f"Insert the number {i + 1}: "))
    lista1.append(num)

for f in range(3):
    print('Insert the option 0 if you want to end the program, '
          '\nInsert the option 1 if you want to see the list organized in order, '
          '\nInsert the option 2 if you want to see the list inverted.')
    num1 = int(input("Insert the option: "))
    if num1 == 0:
        print("Program finished!")
        break
    elif num1 == 1:
        lista1.sort()
        print(lista1)
        break
    elif num1 == 2:
        lista1.reverse()
        print(lista1)
        break
    else:
        print("You are inserting the wrong numbers!")


