# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de Programacao 2

Aula 9 - Heranca

Ex 2
"""


class Veiculo:
    # Atributos
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    # Metodos
    def exibir_dados(self):
        print(self.ano)
        print(self.preco)
        print(self.motor.cilindrada)
        print(self.motor.potencia)


class Motor:
    # Atributos
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


class Carro(Veiculo):
    # Atributos
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    # Metodos
    def exibir_dados(self):
        super().exibir_dados()
        print(self.cor)
        print(self.modelo)


class Caminhao(Veiculo):
    # Atributos
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    # Metodos
    def exibir_dados(self):
        super().exibir_dados()
        print(self.comprimento)


motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime todos os atributos do carro
caminhao.exibir_dados()        # imprime  todos os atributos do caminhão
