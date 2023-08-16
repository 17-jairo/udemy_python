'''
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas - > "uma string", '234', 'a', 'True', '42.3'
- Estiver entre aspas triplas simples -> #uma string''', '''234''', '''a''', '''True''', '''42.3'''

# Estiver entre aspas triplas - > """ uma string """, """ 234 """, """ a """, """ True """, """ 42.3 """

'''

nome = """Geek University"""
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina
Jolie'
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())
nome = 'GEEK UNIVERSITY'
print(nome.lower())
nome = 'Geek University'
print(nome.split()) - > Transforma em uma lista de string.
print(nome[0:4]) #String slice
print(nome[5:15]) #String slice
print(nome.split()[1])
print(nome[::-1]) # Inversão da String - pythonico
print(nome.replace('G', 'P')) # Substitui as letras
'''
nome = 'Geek University'




