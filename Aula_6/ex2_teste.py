# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 2 - Teste de import e classe

Classe Triangulo
Atributos: lado_a, lado_b, lado_c
Metodos: calcular_perimetro
"""

from Ex2 import Triangulo

a = int(input("Lado a:"))
b = int(input("Lado b:"))
c = int(input("Lado c:"))

triangulo = Triangulo(a,b,c)
print("Perimetro:",triangulo.calcular_perimetro())