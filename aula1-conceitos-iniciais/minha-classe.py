class MinhaClasse:

    # metodo construtor, onde são salvos os atributos da classe. Esse método é o primeiro a
    # ser executado ao instanciar um objeto da classe.
    def __init__(self, info):
        self.atributo1 = 'Este é meu primeiro atributo'
        self.atributo2 = 'Este é o segundo atributo'
        self.atributo3 = 2 + info

    def metodo_1(self):
        print("Essa é a ação 1.")

#objeto      #instanciando o objeto com uma classe
instancia1 = MinhaClasse(3)
atributo1 = instancia1.atributo1
atributo2 = instancia1.atributo2
atributo3 = instancia1.atributo3

instancia1.metodo_1()
print(atributo1)
print(atributo2)
print(atributo3)