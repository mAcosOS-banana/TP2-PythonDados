# Exercício 07
"""
Você recebeu os dados do IPCA (Índice de Preços ao Consumidor Amplo) de diversas categorias de consumo em várias regiões brasileiras. Abaixo estão as variações percentuais no último mês para três grupos de consumo: Alimentação e bebidas, Habitação, e Vestuário, nas regiões Aracaju, Belo Horizonte, Belém, Brasília, Campo Grande, e Curitiba.

Os dados estão organizados da seguinte forma:
"""

cidades = ["Aracaju", "Belo Horizonte", "Belém", "Brasília", "Campo Grande", "Curitiba"]
alimentos_bebidas = [-1.04, 0.95, -0.33, 0.5, 0.49, 0.64]  # Aracaju, BH, Belém, Brasília, Campo Grande, Curitiba
habitacao = [1.82, 1.51, 1.44, 1.4, 1.78, 2.06]  # Aracaju, BH, Belém, Brasília, Campo Grande, Curitiba
vestuario = [0.95, 0.17, 0.21, 0.18, 0.13, -0.24]  # Aracaju, BH, Belém, Brasília, Campo Grande, Curitiba

""""
Com base nesses dados, responda às seguintes perguntas:

    Qual foi a maior variação no grupo "Alimentação e bebidas" entre todas as regiões?
    Qual foi a média de variação do grupo "Habitação" em todas as regiões?
    Quantas regiões apresentaram uma variação negativa no grupo "Vestuário"?
    Qual grupo apresentou a maior variação total somando todas as regiões?

Crie funções para responder a cada uma das perguntas acima.
"""
def analisador (lista: list, *args: list):
    dicionário = {}
    grupos_soma = {}
    for jdx ,_ in enumerate(['Alimentos_e_Bebeidas', 'Habitação','Vestuário']):
        grupos_soma[_]=sum(args[jdx])
    grupos_soma = dict(sorted(grupos_soma.items(),key=lambda item: item[1]))
    maior = 0
    menor = 0
    mediahab = 0
    somados = 0
    regioes_com_vest_mn_0 = 0
    for idx, i in enumerate(lista):
        dicionário[i]= args[0][idx],args[1][idx],args[2][idx]
        if dicionário[i][0] > maior:
            maior, cidade_maior = dicionário[i][0], i
        elif dicionário[i][0] < menor:
            menor, cidade_menor = dicionário[i][0], i
        elif dicionário[i][2] < 0:
            regioes_com_vest_mn_0 += 1
            cidade_menor_vest_0 = i
        somados += dicionário[i][0]

    mediahab = somados / len(args[2])
    print('---------------------------------------------------------------------------------------------------------------'.center(120))
    print(f'No grupo Alimentação e bebidas a maior variação foi a da cidade {cidade_maior} com {maior}% de variação'.center(120))
    print(f'A média de variação em habitação foi {mediahab:.1f}%'.center(120))
    print(f'Regiões com valores negativos {cidade_menor_vest_0}, com {regioes_com_vest_mn_0} {'valores' if regioes_com_vest_mn_0 > 1 else 'valor'}'.center(120))
    print(f'O Grupo com maior variação foi {list(grupos_soma.keys())[-1]} com {max(grupos_soma.values())}%'.center(120))
    print('---------------------------------------------------------------------------------------------------------------'.center(120))


    
def main():
    analisador(cidades, alimentos_bebidas, habitacao, vestuario)
    


if __name__ == "__main__":
    main()
