from random import randint
vitorias = 0
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Impar ou Par? [P/I] ")).strip().upper()[0]
    print("Você jogou {} e o computador jogou {}, total de {}".format(jogador, computador, total))
    if tipo == "P":
        if total % 2 == 0:
            print("\033[33mVocê ganhou!\033[m")
            vitorias = vitorias + 1
        else:
            print("\033[31mVocê perdeu!\033[m")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("\033[33mVocê ganhou!\033[m")
            vitorias = vitorias + 1
        else:
            print("\033[31mVocê perdeu!\033[m")
            break
    print("Vamos jogar novamente! ")
print("Total de vitorias consecutivas {}".format(vitorias))
