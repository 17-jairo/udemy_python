x = float(input("Insira o numero X: "))
y = float(input("Insita o número Y: "))

# calculando os quadrados das coordenadas
distancia_quadrada = x**2 + y**2

# calculando a raiz da soma dos quadrados
distancia = distancia_quadrada ** 0.5

# Imprimindo o resultado

print(f'A distancia das origens {x}, e {y}, é {distancia:.2f}')
