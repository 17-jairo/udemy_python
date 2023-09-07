NP = int(input("Insert a positive number: "))
if NP > 0:
    for num in range(NP, 0, -1):
        print(num)
else:
    print(" You must insert an positive number! Try again!")

