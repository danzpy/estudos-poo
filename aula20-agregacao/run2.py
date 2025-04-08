class Professor:
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar(self):
        print(f"Professor: {self.nome}")


class Curso:
    def __init__(self, nome: str):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)

    def exibir_professores(self):
        print(f"Professores do curso {self.nome}:")
        for prof in self.professores:
            prof.apresentar()


prof1 = Professor("Carlos")
prof2 = Professor("Marina")

curso = Curso("Psicologia")
curso.adicionar_professor(prof1)
curso.adicionar_professor(prof2)

curso.exibir_professores()
