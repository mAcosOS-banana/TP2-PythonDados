# Exercício 02
"""
Uma empresa de tecnologia está monitorando a quantidade de acessos diários ao seu site nos últimos 30 dias. Eles desejam realizar uma simulação para prever o comportamento do número de acessos nos próximos dias. Para isso, você deve:

Criar uma função chamada gerar_acessos que simula a quantidade de acessos diários ao site, retornando uma lista de números inteiros aleatórios entre 100 e 500, representando os acessos em 30 dias.

Com os dados gerados pela função, escreva uma nova função chamada calcular_media_acessos que calcule e retorne a média de acessos durante o período de 30 dias.

Suponha que o site da empresa terá uma promoção no próximo mês e eles esperam que os acessos aumentem em 20%. Escreva uma função chamada prever_acessos_futuros que receba a lista de acessos gerados e retorne uma nova lista com os acessos ajustados, considerando o aumento de 20%.

Obs
"""
import random
random.seed(42)

def gerar_acessos(dias = 30):
    lista_de_acessos = []
    for i in range(0,dias):
        lista_de_acessos.append(random.randint(100,500))
    return lista_de_acessos



def calcular_media_acessos(acessos):
    soma = 0
    for i in acessos: 
        soma += i 
    return soma / len(acessos)




def prever_acessos_futuros(acessos):
    soma = 0 
    for i in acessos:
        soma += i*1.20
    return soma / len(acessos)


def main():
    acessos = gerar_acessos()
    media_acessos = calcular_media_acessos(acessos)
    acessos_futuros = prever_acessos_futuros(acessos)
    print(
        f"A média de acessos diários no último mês foi de {media_acessos:.2f} acessos."
    )
    print(f"Previsão de acessos para o próximo mês: {acessos_futuros}")


if __name__ == "__main__":
    main()
