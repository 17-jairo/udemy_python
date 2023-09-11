"Faça um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 após um numero dado."

num1 = int(input("Insert the number: "))
for numero in range(num1 + 1, num1 + 100):
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        print(numero)
        break


