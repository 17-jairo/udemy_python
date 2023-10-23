'''
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saida de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentre dela
é bom fazer uma verificação para que a função seja simplificada.

'''

# Exemplo de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

#Utilizando a função built-in do Python print ()

# print(cores)

# curso = "Programação em python: essencial"
# print(curso)

'''
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> SEMPRE, com letras minusculas e se for nome composto, separado por underline;
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.
'''

# Definindo a primeira funçao

def diz_oi():
    print('oi!')

'''
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi
3 - Veja que esta função não recebe nenhum parametro de entrada
4 - Veja que esta função não retorna nada.
'''

# Utilizando funções
diz_oi()

def cantar_parabens():
    print('Parabens pra voce')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')

cantar_parabens()

