"""
Você está desenvolvendo uma versão do jogo da velha e precisa de uma função que verifique se há um vencedor. O tabuleiro do jogo é representado por uma lista de listas (matriz 3x3), onde cada posição pode ser 'X', 'O', ou uma string vazia '' (representando uma célula vazia). Escreva uma função chamada verificar_vencedor que recebe o tabuleiro como argumento e retorna:

    'X' se o jogador "X" venceu,
    'O' se o jogador "O" venceu,
    'Empate' se todas as posições estão preenchidas e não há vencedor,
    'Nenhum vencedor' se o jogo ainda está em andamento e ninguém venceu.
Regras:
    O jogador vence se conseguir preencher uma linha, coluna ou diagonal com três de seus símbolos.
"""


def verificar_vencedor(tabuleiro: list):
    ganhador = ''
    for i in tabuleiro:
        if i[0]== i[1] == i[2] and i[0] != '':
            return f'{i[0]}, foi o ganhador'
    
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col]== tabuleiro[2][col] and tabuleiro[0][col] != '':
            return f'{tabuleiro[0][col]}, foi o ganhador'
        
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[2][2] and tabuleiro[0][0] != '':
        return f'{tabuleiro[0][0]}, foi o ganhador'
    
    if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[2][0] and tabuleiro[0][2] != '':
        return f'{tabuleiro[0][2]}, foi o ganhador'
                
    for _ in tabuleiro:
        if '' in _:
            return 'jogo não acabou ou nenhum vencedor'
    return 'empate'


def main():
    # Exemplo de uso
    tabuleiro1 = [
        ["X", "O", "X"],         
        ["O", "X", "O"], 
        ["O", "X", "X"]]
    tabuleiro2 = [
        ["X", "O", ""],
        ["O", "O", ""],
        ["X", "", ""]
        ]
    tabuleiro3 = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
        ]
    tabuleiro4 = [
        ["O", "O", "O"],
        ["X", "X", ""],
        ["X", "", ""]
        ]

    print(verificar_vencedor(tabuleiro1))  # Saída esperada: X
    print(verificar_vencedor(tabuleiro2))  # Saída esperada: Nenhum vencedor
    print(verificar_vencedor(tabuleiro3))  # Saída esperada: Empate
    print(verificar_vencedor(tabuleiro4))  # Saída esperada: O


if __name__ == "__main__":
    main()
