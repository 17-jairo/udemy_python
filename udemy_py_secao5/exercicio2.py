import math
num1 = float(input("Insira o numero: "))

if num1 > 0:
    raiz_quadrada = math.sqrt(num1)
    print(f"A raiz quadrada é {raiz_quadrada:.2f}.")
else:
    print("Número invalido!")
