class Pessoa():
    # Ao tentar acessar métodos ou atributos que se iniciam com "__" (dunder-score)
    # retornará um erro pois essas informações estarão privadas.

    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def apresentar(self) -> None:
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")
        self.__coletar_documento()

    def __coletar_documento(self) -> None:
        print(f"Meu CPF é {self.cpf}")

pessoa1 = Pessoa("Daniel", 27, "222.222.222-47")

pessoa1.apresentar()