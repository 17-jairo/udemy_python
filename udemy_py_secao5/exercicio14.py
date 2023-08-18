import numpy as np
num1 = float(input("Insert the grade 1: "))
num2 = float(input("Insert the grade 2: "))
num3 = float(input("Insert the grade 3: "))

values = np.array([num1, num2, num3])
peso = np.array([2, 3, 5])

media_pond = np.average(values, weights=peso)

if 0 <= media_pond <= 2.9:
    print(f"Your score is {media_pond:.2f}, and you are reproved!")
elif 3 <= media_pond <= 4.9:
    print(f"Your score is {media_pond:.2f}, and you are in retention!")
else:
    print(f"Your score is {media_pond:.2f}, and you are approved!")