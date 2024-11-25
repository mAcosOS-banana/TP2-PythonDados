# Exercício 06

"""
Você recebeu uma lista com o nome de 5 alunos e suas respectivas 4 notas. Sua tarefa é criar um programa em Python que exiba essas informações em forma de uma tabela formatada. A tabela deve conter o nome dos alunos, suas notas e a média de cada um.

Os dados são os seguintes:

"""

alunos = [
    ["João", [7.5, 8.0, 6.5, 9.0]],
    ["Maria", [8.5, 9.0, 7.5, 8.0]],
    ["Carlos", [6.0, 7.5, 8.0, 6.5]],
    ["Ana", [9.0, 8.5, 9.5, 8.0]],
    ["Lucas", [5.5, 6.0, 7.0, 6.5]],
]


"""
Com base nesses dados, siga os passos abaixo:

Crie uma função chamada calcular_media que receba as notas de um aluno e retorne a média das quatro notas.
Crie uma função chamada imprimir_tabela que receba a lista de alunos e exiba uma tabela formatada, contendo:

Nome do aluno
Suas quatro notas
A média das notas
A tabela deve ter a seguinte estrutura:

Nome      Nota 1   Nota 2   Nota 3   Nota 4   Média
---------------------------------------------------
João      7.5      8.0      6.5      9.0      7.75
Maria     8.5      9.0      7.5      8.0      8.25
Carlos    6.0      7.5      8.0      6.5      7.00
Ana       9.0      8.5      9.5      8.0      8.75
Lucas     5.5      6.0      7.0      6.5      6.25
Crie as funções e exiba a tabela no formato especificado.
"""


def calcular_media(notas):
    lista_notas = []
    for i in notas:
        media = sum(i[1]) / len(i[1])
        lista_notas.append(media)
    return lista_notas
lista = calcular_media(alunos)


    
def imprimir_tabela(alunos):
    dicio_notas = {}
    cabecalho = ['Nome','Nota1','Nota2','Nota3','Nota4','Média']
    print(f'{cabecalho[0]:<10}{cabecalho[1]:<10}{cabecalho[2]:<10}{cabecalho[3]:<10}{cabecalho[4]:<10}{cabecalho[5]:<10}')
    print('-------------------------------------------------------')
    for idx, i in enumerate(alunos):
        print(f'{i[0]:<10}'+ f'{''.join([f'{str(j):<10}' for j in i[1]])}'+f'{lista[idx]:<10}')


def main():
    imprimir_tabela(alunos)


if __name__ == "__main__":
    main()
