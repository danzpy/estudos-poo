class Pessoa():
    # Ao tentar acessar métodos ou atributos que se iniciam com "__" (dunder-score)
    # retornará um erro pois essas informações estarão privadas.

    # Esses métodos só poderão ser acessados por outros métodos dentro da própria classe, nunca diretamente.

    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def apresentar(self) -> None:
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")
        self.__coletar_documento()

    def __coletar_documento(self) -> None:
        print(f"Meu CPF é {self.__cpf}")

pessoa1 = Pessoa("Daniel", 27, "222.222.222-47")

pessoa1.apresentar() # Este método não retornará erro.
pessoa1.__coletar_documento() # Ao chamar o método __coletar_documento() diretamente, não será possível.

# OBS. Apesar de não ser possível imprimir as informações dessa forma,
# isso não significa que é impossível acessa-las diretamente. Essa é apenas uma maneira
# de evidenciar que aquele método deve ser tratado de uma forma diferente dos demais.