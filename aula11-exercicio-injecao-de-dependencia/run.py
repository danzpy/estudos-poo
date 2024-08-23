class ConectorBancoDeDados:

    def __init__(self) -> None:
        self.connection = None

    def conectar(self) -> None:
        self.connection = True


class RepositorioDeBanco:

    def __init__(self, conexao: ConectorBancoDeDados) -> None:
        self.__conexao = conexao

    def busca_dados(self) -> dict:
        if self.__conexao.connection:
            return {'dado1': 2, 'dado2': 3, 'dado3': 1}
        return None
    
class RegraDeNegocio:

    def __init__(self, repo: RepositorioDeBanco) -> None:
        self.__repo = repo

    def calcular_resultados(self) -> None:
        dados = self.__repo.busca_dados()

        if not dados:
            print('Dados não encontrados.. Verifique sua conexão com o banco.')
        else:
            print(f'A soma dos dados é: {sum(dados.values())}')

conn = ConectorBancoDeDados()
repositorio = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repositorio)

conn.conectar()

print(repositorio.busca_dados())

regra.calcular_resultados()

