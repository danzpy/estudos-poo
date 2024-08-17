# Primeiro princípio do SOLID - Single Responsability

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validacao(nome, idade):
            self.__registrar(nome, idade)
        else:
            print(self.__erro_cadastro(nome))

    def __erro_cadastro(self, nome: str) -> str:
        return f'Erro ao cadastrar usuário {nome}. Dados inválidos'

    def __validacao(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)

    def __registrar(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print(f'Usuário {nome} ({idade} anos) foi cadastrado.\n')



cadastro1 = SistemaCadastral()
cadastro2 = SistemaCadastral()

cadastro1.cadastrar('Daniel', 27)
cadastro2.cadastrar('João', '2')