'''
Uma classe abstrata é como um molde ou esqueleto para outras classes.
Ela não pode ser instanciada diretamente (ou seja, você não cria objetos a partir dela)
e serve apenas como base para outras classes. Ela define métodos que as subclasses
são obrigadas a implementar, garantindo que todas tenham uma estrutura mínima comum.

Pensa numa classe abstrata como um contrato:

“Se você quiser herdar de mim, vai ter que implementar esses métodos.”
'''

from abc import ABC, abstractmethod

class Animal(ABC):

    def respirar(self):
        print("Respirando...")  # já tem lógica

    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self): # Obrigatóriamente preciso do método "fazer_som"
        print("Au au!")

class Gato(Animal):
    def fazer_som(self): # Obrigatóriamente preciso do método "fazer_som"
        print("Miau!")
    
# animal = Animal() <- Instanciar uma classe abstrata irá gerar um erro.

dog = Cachorro()
dog.fazer_som()