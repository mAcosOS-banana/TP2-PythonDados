# Exercício 11
"""
Dada a lista de números inteiros abaixo:
"""

numeros = [3, 8, 1, 5, 9, 2, 7, 4, 6]

"""

Escreva um programa que faça o seguinte:
    a) Ordene a lista em ordem crescente e exiba o resultado.
    b) Remova o menor número da lista e exiba a lista atualizada.
    c) Adicione o número 10 no final da lista.
    d) Exiba a soma de todos os números da lista atualizada.
    e) Exiba o maior número da lista após as modificações.

"""
from exercicio04 import bubble_sort

def main():
    sorted_list = bubble_sort(numeros)
    sorted_list2= sorted_list[1::]
    sorted_list2.append(10)
    soma = sum(sorted_list2)
    maiornumero =sorted_list2[-1]
    return print(
        f'''lista ordenada: {sorted_list}\nlista sem o menor número: {sorted_list2}\nsoma dos valores:{soma}\nmaior número:{maiornumero}\n''')


if __name__ == "__main__":
    main()
