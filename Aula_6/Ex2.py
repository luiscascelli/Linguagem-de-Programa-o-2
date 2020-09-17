# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 2

Classe Triangulo
Atributos: lado_a, lado_b, lado_c
Metodos: calcular_perimetro
"""


class Triangulo():
    # atributos
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    # metodo
    def calcular_perimetro(self):
        p = self.lado_a + self.lado_b + self.lado_c
        return p
