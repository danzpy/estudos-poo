"""
Variáveis de classe em Python são variáveis que são compartilhadas por todas
as instâncias de uma classe. Elas são definidas diretamente na classe e
não dentro de qualquer método. Isso significa que todas as instâncias da classe
têm acesso à mesma variável, e qualquer modificação feita na variável através 
de uma instância será refletida em todas as outras instâncias.
"""

class Carro:
    # Variável de classe
    numero_de_rodas = 4

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Acessando a variável de classe pela classe
print(Carro.numero_de_rodas)  # Saída: 4

# Criando instâncias da classe
carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

# Acessando a variável de classe pelas instâncias
print(carro1.numero_de_rodas)  # Saída: 4
print(carro2.numero_de_rodas)  # Saída: 4

# Modificando a variável de classe através da classe
Carro.numero_de_rodas = 6
print(carro1.numero_de_rodas)  # Saída: 6
print(carro2.numero_de_rodas)  # Saída: 6

# Modificando a variável de classe através de uma instância
carro1.numero_de_rodas = 8
print(carro1.numero_de_rodas)  # Saída: 8
print(carro2.numero_de_rodas)  # Saída: 6
print(Carro.numero_de_rodas)   # Saída: 6