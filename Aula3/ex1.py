# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 3 Ex1
"""

precos = {'Skol':18.9,'Brahma':1.99,'Antarctica':1.50,
          'Stella':50.05,'Bud':49.65,'Imperio':53.78}

print('Preco superior a 50:')
for i in precos:
    if precos[i] >= 50:
        print(i,':',precos[i])

