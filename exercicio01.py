# Exercício 01

"""
Em Python, funções são blocos de código que realizam uma tarefa específica e podem ser reutilizadas em diferentes partes do programa. Sobre as funções em Python, responda às perguntas abaixo:
"""

# 1) O que é uma função e qual a principal vantagem de utilizá-las em um programa?
"""
'''
    Economia de código e tempo. Funções bem estruturadas permitem executar códigos sem que haja uma repetição do mesmo.
    também serve para garantir uma melhor
    '''
"""

# 2) Qual é o número mínimo e o número máximo de parâmetros que uma função pode ter em Python?
"""
0 e até aonde o sistema aguentar com os argumentos variaveis *args
"""

# 3) O que é um parâmetro padrão (default) em uma função? Escreva um exemplo de função com um parâmetro padrão e explique seu funcionamento.
"""
é um parametro que já possui valor pré definido
Modifique o nome e escreva a função abaixo
"""


def anos_10_mais_velho(soma = 10):
    user = ''
    while user.isdigit() == False:   
        user = input('Quantos anos tem?')
        if user.isdigit():
            futureage = int(user) + soma
            return print(futureage)
        else:
            print('Digite um número válido')
anos_10_mais_velho()

