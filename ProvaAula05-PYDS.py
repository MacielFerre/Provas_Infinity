texto = """\nData Science é um campo interdisciplinar que combina estatística, programação e conhecimento de domínio 
para extrair insights de dados. Ele envolve etapas como coleta, limpeza, análise e visualização de informações. 
Técnicas de machine learning são frequentemente usadas para criar modelos preditivos. Ferramentas populares incluem Python, 
R e bibliotecas como Pandas e TensorFlow. Data Science é aplicado em diversas áreas, como saúde, finanças e marketing.\n"""


def processador_texto(texto, **kwargs):
    texto_trabalho = texto

    operador = {
        "contar_palavras" : lambda palavra: len(palavra.split()),
        "contar_letras": lambda letra: sum(1 for letra in texto_trabalho if letra.isalpha()),
        "inverter_texto": lambda texto: texto[::-1],
        "substituir_palavra": lambda texto, palav_antiga, palav_nova: texto.replace(palav_antiga,palav_nova)

    }
    

    for chave, valor in kwargs.items():
        if chave == "contar_palavras":
            numero_de_palavras = operador["contar_palavras"](texto_trabalho)
            return numero_de_palavras
        elif chave == "contar_letras":
            numero_letras = operador["contar_letras"](texto_trabalho)
            return numero_letras
        elif chave == "inverter_texto":
            texto_invertido = operador["inverter_texto"](texto_trabalho)
            return texto_invertido
        elif chave == "substituir_palavra":
            palav_antiga = valor.get("antiga")
            palav_nova = valor.get("nova")
            if palav_antiga and palav_nova:
                novo_texto = operador["substituir_palavra"](texto_trabalho, palav_antiga, palav_nova)
                return novo_texto
    


print("\n-->>Processador de Texto<<--")

while True:
   print("\n1 - Imprimir o Texto Original")
   print("2 - Contar Palavras")
   print("3 - Contar Letras")
   print("4 - Inverter o Texto")
   print("5 - Substituir Palavra")
   print("6 - sair")
   opcao = int(input("Escolha uma opção do menu.: "))

   match opcao:
        case 1:
           print("\nAbaixo está o novo original:")
           print(texto)
        case 2:
           print(f"\nHá nesse texto: {processador_texto(texto, contar_palavras = True)} palavras")
        case 3:
           print(f"\nHá nesse texto: {processador_texto(texto, contar_letras = True)} letras")
        case 4:
           print("\nAbaixo está o texto invertido:")
           print(processador_texto(texto, inverter_texto = True))
        case 5:
           antiga = input("Digite a palavra a ser substituída: ")
           nova = input("Digite a nova palavra.: ")
           print("\nAbaixo está o novo texto:")
           print(processador_texto(texto, substituir_palavra = {"antiga": antiga, "nova": nova}))
        case 6:
           print("\nFim do Programa. Até mais!")
           break