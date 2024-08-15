#[PYIA-A02] Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

contato = {}
nome = input("Digite o nome do contato.: ")
telefone = input("Digite o número de telefone.: ")
email = input("Digite o e-mail do contato.: ")

contato["Nome"]=nome
contato["Telefone"]=telefone
contato["E-mail"]=email

print('')
for chave, valor in contato.items():
    print(f'{chave} -> {valor}')