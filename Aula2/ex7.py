# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 2 Ex5

"""
def intercala_numeros(t1,t2):
    t = (t1[0],t2[0],t1[1],t2[1],t1[2],t2[2])
    return t
    
from random import randint

l1 = []
l2 = []
for i in range (3):
    l1.append(randint(0,100))
    l2.append(randint(0,100))

tupla1 = (l1[0],l1[1],l1[2])
tupla2 = (l2[0],l2[1],l2[2])
tupla3 = intercala_numeros(tupla1, tupla2)

print(tupla1)
print(tupla2)
print(tupla3)

