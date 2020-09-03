# -*- coding: utf-8 -*-

"""
Editor Spyder

Linguagem de programação 2 

Aula 4 Ex 3
"""

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        try:
            print(lista[i])
        except IndexError:
            print('A lista possui', i, 'elementos.')
            break
    print('Fim da função')
 
    
print('Início do programa')
funcao_1()
print('Fim do programa')
