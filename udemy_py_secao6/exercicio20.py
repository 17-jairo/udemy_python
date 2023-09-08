# Inserindo contadores:
numeros_lidos = 0
numeros_pares = 0

# Colocando a condicional:

while True:
    numero = int(input("Insert a number between 0 and 1000: "))
    if numero == 1000:
        break
    numeros_lidos += 1
    if numero % 2 == 0:
        numeros_pares += 1
print(f"Número de dados lidos: {numeros_lidos}")
print(f"Número de valores pares: {numeros_pares}")