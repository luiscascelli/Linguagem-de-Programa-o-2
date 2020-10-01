# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 8 Ex 3
"""


class ContaBancaria:
    # Atributos
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo

    # Metodos
    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += valor
        else:
            print('Senha Incorreta')

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print('Senha Incorreta')


class Cliente:
    # Atributos
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    # Metodos
    def get_senha(self):
        return self.__senha


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime: 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime: 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime: 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime: 150
