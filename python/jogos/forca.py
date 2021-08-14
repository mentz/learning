import random


def imprime_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha.strip().upper() for linha in arquivo]

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]

    return letras_acertadas


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1


def imprime_mensagem_vencedor():
    print("Você venceu!")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu :(")
    print("A palavra secreta era {}".format(palavra_secreta))


def desenha_forca(erros):
    print("  _______     ")
    print(" |  /    |    ")

    if erros == 1:
        print(" | /    (_)   ")
        print(" |/           ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" | /    (_)   ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" | /    (_)   ")
        print(" |/    --|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" | /    (_)   ")
        print(" |/    --|--  ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" | /    (_)   ")
        print(" |/    --|--  ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" | /    (_)   ")
        print(" |/    --|--  ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" | /    (_)   ")
        print(" |/    --|--  ")
        print(" |       |    ")
        print(" |      / \\   ")

    print("_|___         ")
    print()


def jogar():
    imprime_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
