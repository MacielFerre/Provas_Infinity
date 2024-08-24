lista_tarefas = []

#Espaço das funções

def criar_tarefa():
    parada = 'não'
    while True:
        tarefa = {}
        nome = input("\nDigite o nome da tarefa.: ")
        tarefa["nome"]= nome
        descricao = input("Digite a descrição.: ")
        tarefa["descricao"] = descricao
        prioridade = int(input("Digite o valor da prioridade, entre 1 e 10.: "))
        tarefa["prioridade"] = prioridade
        categoria = input("Digite a categoria.: ")
        tarefa["categoria"]=categoria
        tarefa["concluido"] = False
        lista_tarefas.append(tarefa)
        

        while True:
            continuar = input("Deseja cadastar mais alguma tarefa (s/n).: ")
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


def listar_tarefas(var_arg):
    if var_arg == 1:
        for dicionario in lista_tarefas:
            for chave,valor in dicionario.items():
                print(f'{chave} -> {valor}')
            print('\n')
    
    elif var_arg == 2:
        opcao_prioridade = int(input("\nDigite o número da prioridade.: ")) 
        if opcao_prioridade>=1 or opcao_prioridade<=10:
            for dicionario in lista_tarefas:
                if opcao_prioridade == dicionario['prioridade']:
                    print(f'\nLista Tarefas com prioridade.: {opcao_prioridade}')
                    print(dicionario['nome'])
        elif opcao_prioridade<=0 or opcao_prioridade>=11:
            print("Valor de Prioridade Incorreto!")      
        
    
def alterar_status():
    tarefa_alt = input("Qual tarefa você que alterar o status?.: ")
    for dicio in lista_tarefas:
        if dicio['nome']==tarefa_alt:
            dicio['concluido']= not dicio['concluido']
            
          
def alterar_nome():
    print("\nLista das tarefas:")
    for dicionario in lista_tarefas:
        print(f'Tarefa: {dicionario["nome"]}')
    nome_tarefa = input("Digite o nome da tarefa que deseja alterar.: ")
    
    qt_chaves = len(lista_tarefas)
    cont = -1
    
    for i in range(qt_chaves):
        if lista_tarefas[i]['nome'] == nome_tarefa:
            cont+=1
            novo_nome_tarefa = input("Digite o nome nome para a tarefa.: ")
            lista_tarefas[i]['nome'] = novo_nome_tarefa
    if cont<0:
        print("Tarefa não encontrada")    
        

def excluir_tarefa():
    print("\nLista das tarefas:")
    for dicionario in lista_tarefas:
        print(f'Tarefa: {dicionario["nome"]}')
    nome_tarefa_excluir = input("Digite o nome da tarefa que deseja excluir.: ")

    qt_chaves = len(lista_tarefas)
    cont = -1
        
    for x in range(qt_chaves):
        if lista_tarefas[x]['nome'] == nome_tarefa_excluir:
            cont+=1
            indice = x
    if cont>=0 and indice>=0:
        del lista_tarefas[indice]
    if cont<0:
        print("Tarefa não encontrada")


#Inicio do programa
               
while True:
    print("\nSeja bem vindo!")
    print("1 - Criar Tarefas")
    print("2 - Lista Tarefas")
    print("3 - Status da Tarefa")
    print("4 - Editar Tarefa")
    print("5 - Excluir Tarefa")
    print("6 - Sair")
    opcao = int(input("Escolha uma opção do menu.: "))

    match opcao:
        case 1:
            criar_tarefa()

        case 2:
            print("\n1 - Listar todas as tarefas")
            print("2 - Listar por prioridade")
            print("3 - Listar por categoria")
            opcao_2 = int(input("Escolha uma opção do menu.: "))
            listar_tarefas(opcao_2)
        
        case 3:
            alterar_status()

        case 4:
            alterar_nome()
        
        case 5:
            excluir_tarefa()

        case 6:
            print("\nAté mais!")
            break

    
       
    
            
