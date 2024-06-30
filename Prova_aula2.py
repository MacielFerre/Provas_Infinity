# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, 
# exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = float(input("Digite a velocidade do veículo (km/h).: "))

if velocidade>80:
    km_excedente = round(abs(80.0 - velocidade),2)
    valor_multa = km_excedente*20
    print(f"Você ultrapassou o limite de velocidade!")
    print(f"Você foi multado em R$ {valor_multa}.")
elif velocidade<=0:
    print("Valor informado incorreto.")
else:
    print(f"Você está dentro do limite de velocidade!")