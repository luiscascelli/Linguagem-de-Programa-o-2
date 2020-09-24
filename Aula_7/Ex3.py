# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 7 Ex 3
"""


class Carro():
    # Atributos
    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.ligado = False
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4

    # Metodos
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def verificar_pneu(self):
        if self.ligado:
            print('Pressao pneu 1:', self.pneu1.pressao)
            print('Pressao pneu 2:', self.pneu2.pressao)
            print('Pressao pneu 3:', self.pneu3.pressao)
            print('Pressao pneu 4:', self.pneu4.pressao)
        else:
            print('Carro Desligado')


class Pneu():
    # Atributos
    def __init__(self, pressao):
        self.pressao = pressao

    # Metodos
    def furar(self):
        self.pressao = 0


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()
meucarro.desligar()
meucarro.verificar_pneu()
