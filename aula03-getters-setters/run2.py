class MinhaClasse():

    def __init__(self) -> None:
        self.__valor = None


    def setter(self, value) -> None:
        self.__valor = value

    # Com a atribuição deste decorador, consigo apresentar o valor encapsulado
    # sem a necessidade de criar uma variável e invocar o método.
    
    @property
    def getter(self) -> int:
        return self.__valor

classe = MinhaClasse()

classe.setter(233)

print(f'O valor atribuído foi {classe.getter}')