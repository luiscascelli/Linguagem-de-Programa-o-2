# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 8 Ex 2
"""


class Filme:
    # Atributos
    def __init__(self):
        self.__titulo = None
        self.__genero = None

    # Metodos
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero


filmes = []
for i in range(3):
    f = Filme()
    f.set_titulo(input('Titulo: '))
    f.set_genero(input('Genero: '))
    filmes.append(f)

for i in range(len(filmes)):
    print('Filme', i+1)
    print(filmes[i].get_titulo())
    print(filmes[i].get_genero())
