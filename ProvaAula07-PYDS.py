#Dados ficticios de culturas em quatro fazendas entre 2020 e 2023

fazenda1 = [
        {2020: {"Milho": 12846, "Soja": 36092, "Trigo": 22403, "Algodão": 47153, "Feijão": 11188}},
        {2021: {"Milho": 33891, "Soja": 8786, "Trigo": 12273, "Algodão": 45435, "Feijão": 32289}},
        {2022: {"Milho": 1598, "Soja": 48785, "Trigo": 22689, "Algodão": 45142, "Feijão": 33401}},
        {2023: {"Milho": 1825, "Soja": 22329, "Trigo": 43301, "Algodão": 19261, "Feijão": 12627}},
]

fazenda2 = [
        {2020: {"Milho": 20348, "Soja": 10106, "Trigo": 46611, "Algodão": 4448, "Feijão": 16607}},
        {2021: {"Milho": 5414, "Soja": 9566, "Trigo": 34858, "Algodão": 5228, "Feijão": 12236}},
        {2022: {"Milho": 40767, "Soja": 27619, "Trigo": 30961, "Algodão": 27163, "Feijão": 13786}},
        {2023: {"Milho": 30056, "Soja": 47127, "Trigo": 36321, "Algodão": 30653, "Feijão": 9373}},
]

fazenda3 = [
        {2020: {"Milho": 34699, "Soja": 41775, "Trigo": 29984, "Algodão": 28834, "Feijão": 15883}},
        {2021: {"Milho": 29693, "Soja": 36135, "Trigo": 34338, "Algodão": 15092, "Feijão": 37048}},
        {2022: {"Milho": 3751, "Soja": 17635, "Trigo": 6094, "Algodão": 34046, "Feijão": 1297}},
        {2023: {"Milho": 32675, "Soja": 49552, "Trigo": 11304, "Algodão": 28325, "Feijão": 44482}},
]

fazenda4 = [
        {2020: {"Milho": 919, "Soja": 45375, "Trigo": 45519, "Algodão": 3349, "Feijão": 20256}},
        {2021: {"Milho": 15676, "Soja": 19643, "Trigo": 38592, "Algodão": 34233, "Feijão": 43215}},
        {2022: {"Milho": 47321, "Soja": 47927, "Trigo": 46169, "Algodão": 21657, "Feijão": 5696}},
        {2023: {"Milho": 38335, "Soja": 36366, "Trigo": 36612, "Algodão": 21177, "Feijão": 18212}},
]


#Atribuindo o nome das fazendas em um dicionário para organização e coleta do nome como string
fazendas = {
    "Fazenda_1": fazenda1,
    "Fazenda_2": fazenda2,
    "Fazenda_3": fazenda3,
    "Fazenda_4": fazenda4
}

#Retorna o resumo da produção das fazendas e o total
def resumo_producao_fazendas():
    print("\nAbaixo o resumo de produção de cada fazenda!")
    for nome, fazenda in fazendas.items():
        total = 0
        nome_fazenda = nome
        print(f"\n>> {nome_fazenda} <<")
        for dicionario in fazenda:
            for chave in dicionario.keys():
                ano_atual = chave
            for ano in dicionario.values():
                producao_anual = sum(list(ano.values()))
                print(f"A produção em {ano_atual} foi de.: {producao_anual} toneladas")
                total += producao_anual
        print(f"-->Valor Total (2020 a 2023).: {total} toneladas")        
        


#Retorna qual o ano que determinada fazenda teve produção máxima
def resumo_producacao_max():
    print("\nAbaixo o ano em que cada fazenda teve produção Máxima!")
    for nome, fazenda in fazendas.items():
        nome_fazenda = nome
        producao = {}
        lista_toneladas = [] 
        for dicionario in fazenda:
            for chave in dicionario.keys():
                ano_atual = chave
            for ano in dicionario.values():
                for valor in ano.values():
                    producao_anual = sum(list(ano.values()))
            lista_toneladas.append(producao_anual)
            producao[ano_atual] = producao_anual
            max_toneladas = max(lista_toneladas)
            for chave, valor in producao.items():
                if valor == max_toneladas:
                    ano_max = chave
        print(f"{nome_fazenda} -> Ano: {ano_max} -> Produção(ton): {max_toneladas}")


