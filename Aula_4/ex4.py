# -*- coding: utf-8 -*-

"""
Editor Spyder

Linguagem de programação 2 

Aula 4 Ex 4
"""

lista = []
for i in range(5):
    lista.append(input("Nome:"))

def posicao(l,i):
    try:
        return  l[i]  
    except IndexError:
        return "Indice não existe"
        
n = posicao(lista,8)
print(n)