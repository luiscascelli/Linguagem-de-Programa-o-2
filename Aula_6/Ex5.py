# -*- coding: utf-8 -*-
"""
Editor Spyder

Linguagem de programação 2

Aula 6 Ex 5

Classe Aluno
Atributos: nome, tempo_sem_dormir
Metodos: estudar(horas), dormir(horas)
"""


class Aluno():
    # atributos
    def __init__(self):
        self.nome = None
        self.tempo_sem_dormir = 0

    def estudar(self, horas):
        self.tempo_sem_dormir += horas

    def dormir(self, horas):
        self.tempo_sem_dormir -= horas


aluno1 = Aluno()
aluno1.nome = "Luizinho"
aluno1.estudar(3)
aluno1.dormir(2)
aluno1.estudar(4)
aluno1.dormir(2)
print(f'O aluno {aluno1.nome} está {aluno1.tempo_sem_dormir} horas sem dormir')
