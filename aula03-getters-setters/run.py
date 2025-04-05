class MinhaClasse():

    def __init__(self) -> None:
        self.__valor = None # Foi definido um atributo privado.


    def setter(self, value) -> None: # Um setter é um metodo para definir esse atributo dentro da classe.
        self.__valor = value

    def getter(self) -> int: # Um getter é um atributo que retorna o que foi definido no setter, também dentro da classe.
        return self.__valor

classe = MinhaClasse()

classe.setter(2)
getter = classe.getter()

print(f'O valor atribuído foi {getter}')