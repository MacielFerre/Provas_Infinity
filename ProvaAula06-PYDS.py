acervo_biblioteca = []
livros_emprestados = []


def adicionar_livro():
    lista_livro = {}
    print("\n!!!Cadastro de Livros!!!")
    titulo = input("\nDigite o título do livro.: ")
    lista_livro['Título'] = titulo
    autor = input("Digite o nome do Autor.: ")
    lista_livro['Autor'] = autor
    quantidade_livros = int(input("Digite a quantidade de livros.: "))
    lista_livro['Quantidade'] = quantidade_livros
    acervo_biblioteca.append(lista_livro)
    print("\nLivro Cadastrado com Sucesso!!!")



def listar_disponiveis():
    print("\n!!!Lista dos Livros Disponíveis!!!\n")
    for livros in acervo_biblioteca:
        if livros['Quantidade'] >= 1:
            print(f"Livro.: {livros['Título']} || Autor(a).: {livros['Autor']} || Quantidade.: {livros['Quantidade']}")



def fazer_emprestimo():
    print("\n!!!Emprestimo de Livros!!!")
    livro_emprestimo = input("Digite o Título do livro.: ")

    titulos = []
    for livro in acervo_biblioteca:
        titulos.append(livro['Título'])
       
    if livro_emprestimo in titulos:
        for livro in acervo_biblioteca:
                if livro['Título'] == livro_emprestimo:
                    if livro['Quantidade']>=1:
                        usuario = input("Digite o nome do usuário: ")
                        livros_emp_usu = []
                        for titulo in livros_emprestados:
                            if titulo['Nome'] == usuario:
                                livros_emp_usu.append(titulo['Título'])
                        if livro_emprestimo not in livros_emp_usu:
                            dados_locacao = {}
                            dados_locacao['Nome'] = usuario
                            dados_locacao['Título'] = livro_emprestimo
                            livro['Quantidade'] -= 1
                            livros_emprestados.append(dados_locacao)
                            print("\nLivro Emprestado com Sucesso!!!")
                        else:
                            print("\nEsse usuário já possui esse livro emprestado")
                    else:
                        print("\nNão há livros disponíveis para esse título.")        
    else:
        print("\nNão há cadastro deste livro na biblioteca") 

    

        

def devolver_livro():
    print("\n!!!Devolução de Livros!!!")
    livro_devol = input("Digite o Título do livro.: ")

    titulos = []
    for livro in livros_emprestados:
        titulos.append(livro['Título'])


    if livro_devol in titulos:
        for livro in acervo_biblioteca:
            if livro['Título'] == livro_devol:
                livro['Quantidade'] += 1
        for livro in livros_emprestados:
            if livro['Título'] == livro_devol:
                indice = livros_emprestados.index(livro)
                del livros_emprestados[indice]         
        print("\nLivro Devolvido com Sucesso!!!")
    else:
        print("Não há registro de locação deste título")



def pesquisar_livro():
    print("\n!!!Pesquisa de Livros!!!")
    loc_livro = input("Digite o Título do livro.: ")

    titulos = []
    for livro in acervo_biblioteca:
        titulos.append(livro['Título'])

    if loc_livro in titulos:
        for livro in acervo_biblioteca:
            if loc_livro == livro['Título']:
                print(f"\nCom esse título: |{loc_livro}| há {livro['Quantidade']} livros disponíveis")
    else:
        print("\nNão há esse título na biblioteca")


def lista_emprestimo_usuario():
    print("\n!!!Lista de Emprestimo por Usuário!!!")
    nome_usuario = input("Digite o nome do usuário.: ")

    lista_nomes = []
    for nome in livros_emprestados:
        lista_nomes.append(nome['Nome'])

    if nome_usuario in lista_nomes:
        print(f"\n!!!Lista dos Livros Emprestados!!!")
        print(f"Usuário.: {nome_usuario}")
        for nome in livros_emprestados:
            if nome_usuario == nome['Nome']:
                print(f"Livro.: {nome['Título']}")
    else:
        print("\nNão há livros emprestados a este usuário")






print("\n-->> Sistema Biblioteca <<--")
while True:
    print("\n1 - Adicionar Novo Livro")
    print("2 - Listar Livros Disponíveis")
    print("3 - Fazer Empréstimo Livro")
    print("4 - Devolver Livro")
    print("5 - Pesquisar Livro")
    print("6 - Lista Livros Emprestados por Usuário")
    print("7 - Sair")
    opcao = int(input("Escolha uma opção do menu.: "))

    match opcao:
        case 1:
            adicionar_livro()
        case 2:
            listar_disponiveis()
        case 3:
            fazer_emprestimo()
        case 4:
            devolver_livro()
        case 5:
            pesquisar_livro()
        case 6:
            lista_emprestimo_usuario()
        case 7:
            print("Fim do Programa. Até mais!")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")