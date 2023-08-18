import numpy as np
num1 = float(input("Insert the grade 1: "))
num2 = float(input("Insert the grade 2: "))
num3 = float(input("Insert the grade 3: "))

values = np.array([num1, num2, num3])
peso = np.array([1, 1, 2])

media_pond = np.average(values, weights=peso)

if media_pond > 7:
    print(f"Your score is {media_pond:.2f}, and you are approved!")
else:
    print(f"Your score is {media_pond:.2f}, and you are REPROVED!")

