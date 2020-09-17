# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 4

Classe Funcionario
Atributos: nome, salario
Metodos: aumentar_salario(percentual)
"""


class Funcionario():
    # atributos
    def __init__(self):
        self.nome = None
        self.salario = 0

    # metodos
    def aumentar_salario(self, percentual):
        self.salario = self.salario*(1+(percentual/100))


n = input("Nome do funcionario:")
s = float(input("Salario:"))

funcionario = Funcionario()
funcionario.nome = n
funcionario.salario = s
a = float(input("Percentual de aumento:"))
funcionario.aumentar_salario(a)
print("O novo salario do", funcionario.nome, "eh:", funcionario.salario)
