import math
num1 = int(input("Insira o numero: "))

if num1 > 0:
    raiz_quadrada = math.sqrt(num1)
    quadrado = num1 ** 2
    print(f"A raiz quadrada é {raiz_quadrada:.2f} e o número elevado ao quadrado é {quadrado:.2f}.")
else:
    print("Número inválido, favor inserir numero positivo!.")

