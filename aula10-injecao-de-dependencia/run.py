class Celular:

    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f'Enviando mensagem: {mensagem}')

    def abrir_emails(self) -> None:
        print('Abrindo e-mails..')

    def abrir_youtube(self) -> None:
        print('Abrindo Youtube..')


class Pessoa:

    def __init__(self, celular: Celular) -> None:
        self.__celular = celular
    
    def pedir_pizza(self, mensagem) -> None:
        self.__celular.enviar_mensagem(mensagem)

    def estudar(self) -> None:
        self.__celular.abrir_youtube()
        print('Estudando...')

celular1 = Celular('Nokia')
celular2 = Celular('Android')

Daniel = Pessoa(celular1)
Joao = Pessoa(celular2)

Daniel.pedir_pizza('Boa noite, quero uma marguerita.\n')
Joao.estudar()
