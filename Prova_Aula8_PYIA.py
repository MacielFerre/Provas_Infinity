'''
[PYIA-A08] Importe o módulo 'os' e utilize a função 'listdir' para listar todos os arquivos e diretórios no diretório atual. A função 'listdir' retornará uma lista com os nomes dos arquivos e diretórios presentes no diretório onde o script está sendo executado. Em seguida, exiba o conteúdo dessa lista.
'''


import os

def listardiretorios():
    listaDir = os.listdir()
    for i in listaDir:
        print(i)


print("\nItens do Diretório:")
listardiretorios()