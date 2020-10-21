# -*- coding: utf-8 -*-
"""
Linguagem de Programacao II

Aula 11 - Polimorfismo e Classes Abstratas

Ex 2
"""

class Animal:
    # Atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    # Atributos
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    # Metodos
    def emitir_som(self):
        print('Au au')

class Gato(Animal):
    # Atributos
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    # Metodos
    def emitir_som(self):
        print('Miau')

class Cavalo(Animal):
    # Atributos
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    # Metodos
    def emitir_som(self):
        print('Irrraaa')

class Veterinario:
    # Metodos
    def examinar(self, animal):
        animal.emitir_som()

dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro
vet.examinar(horse)       # exibe o som do cavalo
vet.examinar(cat)         # exibe o som do gato
