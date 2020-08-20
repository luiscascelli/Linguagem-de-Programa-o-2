# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 2 Ex4

"""
from random import randint

dados= []
for i in range (10):
    dados.append(randint(1,6))

for i in range(1,7):
    print('Numero',i,'foi sorteado',dados.count(i),'vezes')