# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 8 Ex 4
"""


class CarroCorrida:
    # Atributos
    def __init__(self, numero, piloto, velocidade_maxima,
                 velocidade_atual=0, ligado=False):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = velocidade_atual
        self.__ligado = ligado

    # Metodos
    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__ligado:
            v = self.__velocidade_atual + velocidade
            if v >= self.__velocidade_maxima:
                self.__velocidade_atual = self.__velocidade_maxima
            else:
                self.__velocidade_atual = v

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def get_velocidade_maxima(self):
        return self.__velocidade_maxima


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.acelerar(80)
print(carro.get_velocidade_atual())
carro.acelerar(70)
print(carro.get_velocidade_atual())
carro.frear()
print(carro.get_velocidade_atual())
