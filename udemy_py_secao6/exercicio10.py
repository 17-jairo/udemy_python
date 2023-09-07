NP: int = 2
pares = []
while NP <= 50:
    if NP % 2 == 0:
        pares.append(NP)
    NP += 1
soma = sum(pares)
print(list(pares))
print(f"A soma doa pares será {soma}")

'''
O código fornecido estava proximo ao desejado, mas possuia um pequeno problema.
O loop while não permitia que o valor de NP fosse incrementado dentro do loop, 
resultando em um loop infinito.
Para corrigir isso moveu-se a linha NP += 1 para dentro do bloco if. 
'''