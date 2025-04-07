'''
O polimorfismo ermite que diferentes classes implementem métodos com o mesmo nome,
mas com comportamentos diferentes.

Exemplo:
    Em um jogo, onde vários tipos de personagens têm o método atacar(), mas cada um ataca de forma diferente.
'''

class Personagem:
    def atacar(self):
        raise NotImplementedError("Subclasse precisa implementar este método!")

class Guerreiro(Personagem):
    def atacar(self):
        return "O Guerreiro ataca com espada!"

class Mago(Personagem):
    def atacar(self):
        return "O Mago lança uma bola de fogo!"

class Arqueiro(Personagem):
    def atacar(self):
        return "O Arqueiro dispara uma flecha!"

# Função polimórfica que aceita qualquer personagem
def iniciar_ataque(personagem):
    print(personagem.atacar())

# Criando os personagens
guerreiro = Guerreiro()
mago = Mago()
arqueiro = Arqueiro()

# Chamando a função polimórfica
iniciar_ataque(guerreiro)  # O Guerreiro ataca com espada!
iniciar_ataque(mago)       # O Mago lança uma bola de fogo!
iniciar_ataque(arqueiro)   # O Arqueiro dispara uma flecha!
