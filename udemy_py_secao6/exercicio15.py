NP = int(input("Insert a positive number: "))
if NP > 0:
    for num in range(1, NP):
        if num % 2 != 0:
            print(num)
else:
    print("You must insert an positive number! Try again!")





