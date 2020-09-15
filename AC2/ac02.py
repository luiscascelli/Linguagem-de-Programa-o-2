# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 5 alunos)
# ALUNO 1: Luis Antonio Matile Cascelli 1903598
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:


def calcular_salario(dicionario, nome):
    if dicionario[nome][2] == "DESENVOLVEDOR":
        if dicionario[nome][1] >= 2000:
            sl = dicionario[nome][1]*0.85
        else:
            sl = dicionario[nome][1]*0.95
    elif dicionario[nome][2] == "ANALISTA":
        if dicionario[nome][1] >= 3500:
            sl = dicionario[nome][1]*0.80
        else:
            sl = dicionario[nome][1]*0.90
    elif dicionario[nome][2] == "GERENTE":
        if dicionario[nome][1] >= 4000:
            sl = dicionario[nome][1]*0.75
        else:
            sl = dicionario[nome][1]*0.85
    else:
        raise TypeError
    return sl
