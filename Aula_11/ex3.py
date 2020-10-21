# -*- coding: utf-8 -*-
"""
Linguagem de Programacao II

Aula 11 - Polimorfismo e Classes Abstratas

Ex 3
"""

from abc import ABC, abstractmethod


class Funcionario(ABC):
    # Atributos
    def __init__(self, nome, salario_base, matricula):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    # Metodo Abstrato
    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    # Atributos
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    # Metodos
    def calcular_salario(self):
        return 2*self.salario_base


class Assistente(Funcionario):
    # Atributos
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    # Metodos
    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    # Atributos
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    # Metodos
    def calcular_salario(self):
        return 1.1*self.salario_base


g = Gerente('Jose', 1000)
a = Assistente('Tony', 1000)
v = Vendedor('Ana', 1000)

li = [g, a, v]

for i in li:
    print(i.calcular_salario())
