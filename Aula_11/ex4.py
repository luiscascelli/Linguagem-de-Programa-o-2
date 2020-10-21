# -*- coding: utf-8 -*-
"""
Linguagem de Programacao II

Aula 11 - Polimorfismo e Classes Abstratas

Ex 4
"""


from abc import ABC


class Conta(ABC):
    # Atributos
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    # Metodos
    def exibir_saldo(self):
        print(self.__saldo)

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if (self.saldo - valor) < 0:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor


class Comum(Conta):
    pass


class Limite(Conta):
    # Atributos
    def __init__(self, numero, nome, saldo, limite):
        super().__init__(numero, nome, saldo)
        self.limite = limite

    # Metodos
    def saque(self, valor):
        if (self.saldo - valor) < (-self.limite):
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor


class Poupanca(Conta):
    # Atributos
    def __init__(self, numero, nome, saldo, data):
        super().__init__(numero, nome, saldo)
        self.data = data
