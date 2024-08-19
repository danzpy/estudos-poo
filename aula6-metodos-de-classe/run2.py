class Carro:

    # Variável de classe
    numero_de_rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def print_variavel_classe(self):
        print(self.numero_de_rodas)


    @classmethod # Utilizando esse decorador, o valor será atualizado para a classe e todas suas instâncias.
    def alterar_variavel_classe(cls, valor):
        cls.numero_de_rodas = valor

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(f'Variável de classe acessada pela classe (antes da alteração) ->')
print(Carro.numero_de_rodas)

print(f'\nVariável de classe acessada pela instância "carro2" (antes da alteração) ->')
carro2.print_variavel_classe()

# O valor da variável de classe só será alterada para essa instância.
carro1.alterar_variavel_classe(3)

print(f'\nVariável de classe acessada pela instância "carro1" (depois da alteração) ->')
carro1.print_variavel_classe()

print(f'\nVariável de classe acessada pela classe (depois da alteração) ->')
print(Carro.numero_de_rodas)