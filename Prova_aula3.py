# [LP-A04] Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

soma = 0
repeticao = 0

while True:
    numeros = int(input("Digite um número inteiro.: "))
    
    if numeros !=0:
        soma += numeros
        repeticao += 1
    elif numeros == 0 and repeticao == 0:
        print("\nVocê não pode iniciar digitado o número zero!")
    elif numeros == 0 and repeticao !=0:
        print("\nFim da coleta de números.")
        break
    
print(f"\nA quantidade de valores digitados foi.: {repeticao}")
print(f"A soma dos valores digitados é.: {soma}")
print(f"A média dos valores digitados é.: {(soma/repeticao)}\n")