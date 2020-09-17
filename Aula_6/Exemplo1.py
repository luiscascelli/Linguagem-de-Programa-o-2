# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Exemplo 1

Classe Cachorro
Atributos: nome, idade
Metodos: andar, comer, latir
"""


class Cachorro:
    # atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # metodos
    def andar(self, distancia):
        print("O cachorro andou", distancia, "metros")

    def comer(self):
        print("O cachorro de nome", self.nome, "comeu")

    def latir(self):
        print("Au Au Au")


dog = Cachorro("Tobias", 25)

dog.andar(5)
dog.latir()
dog.comer()
