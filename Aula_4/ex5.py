# -*- coding: utf-8 -*-

"""
Editor Spyder

Linguagem de programação 2 

Aula 4 Ex 5
"""

def buscar(alunos, ra):
    try:
        return alunos[ra]
    except KeyError:
        return "Não encontrado"
 
 
alunos = {}
for i in range(5):
    while True:
        try:
            ra = int(input('RA: '))
            s = str(ra)
            if len(s) != 7:
                raise ValueError
            if ra in alunos:
                raise TypeError
        except ValueError:
            print("O RA deve ser um numero inteiro de 7 digitos")            
        except TypeError:
            print("RA ja existe")
        else:
            break
         
    nome = input('Nome: ')
    alunos[ra] = nome
   
    
print(alunos)
 
ra = int(input('Informe o RA de um aluno para realizar a busca: '))
nome = buscar(alunos, ra)
print('Nome do aluno:', nome)