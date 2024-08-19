class Carro:

    # Variável de classe
    numero_de_rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def print_variavel_classe(self):
        print(self.numero_de_rodas)

    def alterar_variavel_classe(self, valor):
        self.numero_de_rodas = valor

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# O valor da variável de classe só será alterada para essa instância.
carro1.alterar_variavel_classe(3)
carro1.print_variavel_classe()

carro2.print_variavel_classe()

print(Carro.numero_de_rodas)