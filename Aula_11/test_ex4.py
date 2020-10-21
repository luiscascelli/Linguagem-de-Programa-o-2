# -*- coding: utf-8 -*-
"""
Linguagem de Programacao II

Aula 11 - Polimorfismo e Classes Abstratas

Testes para o Ex 4
"""


import unittest
from ex4 import Comum, Poupanca, Limite


class Verificar_ex4(unittest.TestCase):

    def test_deposito(self):
        # Arrange
        co = Comum(1, 'Jose')

        # Act
        co.deposito(10)

        # Assert
        self.assertEqual(10, co.saldo)

    def test_saque(self):
        # Arrange
        po = Poupanca(2, 'Ze', 10, '01-05-2018')
        li = Limite(3, 'Joao', 5, 10)

        # Act
        po.saque(10)
        li.saque(15)

        # Assert
        self.assertEqual(0, po.saldo)
        self.assertEqual(-10, li.saldo)

        # Act
        po.deposito(10)
        li.deposito(15)
        po.saque(11)
        li.saque(16)

        # Assert
        self.assertEqual(10, po.saldo)
        self.assertEqual(5, li.saldo)


if __name__ == '__main__':
    unittest.main()
