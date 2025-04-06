# Violando o principio, precisaria modificar a classe toda vez que uma nova forma de pagamento fosse adicionada à logica.
# Isso deixaria o código aberto para modificação.

class Pagamento:
    def processar_pagamento(self, metodo, valor):
        if metodo == 'cartao_credito':
            print(f"Processando pagamento de {valor} com cartão de crédito.")
        elif metodo == 'paypal':
            print(f"Processando pagamento de {valor} com PayPal.")
        else:
            print(f"Processando pagamento de {valor} com Boleto.")


cartao = Pagamento()

cartao.processar_pagamento('cartao_credito', 200)