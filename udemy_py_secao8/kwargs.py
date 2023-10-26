'''
**kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que
utilizemos parametros nomeados, e trnasforma esses parametros extras em um dicionario.
_____________________________________________________________________________________________________________________
# Exemplo 1

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa= 'branco')
-----------------------------------------------------------------------------------------------------------------------
# Exemplo 2

def comprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == "Python":
        return 'Você recebeu um cumprimento Pythonico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(comprimento_especial())
print(comprimento_especial(geek='Python'))
print(comprimento_especial(geek='Oi'))
print((comprimento_especial(geek='especial')))
-----------------------------------------------------------------------------------------------------------------------
# Nas nossas funções podemos ter (NESTA ORDEM):

- Parametros obrigatórios;
- *args
- Parametros default(não obrigatorios)
- **kwargs
-----------------------------------------------------------------------------------------------------------------------

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Casado')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)
----------------------------------------------------------------------------------------------------------------------
# Entenda por que é importante manter a ordem dos parametros na declaração

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome= 'University', cargo= 'Instrutor'))


Output:
[1, = obrigatorio
 2, = obrigatorio
  (3,) = *args
  , 'Geek' = default
  , {'sobrenome': 'University', 'cargo': 'Instrutor'}] = kwargs
----------------------------------------------------------------------------------------------------------------------
# Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
-----------------------------------------------------------------------------------------------------------------------
# OBS! Os nomes da chave em um dicionario devem ser os mesmos dos parametros da função
'''





