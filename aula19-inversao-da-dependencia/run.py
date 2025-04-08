'''
“Módulos de alto nível não devem depender de módulos de baixo nível.
Ambos devem depender de abstrações. Abstrações não devem depender de detalhes.
Detalhes devem depender de abstrações.”

Tradução:

## Regra 1 — A lógica principal não depende diretamente da implementação ##

A classe Principal (nível alto), que executa a lógica principal do programa,
não depende diretamente de Elemento ou Elemento2 (nível baixo).
Em vez disso, ela recebe no construtor um objeto do tipo ElementoInterface,
sem saber qual implementação concreta está por trás

## Regra 2 — Ambos dependem de uma abstração ##

Ambas devem depender de uma abstração (interface ou classe abstrata).
Tanto Principal quanto as classes Elemento e Elemento2 dependem da interface ElementoInterface,
que define o contrato comum com o método executar().

## Regra 3 — Os detalhes conhecem a abstração, não o contrário ##

As implementações concretas (Elemento e Elemento2) sabem que precisam implementar ElementoInterface,
mas a classe Principal não precisa conhecer os detalhes dessas implementações.
Isso significa que você pode criar novos “elementos” sem precisar alterar a Principal
'''

from elementos.interfaces.elemento_interface import ElementoInterface
from elementos.elemento import Elemento
from elementos.elemento2 import Elemento2

class Principal():
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem # <- Dependência na interface. Se eu apagar, excluir ou modificar a classe, não afetará o projeto.

    def run(self) -> None:
        self.__elem.executar()
        print('Estou finalizando na classe principal')


el = Elemento() # Posso alterar o elemento sem prejudicar o projeto pois a dependência está na interface
el2 = Elemento2() 

cl1 = Principal(el)
cl1.run()