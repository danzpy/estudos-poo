'''
Composição é uma relação do tipo “é feito de” ou “possui com controle total”.
Na composição, uma classe cria e gerencia internamente os objetos de outras classes — 
e esses objetos não existem fora dela.

Aqui, a classe Repositorio é composta por dois objetos:

 - Select
 - Insert

Mas atenção: esses objetos são criados DENTRO da classe Repositorio. Ou seja:
Eles só existem dentro do repositório.
Eles não são passados de fora, como seria numa agregação.
Se o Repositorio for destruído, Select e Insert morrem junto.


A classe Repositorio compõe os objetos Select e Insert porque ela instancia esses objetos dentro de si
e controla totalmente seu ciclo de vida. Esse é o coração da composição: uma classe complexa que é formada
por partes internas, que ela mesma gerencia.
'''

class Select:
    def by_id(self, id) -> any:
        print(f'Selecionando o elemento {id} no banco de dados')

class Insert:
    def insert_value(self, valor: any) -> None:
        print(f'Inserindo o valor: "{valor}" no banco de dados')


class Repositorio:
    def __init__(self) -> None:
        self.__select = Select() # composição
        self.__insert = Insert() # composição

    def select_by_id(self, id: int) -> any:
        self.__select.by_id(id)

    def insert(self, valor) -> None:
        self.__insert.insert_value(valor)

repo = Repositorio()

repo.select_by_id(3)
repo.insert('Porta')