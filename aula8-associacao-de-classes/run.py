class Interruptor:

    status = False

    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def __imprime_estado(self, estado):
        self.estado = estado
        print(self.estado)

    def acender(self) -> None:
        if self.status:
            self.__imprime_estado(f'A luz do {self.comodo} já está acesa.')
        else:
            self.status = True
            self.__imprime_estado(f'A luz do {self.comodo} foi acesa.')

    def apagar(self) -> None:
        if not self.status:
            self.__imprime_estado(f'A luz do {self.comodo} já está apagada.')
        else:
            self.status = False
            self.__imprime_estado(f'A luz do {self.comodo} foi apagada.')


class Pessoa:

    def __init__(self, nome: str) -> None:
        self.nome = nome

    def acender_luzes(self, interruptor: Interruptor) -> None:
        interruptor.acender()
    
    def apagar_luzes(self, interruptor: Interruptor) -> None:
        interruptor.apagar()
    
pessoa1 = Pessoa('Daniel')
interruptor1 = Interruptor('Quarto')

pessoa1.acender_luzes(interruptor1)
pessoa1.apagar_luzes(interruptor1)
pessoa1.acender_luzes(interruptor1)
pessoa1.acender_luzes(interruptor1)