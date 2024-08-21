# [PYIA-A03] Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
# Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o 
# valor total da compra.


lista_de_produtos = {}
contador = 1
soma = 0

print("\nSeja bem vindo ao cadastro de compras!")
while contador<=5:
    produto = input(f"\nDigite o nome do {contador}º produto.: ")
    preco = float(input(f"Digite o preço do {contador}º produto.: R$ "))
    lista_de_produtos[produto]=preco
    contador +=1

for valor in lista_de_produtos.values():
    soma += valor

print(f'\nO valor total da compra.: R$ {soma}')

    