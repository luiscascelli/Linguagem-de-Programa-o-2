# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 6

Classe Carro
Atributos: qtd_combustivel
Metodos: adicionar_combustivel(litros), obter_combustivel(), andar(distancia)
"""


class Carro():
    # atributos
    def __init__(self):
        self.qtd_combustivel = 0

    # metodos
    def adicionar_combustivel(self, litros):
        self.qtd_combustivel += litros

    def obter_combustivel(self):
        return self.qtd_combustivel

    def andar(self, distancia):
        consumo = distancia*0.2
        self.qtd_combustivel -= consumo


meu_carro = Carro()
meu_carro.adicionar_combustivel(20)
meu_carro.andar(80)
print(f'Litros de combustível no tanque: {meu_carro.obter_combustivel()}')
