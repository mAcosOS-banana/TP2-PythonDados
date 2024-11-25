"""
Você foi contratado para criar uma função que gera um relatório de vendas. A função deve receber uma lista de vendas (valores monetários) e um parâmetro opcional chamado imposto, que representa o percentual de imposto a ser aplicado nas vendas. O parâmetro imposto deve ter um valor padrão de 10% caso não seja informado. A função deve retornar o valor total das vendas após a aplicação do imposto.

A Saída esperada para o exemplo abaixo é:
Total com imposto padrão: R$ 660.00
Total com imposto de 5%: R$ 630.00

"""


# Modifique a função abaixo para que ela atenda aos requisitos do enunciado de parametros valores padrão.
def calcular_total_vendas(vendas, imposto=10):
    perc = (100 + imposto) / 100
    vendas_com_imposto =  [i * perc for i in vendas]
    return sum(vendas_com_imposto)


def main():
    vendas = [100, 200, 300]
    total_com_imposto_padrao = calcular_total_vendas(vendas)
    total_com_imposto = calcular_total_vendas(vendas, imposto=5)
    print(f"total_com_imposto_padrao = {total_com_imposto_padrao}")
    print(f"total_com_imposto = {total_com_imposto}")


# Exemplo de uso 1 (sem informar o imposto)

if __name__ == "__main__":
    main()
