cadastro_geral = []

while True: 
    print("\nSistema de Cadastro de Alunos")
    print('1 - Cadastrar Aluno')
    print('2 - Excluir Aluno')
    print('3 - Visualização de Alunos')
    print('4 - Média de Notas')
    print('5 - Aluno com Melhor Média')
    print('6 - Sair')
    opcao = int(input('Digite uma das opões acima.: '))

    match opcao:
        case 1:
            dados_aluno={}
            nome_aluno = input("\nDigite o nome do aluno.: ")
            dados_aluno['Nome'] = nome_aluno
            idade_aluno = int(input("Digite a idade do aluno.: "))
            dados_aluno['Idade'] = idade_aluno
            nota_matematica = float(input("Digite a note de Matemática.: "))
            nota_ciencias = float(input("Digite a note de Ciências.: "))
            nota_historia = float(input("Digite a note de História.: "))
            notas = (nota_matematica, nota_ciencias, nota_historia)
            dados_aluno['Notas'] = notas
            cadastro_geral.append(dados_aluno)
            print("\n>>||Aluno Cadastrado com sucesso||<<")
            
        case 2:
            print("\nLista de Alunos para Exclusão:")
            for dicionario in cadastro_geral:
                print(dicionario['Nome'])
            aluno_excluir = input("Digite o nome do aluno.: ")
            for dicionario in cadastro_geral:
                if aluno_excluir in dicionario['Nome']:
                    indice = cadastro_geral.index(dicionario)
                    del cadastro_geral[indice]
                    print("\n>>||Aluno Excluído com sucesso||<<")
                
                  
        
        case 3:
            print('\nLista de Alunos:')
            for dicionario in cadastro_geral:
                    print('\nNome -> ', dicionario['Nome'])
                    print('Idade -> ', dicionario['Idade'])
                    print('Notas -> Matemática: ', dicionario['Notas'][0], ' // Ciências: ',dicionario['Notas'][1], ' // História: ', dicionario['Notas'][2])
                    media = (dicionario['Notas'][0]+dicionario['Notas'][1]+dicionario['Notas'][2])/3
                    print('Média -> ', round(media,2))

        case 4:
            print('\nMédias por Aluno:')
            for dicionario in cadastro_geral:
                print('\nNome-> ', dicionario['Nome'])
                media = (dicionario['Notas'][0]+dicionario['Notas'][1]+dicionario['Notas'][2])/3
                print('Média -> ', round(media,2))

        case 5:
            print('\nAluno com Melhor Média:')
            melhor_media = 0.0
            melhor_aluno = ''
            for dicionario in cadastro_geral:
                media = (dicionario['Notas'][0]+dicionario['Notas'][1]+dicionario['Notas'][2])/3
                if media > melhor_media:
                    melhor_media = media
                    melhor_aluno = dicionario['Nome']
            print(f'Nome -> {melhor_aluno} // Média -> {melhor_media}')

        case 6:
            print("\nFim do Programa! Até Mais.\n")
            break        