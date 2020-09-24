# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 7 Ex 2
"""


class Pedido():
    # Atributos
    def __init__(self):
        self.produtos = []

    # Metodos
    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        vt = 0
        for i in self.produtos:
            vt += (i.preco*i.qtd)
        return vt


class Produto():
    # Atributos
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())
