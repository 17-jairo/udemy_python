#Resposta usando While
N = int(input("Insira um numero inteiro positivo: "))
soma = 0
if N <= 0:
    print("Favor inserir numero inteiros positivos")
else:
    inteiros =[]
    numero = 1
    while len(inteiros) < N:
        inteiros.append(numero)
        soma += numero
        numero += 1

print(f"Os {N} primeiros números naturais são: {inteiros} e a soma deles é {soma}")

#Resposta usando For

N = int(input("Insira um numero inteiro positivo: "))
soma = 0
for num in range(1, N + 1):
    print(num)
    soma += num

print(f'A soma de {N} numeros é {soma}')
