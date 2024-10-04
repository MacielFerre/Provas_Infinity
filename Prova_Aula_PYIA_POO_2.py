'''
[PYIA-A12]  Crie uma classe base chamada Veiculo que tenha um método chamado movimentar. 
Este método deve imprimir a mensagem "Veículo está em movimento." para indicar que qualquer veículo está em movimento. 
Em seguida, crie duas subclasses chamadas Carro e Moto que herdem de Veiculo. Dentro de cada uma dessas subclasses, sobrescreva o método 
movimentar para imprimir mensagens específicas para cada tipo de veículo. Na classe Carro, o método movimentar deve imprimir "Carro está dirigindo.", 
enquanto na classe Moto, o método deve imprimir "Moto está acelerando."
'''

class Veiculo:
    def movimentar(self):
        return "Veiculo está em movimento"
        

class Carro(Veiculo):
    def movimentar(self):
        return 'Carro está dirigindo'
    
class Moto(Veiculo):
    def movimentar(self):
        return 'Moto está acelerando'
    

automovel_geral = Veiculo()
auto_4_rodas = Carro()
auto_2_rodas = Moto()

print(automovel_geral.movimentar())
print(auto_4_rodas.movimentar())
print(auto_2_rodas.movimentar())