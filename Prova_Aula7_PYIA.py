# [PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os resultados desses dois lançamentos e retornar o valor total.

import random

def lancar_dados():
    dado1 = [1,2,3,4,5,6]
    dado2 = [1,2,3,4,5,6]
    jogada_dado1 = random.choice(dado1)
    jogada_dado2 = random.choice(dado2)
    print("\nLançamento de Dados...")
    print(f"O 1º dado foi: {jogada_dado1}")
    print(f"O 2º dado foi: {jogada_dado2}")
    print(f"A soma dos dois valores é.: {jogada_dado1+jogada_dado2} ")


continuar = 's'
while True:
    if continuar == 's':
        lancar_dados()
        continuar = str.lower(input("Deseja fazer outro lançamento dos dados (s/n).: "))
    elif continuar == 'n':
        print("\nAté mais! Fim do Programa.\n")
        break
    else:
        print("\nVocê digitou opção incorreta!")
        continuar = str.lower(input("Deseja fazer outro lançamento dos dados (s/n).: "))
    
        

   

