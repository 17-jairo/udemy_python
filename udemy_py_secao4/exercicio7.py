
'''
num1 = float((input("Insert the temperature in ºF: ")))
conv1 = 5.0 * (num1-32.0)/9.0
print('The temperature in ºC is', conv1)

In this case the output have a lot of decimals (31.88888888888889).
To fix it, we need to insert the 2f in the formula, as discribed below:
'''

num1 = float((input("Insert the temperature in ºF: ")))
conv1 = 5.0 * (num1-32.0)/9.0
print(f'The temperature in ºC is: {conv1:.2f}')