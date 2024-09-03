'''
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma 
estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.
'''

from functools import reduce
def maior_numero(*args):
    return reduce(lambda x,y: x if x>y else y, args)

lista_numeros=[100,600,400]

print(f'O maior número é.: {maior_numero(*lista_numeros)}')