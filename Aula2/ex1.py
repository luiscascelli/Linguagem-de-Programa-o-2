# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 2 Ex1
"""
numeros = []
for i in range(10):
    print('Numero[',i,']')
    numeros.append(int(input()))

print('Maximo:',max(numeros))
print('Minimo:',min(numeros))
m = sum(numeros)/len(numeros)
print('Media:',m)
print('Menores que a media:5')
for i in numeros:
    if i < m:
        print(i)

