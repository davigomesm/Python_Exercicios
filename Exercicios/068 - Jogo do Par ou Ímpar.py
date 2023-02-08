#   Exercício Python 068 - Jogo do Par ou Ímpar
#   Faça um programa que jogue par ou ímpar com o computador.
#   O jogo só será interrompido quando o jogador perder,
#   mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

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
            print("Você ganhou!")
            vitorias = vitorias + 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você ganhou!")
            vitorias = vitorias + 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente! ")
print("Total de vitorias consecutivas {}".format(vitorias))
