# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:17:49 2020

@author: Luis Antonio

Linguagem de Programacao II

Aula 10 - Herança

Ex 1
"""


class Pessoa:
    # Atributos
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    # Atributos
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    # Metodos
    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Funcionario(Pessoa):
    # Atributos
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Disciplina:
    # Atributos
    def __init__(self, nome):
        self.nome = nome


class Professor(Funcionario):
    # Atributos
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.disciplina = []

    # Metodos
    def incluir_disciplina(self, disciplina):
        self.disciplina.append(disciplina)


class Tecnico(Funcionario):
    # Atributos
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo


disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456",
                       "(11)99999-9555", "9999999", 2000, "Mestrado")

aluno1 = Aluno("Maria", "Avenida São Francisco, 239",
               "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77",
                   "(11)93333-3333", "8787887", 1500, "Tecnico")

aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)

for i in aluno1.disciplina:
    print(i.nome)
