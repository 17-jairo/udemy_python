soma = 0

for num in range(1,11):
    num = int(input("Digite o numero: "))
    if num > 0:
        soma += num
        media = soma / 10
    else:
        print("Digite números positivos!")
print(f"A média é {media}")

'''
A resposta acima foi a mais próxima encontrada ao que solicita o enunciado. Ela conta com a variavel contador, que é res
ponsvel por verificar a quantidade de vezes que meu numero é somado!
soma = 0
contador = 0

for _ in range(1, 11):
    num = int(input("Digite o numero: "))
    
    if num > 0:
        soma += num
        contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos números positivos é {media:.2f}")
else:
    print("Nenhum número inteiro positivo foi inserido.")

'''