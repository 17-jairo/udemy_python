NP = int(input("Insert a positive number: "))
if NP > 0:
    for num in range(NP, 0, -1):
        if num % 2 == 0:
            print(num)
else:
    print(" You must insert a positive number! Try again!")




