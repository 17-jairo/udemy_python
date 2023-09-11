N = int(input("Digite um número inteiro e positivo: "))
soma = 1
fatorial = 1
contador = 1

while contador <= N:
    fatorial *= contador
    soma += 1 / fatorial
    contador += 1

print(f"O valor de E para N = {N} é aproximadamente {soma:.2f}")

# Calculo usando o For

N = int(input("Digite um número inteiro e positivo: "))
soma = 1
fatorial = 1

for i in range(1, N + 1):
    fatorial *= i
    soma += 1 / fatorial

print(f"O valor de E para N = {N} é aproximadamente {soma:.2f}")
