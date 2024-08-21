# Nesse caso, poderiam ser adicionados quantos métodos fossem necessários sem modificar a classe.

class Metodo:

    def __init__(self, metodo: str) -> None:
        self.metodo = metodo

    def apresentar_metodo(self):
        print(f'{self.metodo} selecionado.')

class Pagamento:

    def processar_pagamento(self, metodo: Metodo, valor: int) -> None:
        metodo.apresentar_metodo()
        print(f'Processando pagamento no valor de R${valor},00 reais.')



pagamento = Pagamento()
cartao = Metodo('Cartão')
dinheiro = Metodo('Dinheiro')

pagamento.processar_pagamento(cartao, 200)
pagamento.processar_pagamento(dinheiro, 35)