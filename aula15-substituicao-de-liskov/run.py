'''
O principrio da substituição de Liskov diz que os objetos podem ser substituídos por seus
subtipos (classes herdeiras) sem que isso afete a execução correta do programa.

Ou seja, herdar de uma classe não é só copiar código: a subclasse precisa manter o contrato da classe mãe.
'''

class Ave:
    def voar(self):
        print("Voando alto!")

class Pinguim(Ave):
    def voar(self):
        raise Exception("Pinguins não voam!")
    
'''
Aqui, Pinguim é uma subclasse de Ave, mas não cumpre o que se espera de uma ave: voar.
Se um código espera uma Ave e tenta chamar voar(), o Pinguim quebra tudo — violando o princípio de Liskov.
'''

class Ave:
    pass

class AveQueVoa(Ave):
    def voar(self):
        print("Voando!")

class Canario(AveQueVoa):
    pass

class Pinguim(Ave):
    def nadar(self):
        print("Nadando!")

canario = Canario()
pinguim = Pinguim()

canario.voar()
pinguim.nadar()