import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

def craps():
    primeira_jogada = lancar_dados()
    print(f"Dados lançados: {primeira_jogada}")

    if primeira_jogada == 7 or primeira_jogada == 11:
        print("Natural! Jogador ganhou")
    elif primeira_jogada == 2 or primeira_jogada == 3 or primeira_jogada == 12:
        print("Craps! Jogador perdeu")
    else:
        print(f"Seu ponto é {primeira_jogada}")
        while True:
            proximo_lance = lancar_dados()
            print(f"Você lançou de novo e obteve {proximo_lance}")
            if proximo_lance == primeira_jogada:
                print("Ganhou")
                break
            elif proximo_lance == 7:
                print("7! Perdeu")
                break

craps()
