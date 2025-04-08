'''
Segregação de interfaces significa que uma classe (filha) que utiliza de uma interface
deve utilizar todas os métodos abstratos da interface. Sem a manipulação para que isso
ocorra sem erros
'''


from abc import ABC, abstractmethod

class MeioDePagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

    @abstractmethod
    def troco(self, montante, valor):
        pass

class Dinheiro(MeioDePagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} no dinheiro.")

    def troco(self, montante, valor):
        print(f"{montante} - {valor}, o troco é de: {montante - valor}")

    
class CartaoCredito(MeioDePagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} no crédito.")

    def troco(self, montante, valor):
        raise Exception('Não há troco para essa modalidade') # Isso fere o princípio da segregação