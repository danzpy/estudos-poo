'''
Agregação é uma relação do tipo “tem um”, onde uma classe usa outra como parte de sua composição, 
mas sem ser dona exclusiva daquele objeto. A ideia é: os objetos podem existir separadamente.

O carrinho "tem" produtos, mas ele não cria os produtos, nem depende deles para existir.
Os objetos banana, pera e uva são criados fora do carrinho e só depois adicionados a ele.
Se o carrinho for destruído, os produtos continuam existindo, pois não pertencem exclusivamente ao carrinho.

Esse é o ponto chave da agregação: existência independente dos objetos.

'''

class Produto:
    def __init__(self, nome: str, valor: int)-> None:
        self.nome = nome
        self.__valor = valor

    def informacoes_do_produto(self) -> None:
        print(f'Produto: {self.nome} - Valor: {self.__valor}')


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Produto) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print('Compra finalizada!')
        print('     Produtos: ')
        for produto in self.__produtos:
            produto.informacoes_do_produto()

banana = Produto('banana', 3) # Produto existe sozinho
pera = Produto('pera', 2) # Produto existe sozinho
uva = Produto('uva', 4) # Produto existe sozinho

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produtos(banana) # Agregando ao carrinho
carrinho.adicionar_produtos(pera) # Agregando ao carrinho
carrinho.adicionar_produtos(uva) # Agregando ao carrinho

carrinho.finalizar_compra()