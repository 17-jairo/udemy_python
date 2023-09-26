'''

Módulos Collections - Deque

Podemos dizer que deque é uma lista (container) de alta performance

'''

# Importa
from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)

deq.appendleft('t')
print(deq)

# Removendo elementos

print(deq.pop())

print(deq)

print(deq.popleft())
print(deq)
