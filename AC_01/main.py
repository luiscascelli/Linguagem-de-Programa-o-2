'''
Esse arquivo pode ser utilizado para testar a implementação da AC01.
Não Faça nenhuma alteração nesse arquivo.
Para cada função, são realizados dois testes. 
Ao executar esse arquivo, não deve ser exibida nenhuma mensagem de ERRO.
'''


from ac01 import quantidade, excluir, posicoes_lista, aprovados, incluir_nota


def teste1():
    tupla = (2, 3, 4, 2, 5, 2)
    retorno = quantidade(tupla, 2)        # chamada da função 
    if retorno == 3:
        print(" CORRETO")
    else:
        print(" ERRADO")

    tupla = (2, 3, 4, 2, 5, 2)
    retorno = quantidade(tupla, 1)        # chamada da função
    if retorno == 0:
        print(" CORRETO")
    else:
        print(" ERRADO")


def teste2():
    lista = [1, 2, 3, 2, 4]
    retorno = excluir(lista, 2)          # chamada da função
    if retorno == [1, 3, 4]:
        print(" CORRETO")
    else:
        print(" ERRADO")
    
    lista = [1, 2, 2, 4, 4, 4, 0]
    retorno = excluir(lista, 4)         # chamada da função
    if retorno == [1, 2, 2, 0]:
        print(" CORRETO")
    else:
        print(" ERRADO")


def teste3():
    lista = ['a', 2, 'b', 'a', 'a']
    retorno = posicoes_lista(lista, 'a')        # chamada da função
    if retorno == [0, 3, 4]:
        print(" CORRETO")
    else:
        print(" ERRADO")
        
    lista = [2, 5, 5, 7, 8, 9, 10]
    retorno = posicoes_lista(lista, 5)          # chamada da função
    if retorno == [1, 2]:
        print(" CORRETO")
    else:
        print(" ERRADO")


def teste4():
    alunos = {'Augusto':[4.5, 7.0, 6.0],
              'Denise':[9.0, 8.5, 9.5],
              'Ana Paula':[3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == ['Denise', 'Marcelo']:
        print(" CORRETO")
    else:
        print(" ERRADO")    


    alunos = {'Paulo':[5.5, 5.0, 4.0],
              'Fernando':[6.0, 6.0, 6.0],
              'Maria':[10.0, 8.5, 9]}
    retorno = aprovados(alunos)                 # chamada da função
    if retorno == ['Fernando', 'Maria']:
        print(" CORRETO")
    else:
        print(" ERRADO") 


def teste5():
    alunos = {'Augusto':[4.5, 7.0, 6.0],
              'Denise':[9.0, 8.5, 9.5], 
              'Ana Paula':[3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0]}
    retorno = incluir_nota(alunos, 'Denise', 10.0)      # chamada da função
    if retorno == {'Augusto':[4.5, 7.0, 6.0],
                   'Denise':[9.0, 8.5, 9.5, 10.0],
                   'Ana Paula':[3.5, 1.0, 6.5],
                   'Marcelo': [9.0, 10.0, 7.0]}:
        print(" CORRETO")
    else:
        print(" ERRADO")
        
    retorno = incluir_nota(alunos, 'Marcelo', 5.0)      # chamada da função
    if retorno == {'Augusto':[4.5, 7.0, 6.0],
                   'Denise':[9.0, 8.5, 9.5, 10.0],
                   'Ana Paula':[3.5, 1.0, 6.5],
                   'Marcelo': [9.0, 10.0, 7.0, 5.0]}:
        print(" CORRETO")
    else:
        print(" ERRADO")



print("Função quantidade:")
teste1()

print("Função excluir:")
teste2()

print("Função posicoes_lista:")
teste3()

print("Função aprovados:")
teste4()

print("Função incluir_nota:")
teste5()
