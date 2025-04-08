'''
Uma interface é como um contrato que define um conjunto de métodos que uma classe deve implementar,
mas sem fornecer a implementação desses métodos. Ela não tem lógica, só a estrutura. Ou seja,
não precisa de métodos ou lógica, como uma classe abstrata pode ter. 

Diferente de uma classe abstrata, uma interface não implementa nada, ela só diz:

“Se você quiser usar isso aqui, vai ter que me obedecer.”

Interface = promessa de que certos métodos existem, mas cada classe define o que esses métodos fazem.
'''

from abc import ABC, abstractmethod

class MeioDePagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class CartaoCredito(MeioDePagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} no crédito.")

class Boleto(MeioDePagamento):
    def pagar(self, valor):
        print(f"Gerando boleto de R${valor:.2f}.")


obj1 = CartaoCredito()

obj1.pagar(valor=12)
