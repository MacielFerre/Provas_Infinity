'''
[PYDS-A01] Gerenciamento de Compras de Produtos.
Você foi contratado para desenvolver um programa que auxiliará no processo de compra de produtos em uma loja. O programa deve permitir que o usuário 
insira o nome e o preço de diversos produtos, e após a inserção de cada produto, deve perguntar se o usuário deseja adicionar mais produtos à lista. 
O processo de inserção de produtos continuará até que o usuário opte por parar.
Ao término das inserções, o programa deve fornecer um resumo da compra com as seguintes informações:
A) Total gasto na compra: O programa deve calcular e exibir a soma de todos os preços dos produtos inseridos.
B) Quantidade de produtos que custam mais de R$1000: O programa deve contar e exibir quantos dos produtos cadastrados têm preço superior a R$1000.
C) Nome do produto mais barato: O programa deve identificar e exibir o nome do produto com o menor preço.
'''

lista_compra = []
soma_total = 0

while True:
    print('\n||Gerenciamento de Compras||')
    print("1 - Adicionar itens")
    print("2 - Total de Gastos")
    print("3 - Quantidade de produtos acima de R$ 1.000,00")
    print("4 - Produto mais barato")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção do menu.: "))

    match opcao:
        case 1:
            parada = 'não'
            while True:
                produto = {}
                nome = input("\nDigite o nome do produto.: ")
                produto["nome"]= nome
                preco = float(input("Digite o valor do produto.: R$ "))
                produto['preço'] = preco
                quantidade = float(input("Digite a quantidade do produto.: "))
                produto['quantidade'] = quantidade
                preco_id = preco * quantidade
                soma_total += preco_id
                lista_compra.append(produto)

                while True:
                    continuar = input("Deseja cadastar mais algum produto (s/n).: ")
                    if continuar == 's' or continuar == 'S':
                        break
                    elif continuar == 'n' or continuar == 'N':
                        parada = 'stop'
                        break
                    else:
                        print("Opção Invalida!")
                        continue
                if parada == 'stop':
                    break
        
        case 2:
            print(f"\nO valor total é.: R$ {soma_total}")

        case 3:
            cont = 0
            for dicionario in lista_compra:
                if dicionario['preço'] > 1000.00:
                    cont +=1
            print(f"\nHá {cont} produtos acima de R$ 1.000,00")

        case 4:
            nome_produto = ''
            valor_produto = soma_total
            for dicionario in lista_compra:
                if dicionario['preço'] < valor_produto:
                    nome_produto = dicionario['nome']
                    valor_produto = dicionario['preço']
            print(f'\nO produto mais barato é: {nome_produto}, que custa {valor_produto}')

        case 5:
            print("\nAté mais!")
            break
                





