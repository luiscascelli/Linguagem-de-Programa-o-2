# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 2 Ex5

"""
from random import randint

l1 = []
l2 = []
for i in range (5):
    l1.append(randint(0,100))
    l2.append(randint(0,100))

tupla1 = (l1[0],l1[1],l1[2],l1[3],l1[4])
tupla2 = (l2[0],l2[1],l2[2],l2[3],l2[4])
tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)