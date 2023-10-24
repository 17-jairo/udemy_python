'''
Funções com parametro de entrada

- Funções que recebem dados para serem processados dentro da mesm;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada:
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Possuem entrada e saída.

# Refatorando uma função

def quadrado_de_7():
    return 7 * 7
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())

def quadrado(numero):
    return numero * numero
print(quadrado(2))
print(quadrado(7))
print(quadrado(3))

# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')

cantar_parabens("Arthur")

# Funções podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parametros forem necessarios. Eles são separados por virgula.

# Exemplo:

def soma(a, b):
    return a + b
def multiplica(num1, num2):
    return num1 * num2
def outa(num1, b, msg):
    return (num1 + b) * msg

print(soma(2,3))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outa(3, 2, "Geek "))
print(outa(5, 4, 'Python '))

# Obs: Se a gente informar um número errado de parametro ou argumentos, teremos um TypeError

# Nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo("Angelina", "Jolie"))

# A diferença entre Parametros e Argumentos

# Parametros são variáveis declaradas na definição de uma pessoa;
# Argumentos são dados passados durante a execução de uma fução;

# A ordem dos parametros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))
'''


