resultados = (
    ("Equipe1", 10, 9.7, 6.5, 7.8),
    ("Equipe2", 8.9, 9.4, 7.5, 4.8),
    ("Equipe3", 5, 9.8, 8.5, 9.8),
    ("Equipe4", 8, 5.5, 8.5, 7.9),
    ("Equipe5", 9.1, 9.3, 6.8, 8.8)
)

medias = []
classificacao = []


for x in range(0,5):
    soma=0
    for i in range(1,5):
        soma = soma + resultados[x][i]
    medias.insert(x, round((soma/4),1))

lista_medias_decrescente = sorted(medias, reverse=True)

print(f'As médias das equipes são.: {medias}')
print(f'A lista médias em ordem decrescente.: {lista_medias_decrescente}')


for i in range(0,5):
    classificacao.insert(i, (resultados[i][0], medias[i]))    
print(f'A classificação geral é a seguinte.: {classificacao}')

classificacao_ordenada = sorted(classificacao,key=lambda x: x[1], reverse=True)

print("\nClassificação:")
for x, y in classificacao_ordenada:
    print(f'{x}: {y}')