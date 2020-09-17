# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 3

Classe TV
Atributos: canal, volume
Metodos: aumentar_voçlume(), diminuir_volume(), alterar_canal(canal)
"""


class TV():
    # atributos
    def __init__(self):
        self.canal = None
        self.volume = 0

    # metodos
    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


tv = TV()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')
print(f'A tv está no volume {tv.volume}')
