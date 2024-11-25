"""
Escreva uma função chamada meu_split que deve receber uma string e um delimitador. A função deve dividir a string em partes com base no delimitador fornecido e retornar uma lista contendo as partes resultantes. A função deve replicar o comportamento básico
da função embutida split() do Python.
Requisitos
 • A função deve aceitar dois parâmetros:
    • texto (tipo str): A string que será dividida.
    • delimitador (tipo str): O caractere ou string que será usado como delimitador para dividir texto.
 • A função deve levar em consideração:
    • Delimitadores consecutivos (ou seja, se houver dois delimitadores seguidos, a função deve incluir na lista partes vazias).
    • Caso o delimitador não seja encontrado na string, a função deve retornar uma lista contendo a string original como seu único elemento.

Obs: Não utilize a função split do python nessa questão.

"""


def meu_split(texto, delimitador = ' '):
    
    
    lista_de_palavras = []
    palavras = ''
    for i in texto:
        print(palavras)
        if i == delimitador:
            if palavras:
                print(palavras)
                lista_de_palavras.append(palavras)
                palavras = ''
        else:
            palavras += i
    if palavras:
        lista_de_palavras.append(palavras)

    return lista_de_palavras
        
    




def main():
    resultado = meu_split("Olá, como você está?", " ")
    print(resultado)  # Saída esperada: ['Olá,', 'como', 'você', 'está?']

    resultado = meu_split("Um|dois|três|quatro", "|")
    print(resultado)  # Saída esperada: ['Um', 'dois', 'três', 'quatro']

    resultado = meu_split("Texto sem delimitador", "#")
    print(resultado)  # Saída esperada: ['Texto sem delimitador']


if __name__ == "__main__":
    main()
