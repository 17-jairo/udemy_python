'''
Any e All

All - Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio.
_______________________________________________________________________________________________________________________
# Exemplo all ()
print(all([0, 1, 2, 3, 4])) # Todos os numeros são verdadeiros? - False
print(all([1, 2, 3, 4])) # Todos os numeros são verdadeiros? - True
print(all([]))
_______________________________________________________________________________________________________________________
Iteravel com list comprehension

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 ==0]))
-----------------------------------------------------------------------------------------------------------------------
# Any - Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, 3, 4])) # True
'''


