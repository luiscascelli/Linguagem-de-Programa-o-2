# -*- coding: utf-8 -*-

"""
Editor Spyder

Linguagem de programação 2 

Aula 4 Ex 2
"""

while True:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
        
    except ValueError:
        print("Os valores devem ser numeros inteiros")
        
    except ZeroDivisionError:
        print("O segundo valor deve ser diferente de zero")    
    
    else:
        break

print('O resultado da divisão é:', z)