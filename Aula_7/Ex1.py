# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 7 Ex 1
"""


class Pessoa():
    # Atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self. idade = idade
        self.carro = None

    # Metodos
    def comprar_carro(self, carro):
        self.carro = carro


class Carro():
    # Atributos
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)
print('Modelo do meu carro: ', eu.carro.modelo)
print('Placa do meu carro: ', eu.carro.placa)
