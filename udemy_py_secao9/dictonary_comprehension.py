numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

'----------------------------------------------------------------------------------------------------------------------'

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

'----------------------------------------------------------------------------------------------------------------------'

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
