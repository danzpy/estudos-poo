class Motor:
    def ligar(self):
        print("Motor ligado.")

    def desligar(self):
        print("Motor desligado.")

class Carro:
    def __init__(self, modelo: str):
        self.modelo = modelo
        self.__motor = Motor()  # Composição: o motor é criado dentro do carro

    def ligar_carro(self):
        print(f"Ligando o carro modelo {self.modelo}")
        self.__motor.ligar()

    def desligar_carro(self):
        print(f"Desligando o carro modelo {self.modelo}")
        self.__motor.desligar()


meu_carro = Carro("Civic")
meu_carro.ligar_carro()
meu_carro.desligar_carro()
