# Exercício 03
"""
Você foi encarregado de realizar uma simulação para analisar o comportamento de um dado de seis faces (numerado de 1 a 6). Para isso, siga os passos abaixo:

Crie uma função chamada simular_lancamento_dado que simule o lançamento de um dado 100 vezes. A função deve retornar uma lista com os resultados dos lançamentos, ou seja, números inteiros entre 1 e 6.

Usando os dados gerados pela função, responda às perguntas abaixo:

a) Qual foi o número que mais apareceu nos lançamentos?
b) Qual foi o número que menos apareceu?
c) Qual é a frequência de cada número (de 1 a 6) nos 100 lançamentos?
d) Qual foi a porcentagem de vezes que o número 6 apareceu nos lançamentos?

Escreva uma função analisar_resultados_dado que receba a lista de resultados dos lançamentos e responda às perguntas acima.

# Exemplo de saída esperada:

Lançamentos: [3, 6, 2, 1, 5, 4, 6, ..., 2]
Número que mais apareceu: 6
Número que menos apareceu: 1
Frequência de cada número: {1: 12, 2: 15, 3: 20, 4: 18, 5: 17, 6: 18}
Porcentagem de 6: 18%

"""
import random
random.seed(42)

def simular_lancamento_dado(time = 100):
    lista_de_jogadas = []
    for i in range(0,time):      
        lista_de_jogadas.append(random.randint(1,6))
    return lista_de_jogadas

def analisar_resultados_dado(lancamentos):
    meu_dict = {}
    count = 0
    lancamentos = simular_lancamento_dado()
    print(lancamentos)
    for i in lancamentos:
        meu_dict[i] =lancamentos.count(i)
        count += 1 
    sorteddict = dict(sorted(meu_dict.items(), key= lambda item: item[1],reverse=False))
    last_one, last_value = tuple(sorteddict.keys())[len(sorteddict)-1], tuple(sorteddict.values())[len(sorteddict)-1]
    first_one, first_value = tuple(sorteddict.keys())[0], tuple(sorteddict.values())[0]
    six_perc = (meu_dict[6] / len(lancamentos)) * 100
    stringNums= ''.join([str(i)+ ', ' for i in lancamentos])
    stringNums= stringNums.strip()[0:len(stringNums)-2:]
    
    return print(f'''
        Lançamentos: {f'{stringNums[0:20-1:1]}...' + ' ' + f',{stringNums[-1]}'} 
        Número que mais apareceu: {last_one}, com {last_value} aparicões
        Número que menos apareceu: {first_one}, com {first_value} aparicões
        Frequência de cada número: {sorteddict}
        Porcentagem de 6: {six_perc:.2f}%
''')
    
    #####################################################################################
    
def main():
    lancamentos = simular_lancamento_dado()
    analisar_resultados_dado(lancamentos)


if __name__ == "__main__":
    main()
