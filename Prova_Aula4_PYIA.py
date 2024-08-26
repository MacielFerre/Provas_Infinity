'''
[PYIA-A04] Crie uma função chamada media que receberá três números como argumentos. 
Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, em seguida, 
divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.

'''


def media_aritmetica(n1,n2,n3):
    return round((n1+n2+n3)/3,2)

lista_numero=[]
print("Cálculo da Média Arimética")
for i in range(1,4):
    lista_numero.append(float(input(f"Digite o {i}º número.: "))) 

print(f"\nO valor da média é.: {media_aritmetica(lista_numero[0],lista_numero[1],lista_numero[2])}")