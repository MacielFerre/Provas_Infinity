def menu_calculadora():
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Resultado/Sair")

def coletor_numeros():
    valor_numerico = float(input("\nDigite outro número.: "))
    return valor_numerico

def somar(total, numero):
    return total + numero
    
def subtracao(total, numero):
    return total - numero
    
def multiplicao(total, numero):
    return total * numero

def divisao(total, numero):
    return total / numero

print("--||--Calculadora--||--")
valor_n1 = float(input("\nDigite um número.: "))
total = 0
total += valor_n1

while True:
    menu_calculadora()    
    operador = int(input("Digite uma operação acima.: "))

    match operador:
        case 1:
            total = somar(total, coletor_numeros())
            print(f"Total: {total}")

        case 2:
            total = subtracao(total, coletor_numeros())
            print(f"Total: {total}")    

        case 3:
            total = multiplicao(total, coletor_numeros())
            print(f"Total: {total}")
    
        case 4:
            valor_n2 = coletor_numeros()
            if valor_n2 != 0:
                total = divisao(total, valor_n2)
                print(f"Total: {total}")
            else:
                print("Este número (divisor) não pode ser zero!")
                continue
        case 5:
            print(f"\nResultado Final: {total}")
            print(f"Até mais!\n")
            break