# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 1

Classe Livro
Atributos: titulo, autor, qtd_livros
"""


class Livro():
    # atributos
    def __init__(self, nome, autor, pag):
        self.nome = nome
        self.autor = autor
        self.pag = pag


livro1 = Livro("Idade da Razao", "Sartre", 300)
livro2 = Livro("O Estrangeiro", "Camus", 150)


print(livro1.autor)
print(livro2.nome)
