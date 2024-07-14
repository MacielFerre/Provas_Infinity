# [LP-A03] Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar 
# de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


numero = int(input("Digite um número inteiro para criação da tabuada.: "))
print("______________________")
print(f"\nTabuada de {numero}")
print("______________________")

for i in range(1,11):
    print(f"{numero} X {i} = {numero*i}")

    
    
    
        