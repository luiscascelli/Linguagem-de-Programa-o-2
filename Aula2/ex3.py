# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 2 Ex3

"""
from random import randint

lista = []
for i in range (10):
    lista.append(randint(0,100))
    
pares = []
impares = []
for i in lista:
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Pares:',pares)
print('Impares:',impares)
