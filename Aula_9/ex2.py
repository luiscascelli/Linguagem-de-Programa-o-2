# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de Programacao 2

Aula 9 - Heranca

Ex 2
"""


class Animal:
    # Atributos
    def __init__(self, nome, cor, numero_de_patas):
        self.nome = nome
        self.cor = cor
        self.numero_de_patas = numero_de_patas

    # Metodos
    def exibir_dados(self):
        print(self.nome)
        print(self.cor)
        print(self.numero_de_patas)


class Cachorro(Animal):
    # Atributos
    def __init__(self, nome, cor, numero_de_patas, raca):
        super().__init__(nome, cor, numero_de_patas)
        self.raca = raca

    # Metodos
    def exibir_dados(self):
        super().exibir_dados()
        print(self.raca)


animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()
