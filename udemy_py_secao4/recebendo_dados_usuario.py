"""
Recebendo dados do usuario
Todo dado recebido do tipo input é uma string
Em python, string é tudo que estiver entre aspas simples duplas duplas simples, simples triplas e duplas triples

"""
#Entrada de dados
print("Qual seu nome? ")
nome = input()
#Exemplo de print antigo python 2
#print("Seja bem vindo (a) %s" % nome)
#print ('Seja bem vindo {0}'. format(nome))
print(f'Seja bem-vindo(a) {nome}')
print("Qual sua idade? ")
idade = input()

#Processamento

#Saída de dados
#Exemplo de print antigo python 2x
#print('A %s tem %s anos' % (nome,  idade))
#print ('A {0} tem {1} anos' .format (nome, idade))
print(f'A {nome} tem {idade} anos')

#Cast é a conversão de im tipo de dado para outro
print(f'A {nome} nasceu em {2018 - int(idade)}')