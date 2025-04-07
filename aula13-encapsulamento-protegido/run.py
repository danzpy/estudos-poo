'''
É uma convenção usada para indicar que um atributo ou método não deve ser acessado
diretamente fora da classe ou de suas subclasses, mas ainda pode ser acessado
(ou seja, não é completamente privado).
'''

class Felino:
    def __init__(self, nome: str) -> None:
        self.nome = nome 

    def miar(self) -> None:
        print(f'{self.nome} está miando..')

    def rugir(self) -> None:
        print(f'{self.nome} está rugindo..')

    def __dormir(self) -> None:
        print('O animal está dormindo...')

    def _comer(self) -> None: # Um underscore representa o encapsulamento protegido.
        print('O animal está comendo..')

class Gato(Felino):
    def __init__(self, nome: str, cor) -> None:
        super().__init__(nome)
        self.cor = cor

    def descansar(self) -> None:
        self.__dormir()

    def alimentar(self) -> None:
        self._comer()


maria = Gato('Maria', 'cinza')

# Não é possível acessar um método privado (dunderscore) da classe mãe.

# maria.descansar() <---- Output: Erro
# maria.__dormir()  <---- Output: Erro

# Uma boa prática seria utilizar o encapsulamento protegido. Isso é tratado apenas como convenção pois não geram erros.

maria._comer() # <---- Isso (acessar o método protegido da classe superior) em outras linguagens não seria possível.

maria.alimentar()




