# Exercício 04
"""
Uma fábrica de M&M's está avaliando a qualidade de seus sacos de M&M's com base na distribuição de cores. O objetivo é garantir que nenhum saco tenha uma diferença muito grande entre a cor que mais aparece e a cor que menos aparece. As cores são: vermelho, azul, amarelo, verde, laranja, e marrom.

As regras de qualidade estabelecem que:
    A quantidade da cor que mais aparece não pode exceder 50% da quantidade total de M&M's no saco.
    A quantidade da cor que menos aparece também não pode ser inferior a 10% do total de M&M's.

Para ajudar a fábrica a avaliar a qualidade dos sacos, você deve criar uma função chamada analisar_cores_mms que retorna a quantidade de sacos que atendem às regras de qualidade. A função deve receber uma lista de sacos de M&M's, onde cada saco é representado por uma lista com a quantidade de cor de cada M&M. Por exemplo, o saco [10, 20, 30, 40, 50, 60] contém 10 M&M's vermelhos, 20 azuis, 30 amarelos, 40 verdes, 50 laranjas e 60 marrons.

"""

def bubble_sort(lista : list, reverse = False):
    if reverse == False:    
        for idx in range(len(lista)-1):
            for i in range(len(lista)-idx-1):    
                if lista[i] > lista[i + 1]:
                    lista[i],lista[i + 1] = lista[i+ 1], lista[i] 
        return lista
    elif reverse == True:
        for idx in range(len(lista)-1):
            for i in range(len(lista)-idx-1):    
                if lista[i] < lista[i + 1]:
                    lista[i],lista[i + 1] = lista[i+ 1], lista[i] 
        return lista



def analisar_cores_mms(sacos):
    a = 0
    for idx in range(len(sacos)):
        somer = sum(sacos[idx]) 
        min =bubble_sort(sacos[idx])[0]
        max = bubble_sort(sacos[idx],reverse=True)[0]
        if min >= somer* 0.10 and max <= somer * 0.50:
            a += 1
    return a

def main(): 
    # Gerar sacos aleatórios de M&M's com semente constante (não modificar)"
    import random

    random.seed(42)
    sacos = [[random.randint(1, 100) for _ in range(6)] for _ in range(100)]

    # Avaliar sacos de M&M's
    resultado = analisar_cores_mms(sacos)

    # Imprimir resultado
    print(f"Sacos de M&M's que atendem às regras de qualidade: {resultado}")


if __name__ == "__main__":
    main()
