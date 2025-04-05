class MinhaClasse():

    def __init__(self) -> None:
        self.__valor = None


    def setter(self, value) -> None:
        self.__valor = value

    def getter(self) -> int:
        return self.__valor

classe = MinhaClasse()

classe.setter(2)
getter = classe.getter()

print(f'O valor atribuído foi {getter}')