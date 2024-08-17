# Primeiro princípio do SOLID - Single Responsability

# O código abaixo não está dentro do princípio pois existem diversas "tarefas" dentro de um único método.

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): # 1 - Validação
            print('Acessando o banco de dados...') # 2 - Acessando o banco
            print(f'Usuário {nome} ({idade} anos) foi cadastrado.') 
        else:
            print(f'Erro ao cadastrar usuário {nome}. Dados inválidos') # 3 - Tratamento de erros

cadastro1 = SistemaCadastral()
cadastro2 = SistemaCadastral()

cadastro1.cadastrar('Daniel', 27)
cadastro2.cadastrar('João', '2')