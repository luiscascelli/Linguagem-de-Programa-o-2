# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Luis Antonio Matile Cascelli 1903598
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


class Escola:
    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    # Metodos
    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.__diretor = None
        self.__monitor = None

    # Metodos
    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Professor:
    # Atributos
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    # Metodos
    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno:
    # Atributos
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.__casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    # Metodos
    def set_casa(self, casa):
        self.__casa = casa

    def get_casa(self):
        return self.__casa

    def get_triunfo(self):
        return self.__triunfos

    def get_mau_feito(self):
        return self.__mau_feitos

    def incluir_triunfo(self, triunfo):
        self.__triunfos += triunfo

    def incluir_mau_feito(self, mau_feito):
        self.__mau_feitos += mau_feito


class Disciplina:
    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    # Metodos
    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)
