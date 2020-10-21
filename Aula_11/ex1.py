# -*- coding: utf-8 -*-
"""
Linguagem de Programacao II

Aula 11 - Polimorfismo e Classes Abstratas

Ex 1
"""

from abc import ABC, abstractmethod

class Operacao(ABC):
    # Metodo Abstrato
    @abstractmethod
    def calcular(self,x,y):
        pass


class Soma(Operacao):
    # Metodo
    def calcular(self, x, y):
        return x+y

class Subtracao(Operacao):
    # Metodo
    def calcular(self, x, y):
        return x-y

class Multiplicacao(Operacao):
    # Metodo
    def calcular(self, x, y):
        return x*y

class Divisao(Operacao):
    # Metodo
    def calcular(self, x, y):
        return x/y

# Programa Principal

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10,5))      # 15
print(sub.calcular(10,5))       # 5
print(div.calcular(10,5))       # 2.0
print(mult.calcular(10,5))      # 50
