num1 = float(input("Insert the first number: "))
num2 = float(input("Insert the second number: "))
num3 = float(input("Insert the third number: "))
numeros = [num1, num2, num3]
numeros.sort()
print(f" a ordem dos numeros crescentes é {tuple(numeros)}")

'''
Exercicio exigiu do uso de listas, sendo que não estudamos esse assunto. Foi usada a função sort, que não tivemos em
aula e a função tupla, que também não tivemos em aula.
abaixo resolução chatgpt:

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numeros = [num1, num2, num3]
numeros.sort()  # Ordenando a lista diretamente

ordem_crescente = tuple(numeros)  # Convertendo de volta para uma tupla

print(f"A ordem dos números crescentes é {ordem_crescente}")

'''