#Informa o ano em que a soma da produção de todas as fazendas juntas tiveram a maior produção.
def producao_maxima_ano():
    #Coleta os anos de produção das fazendas e transforma em um dicionário como chave.
    lista_anos = set()
    Anos_Producao = {}
    for fazenda in fazendas.values():
        for dicionario in fazenda:
            for ano in dicionario.keys():
                lista_anos.add(ano)
    for ano in lista_anos:
        Anos_Producao[ano] = 0
    #A cada ano/chave é inserido como valor correspondente a produção total do respectivo ano
    for fazenda in fazendas.values():
        for dicionario in fazenda:
            for ano, produtos in dicionario.items():
                producao_total = sum(produtos.values())
                Anos_Producao[ano]+=producao_total
    #Retorna o maior e menor ano de produção geral para o case 3 e 4
    valor_maximo = max(Anos_Producao.values())
    valor_minimo = min(Anos_Producao.values())
    for chave, valor in Anos_Producao.items():
        if valor == valor_maximo:
            ano_maximo = chave
        elif valor == valor_minimo:
            ano_minimo = chave
    return ano_maximo, valor_maximo, valor_minimo, ano_minimo
    
#Retorna a maior e menor produção de cultura geral acumulada
def maior_menor_producao_cultura():
    dicionario_cultura = {}
    lista_cultura = set()
    for fazenda in fazendas.values():
        for dicionario in fazenda:
            for produtos in dicionario.values():
                for cultura in produtos.keys():
                    lista_cultura.add(cultura)
    for cultura in lista_cultura:
        dicionario_cultura[cultura] = 0

    for fazenda in fazendas.values():
        for dicionario in fazenda:
            for ano, produtos in dicionario.items():
                for lista_cultura in produtos:
                    dicionario_cultura[lista_cultura] += produtos[lista_cultura]
    print("\n")
    for chave, valor in dicionario_cultura.items():
        if valor == max(dicionario_cultura.values()):
            produto_max = chave
            print(f"A cultura com MAIOR produção acumulada foi.: -{produto_max}- com {valor} Toneladas")
        elif valor == min(dicionario_cultura.values()):
            produto_min = chave
            print(f"A cultura com MENOR produção acumulada foi.: -{produto_min}- com {valor} Toneladas")


#Retorna em determinado ano, qual fazenda teve a maior e a menor produção
def fazenda_maior_menor_producao():
    anos = set()
    fazend_producao = {}
        

    for fazenda in fazendas.values():
        for dicionario in fazenda:
            for ano in dicionario.keys():
                anos.add(ano)

    opcao_ano = int(input(f"Escolha entre os seguinte anos.: {anos}.: "))

    if opcao_ano in anos:

        for nome_fazenda in fazendas.keys():
            fazend_producao[nome_fazenda] = 0

        for nome, fazenda in fazendas.items():
            for dicionario in fazenda:
                for ano, produtos in dicionario.items():
                    producao_ano = sum(produtos.values())
                    if ano == opcao_ano:
                        fazend_producao[nome] = producao_ano

        for dados_nome, valor in fazend_producao.items():
            if valor == max(fazend_producao.values()):
                nome_fazenda_max = dados_nome
                valor_fazenda_max = valor
            if valor == min(fazend_producao.values()):
                nome_fazenda_min = dados_nome
                valor_fazenda_min = valor                

        print(f"\nA fazenda com MAIOR produção em -{opcao_ano}- é a {nome_fazenda_max} com {valor_fazenda_max} Toneladas")
        print(f"A fazenda com MENOR produção em -{opcao_ano}- é a {nome_fazenda_min} com {valor_fazenda_min} Toneladas\n")

    else:
        print("Valor digitado não corresponde o ano válido!")



#Parte principal do programa.
while True:
    print("\n-->> Sistema Gestão Fazendas <<--")
    print("1 - Total Produção Fazendas")
    print("2 - Ano de Produção Máxima de cada fazenda")
    print("3 - Produção Máxima Geral(Ano)")
    print("4 - Produção Mímina Geral(Ano)")
    print("5 - Maior/Menor Produção Cultura Acumulada")
    print("6 - Fazenda com Maior/Menor produção por Ano")
    print("7 - Sair")
    opcao = input("Escolha uma opção do menu.: ")

    match opcao:
        case "1":
            resumo_producao_fazendas()
        case "2":
            resumo_producacao_max()
        case "3":
            ano_maximo, valor_maximo, valor_minimo, ano_minimo = producao_maxima_ano()
            print(f"\n-> O ano com MAIOR produção geral foi: {ano_maximo}, com um total de {valor_maximo} Toneladas.")
        case "4":
            ano_maximo, valor_maximo, valor_minimo, ano_minimo = producao_maxima_ano()
            print(f"\n-> O ano com MENOR produção geral foi: {ano_minimo}, com um total de {valor_minimo} Toneladas.")
        case "5":
            maior_menor_producao_cultura()
        case "6":
            fazenda_maior_menor_producao()
        case "7":
            print("\nFim do Programa. Até mais!")
            break
        case _:
            print("\nOpção Inválida. Tente novamente!")





