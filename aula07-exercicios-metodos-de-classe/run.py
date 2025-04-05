class Loja:

    taxa = 0.05

    def __init__(self, valor_produto: float) -> None:
        self.valor_produto = valor_produto

    def consultar_valor_do_produto(self) -> None:
        print(self.valor_produto * (1 + self.taxa))

    @classmethod
    def editar_taxa_do_produto(cls, valor: float) -> None:
        cls.taxa = valor

print('Loja 1')
loja1 = Loja(2.0)
loja1.consultar_valor_do_produto()

print('\nLoja 2')
loja2 = Loja(2.0)
loja2.editar_taxa_do_produto(0.1)
loja2.consultar_valor_do_produto()

print('\nLoja 1 - Após alteração')
loja1.consultar_valor_do_produto()