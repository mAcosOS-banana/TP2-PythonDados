# Exercício 10
"""
Uma empresa de tecnologia quer analisar a performance de seus vendedores com base nas vendas realizadas durante o mês. Eles pediram que você desenvolva um programa para processar os dados de vendas e exibir o ranking dos vendedores com base no número de vendas realizadas.
Você deve criar uma função ranking_vendedores(vendedores) que receba uma lista de tuplas. Cada tupla contém dois elementos: o nome do vendedor (uma string) e o número de vendas realizadas (um número inteiro). A função deve retornar uma lista com os nomes dos vendedores ordenados do maior para o menor número de vendas. Se dois vendedores tiverem o mesmo número de vendas, eles devem ser ordenados em ordem alfabética.
"""

import random

randomizer = [random.randint(0,100) for i in range(5)]
vendedores = [("Alice", randomizer[0]), ("Bob", randomizer[1]), ("Carlos", randomizer[2]), ("Diana", randomizer[3]), ("Eva", randomizer[4])]


def ranking_vendedores(vendedores):
    dicio = {}
    contador = 0
    for i in vendedores:
        dicio[i[0]] = i[1]
        dicio = dict(sorted(dicio.items(), key=lambda item: item[1],reverse=True))
    for idx, i in enumerate(list(dicio.items())):
        contador += 1
        match contador:
            case 1:
                print(f'🥇 {list(dicio.keys())[idx]:<6}', f'{"🟦"*(list(dicio.items())[idx][1]//2)}', f'{list(dicio.values())[idx]} vendas')
            case 2:
                print(f'🥈 {list(dicio.keys())[idx]:<6}', f'{"🟦"*(list(dicio.items())[idx][1]//2)}', f'{list(dicio.values())[idx]} vendas')
            case 3:
                print(f'🥉 {list(dicio.keys())[idx]:<6}', f'{"🟦"*(list(dicio.items())[idx][1]//2)}', f'{list(dicio.values())[idx]} vendas')
            case _:
                print(f' {contador} {list(dicio.keys())[idx]:<6}', f'{"🟦"*(list(dicio.items())[idx][1]//2)}', f'{list(dicio.values())[idx]} vendas')        


def main():
    resultado = ranking_vendedores(vendedores)
    print("Ordem dos melhores vendoedores:\n", resultado)
main()