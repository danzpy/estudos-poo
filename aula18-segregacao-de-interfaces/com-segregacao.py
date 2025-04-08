from abc import ABC, abstractmethod

class MeioDePagamentoDigital(ABC): # Primeira interface
    @abstractmethod
    def pagar(self, valor):
        pass

class MeioDePagamentoFisico(ABC): # Segunda interface
    @abstractmethod
    def pagar(self, valor):
        pass

    @abstractmethod
    def troco(self, montante, valor):
        pass

class Dinheiro(MeioDePagamentoFisico):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} no dinheiro.")

    def troco(self, montante, valor):
        print(f"R${montante},00 - R${valor},00 no dinheiro, o troco é de: R${montante - valor},00")

    
class CartaoCredito(MeioDePagamentoDigital):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} no crédito.")

obj1 = CartaoCredito()
obj2 = Dinheiro()

obj1.pagar(10)
obj2.pagar(10)
obj2.troco(15,10)