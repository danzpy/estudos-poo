class Interruptor:

    status = None

    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def verifica_status(self):
        if self.status:
            return True

    def imprime_status(self):
        if self.status:
            print(f'Luz do {self.comodo} foi acesa.')
        else:
            print(f'Luz do {self.comodo} foi apagada.')

    def acender(self) -> None:
        if self.verifica_status():
            print(f'A luz do {self.comodo} já está acesa.')
        else:
            self.status = True
            self.imprime_status()

    def apagar(self) -> None:
        if not self.verifica_status():
            self.imprime_status()
            print(f'A luz do {self.comodo} já está apagada.')
        else:
            self.status = False
            self.imprime_status()


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