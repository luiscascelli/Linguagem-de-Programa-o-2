# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2 

Aula 3 Ex2
"""

notas = {'Aluno1':[5.5,2.3,10],'Aluno2':[4.6,9.6,2.1],'Aluno3':[8.7,6.1,9.8],
         'Aluno4':[3.5,7.9,9.2],'Aluno5':[5,9,7],'Aluno6':[2.6,3.7,10]}

print('Medias:')
for i in notas:
    m = sum(notas[i])/len(notas[i])
    print(f"{i}:{m:.2f}")

