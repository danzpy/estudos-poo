from .interfaces.elemento_interface import ElementoInterface

class Elemento2(ElementoInterface):
    def executar(self) -> None:
        print('Estou executando o Elemento Alternativo')