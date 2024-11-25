"""
Você foi encarregado de desenvolver um gerador de senhas seguras para uma aplicação. Escreva uma função que gere uma senha aleatória de comprimento variável, que inclua letras maiúsculas, minúsculas, números e caracteres especiais. O comprimento da senha será passado como argumento.
A senha gerada deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial. A função deve retornar a senha gerada.
"""
import random
def gerar_senha_aleatoria(tamanho):
    if tamanho >= 4:
        letters = random.choice('abcdefghijklmnopqrstuvwxyz')
        uppercaseletters = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        specialchars = random.choice(r'!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        numerics = random.choice('0123456789')
        chars = letters + specialchars + numerics + uppercaseletters
        senha = ''.join(random.choice(chars) for _ in range(tamanho))
        return senha
    else:
        raise ValueError('o tamanho da senha deve ser no minimo com 4 caracteres')
def main():
    print("Uma senha aleatória de tamanho 8:", gerar_senha_aleatoria(8))
    print("Uma senha aleatória de tamanho 12:", gerar_senha_aleatoria(8))
    print("Uma senha aleatória de tamanho 4:", gerar_senha_aleatoria(4))


if __name__ == "__main__":
    main()
