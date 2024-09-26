"""
Ao utilizar Heranças, é possível atribuir uma classe (mãe) a uma outra classes e herdar suas características e
métodos (abertos).

Note que no exemplo abaixo, foi possível instanciar a classe "Gato" e utilizar os métodos e 
atributos da classe superior.
"""

class Felino:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def miar(self) -> None:
        print(f'{self.nome} está miando..')

    def rugir(self) -> None:
        print(f'{self.nome} está rugindo..')

class Gato(Felino):
    def __init__(self, nome: str, cor) -> None:
        super().__init__(nome)
        self.cor = cor

class Leao(Felino):
    def __init__(self, nome: str, cor) -> None:
        super().__init__(nome) # Refere-se ao construtor da classe superior (Felino)
        self.cor = cor

gato1 = Gato('Maria', 'cinza')
gato2 = Gato('João', 'branco')
leao1 = Leao('Jorge', 'amarelo')

gato1.miar()
leao1.rugir()

print(gato1.cor)