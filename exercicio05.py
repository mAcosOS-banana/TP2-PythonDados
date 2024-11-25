# Exercício 05
"""O Instituto Nacional de Meteorologia (INMET) está monitorando as chuvas em diversas regiões do Brasil e gerou um conjunto de dados fictícios com a quantidade de chuva acumulada (em milímetros) nos últimos 12 meses em 5 capitais brasileiras: São Paulo, Rio de Janeiro, Brasília, Salvador, e Porto Alegre.

Os dados são representados em uma lista de listas onde cada sublista contém o nome da cidade e uma lista com as chuvas acumuladas em milímetros para cada mês (de janeiro a dezembro):

"""

chuvas = [
    ["São Paulo", [150, 200, 180, 140, 160, 170, 210, 220, 200, 180, 190, 210]],
    ["Rio de Janeiro", [180, 220, 210, 190, 160, 150, 240, 250, 230, 210, 200, 190]],
    ["Brasília", [100, 120, 130, 110, 90, 80, 60, 50, 70, 110, 120, 140]],
    ["Salvador", [220, 240, 230, 210, 200, 220, 230, 240, 250, 260, 250, 240]],
    ["Porto Alegre", [180, 200, 190, 170, 160, 150, 180, 190, 210, 220, 230, 210]],
]

"""
Com base nesses dados, responda às seguintes perguntas:

    Qual cidade teve a maior quantidade total de chuva acumulada no ano?
    Qual cidade teve a menor quantidade total de chuva acumulada no ano?
    Qual foi o mês mais chuvoso em São Paulo e qual foi a quantidade de chuva acumulada nesse mês?
    Qual é a média mensal de chuva em Salvador ao longo do ano?
    Qual é a cidade com a maior variação de chuva entre o mês mais seco e o mês mais chuvoso? Qual é essa variação?


Crie funções para responder a cada uma das perguntas acima. 
Em seguida, adicione na função main a chamada para cada uma das funções e imprima os resultados.
"""

def maior_quantidade (lista: list):
    chuva_soma = {}
    map_variacoes = {}
    months = {1: 'janeiro',2:'fevereiro',3:'abril',4:'março',5:'maio',6:'junho',7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}

    for i in range(len(lista)-1):
        chuva_soma[chuvas[i][0]] = sum(chuvas[i][1])
    sortedchuvas = sorted(chuva_soma.items(),key=lambda item: item[1]) 
    for i in chuvas:
        maior_numero = i[1][0]
        menor_numero = i[1][0]
        media = round(sum(i[1]) / len(i[1]),1)
        for idx , _ in enumerate(i[1]):
            if _ > maior_numero:
                maior_numero = _
                mes  = months[idx]
            elif _  < menor_numero: 
                menor_numero = _ 
                mes2 = months[idx]
            variacao = maior_numero - menor_numero
            map_variacoes[i[0]] = variacao
            map_variacoes_t = sorted(map_variacoes.items(),key= lambda item: item[1])
       


        
        print('\n'.center(75))
        print(f'{i[0]}'.center(75))
        print('---------------------------------------------------'.center(75))
        print(f'maior mês/valor: {mes} = {maior_numero} milimetros'.title().center(75))
        print(f'menor mês/valor: {mes2} = {menor_numero} milimetros'.title().center(75))
        print(f'variação: {variacao} milimetros'.title().center(75))
        print(f'media mensal: {media} milimetros/m'.title().center(75))
    print('\n'.center(75))
    print(f'A cidade com maior variação foi {map_variacoes_t[-1][0]} com um variação de {map_variacoes_t[-1][1]} milimetros')
    print(f'A cidade que teve a maior quantidade de chuva foi {sortedchuvas[-1][0]} com {sortedchuvas[-1][1]} milimetros')
    print(f'A cidade que teve a menor quantidade de chuva foi {sortedchuvas[0][0]} com {sortedchuvas[0][1]} milimetros')
def main():
    maior_quantidade(chuvas)
    pass


if __name__ == "__main__":
    main()
