# -*- coding: utf-8 -*-

"""
Editor Spyder

Linguagem de programação 2 

Aula 4 Ex 4
"""

lista = []
for i in range(10):
    lista.append(input("Nome:"))

def posicao(l,i):
    try:
        if i >= 5:
            raise IndexError
        print('Indice',i,':',l[i])
        
    except IndexError:
        print('Indice deve ser de 0 a 4')
        
posicao(lista,15)