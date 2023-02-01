from random import randint
from time import sleep

print("{:=^45}".format("\033[1;32m PEDRA PAPEL TESOURA \033[m"))
print("""\033[1mSuas opções:\033[m
\033[1;37m[0] PEDRA\033[m
\033[1m[1] PAPEL\033[m
\033[1;34m[2] TESOURA\033[m""")

itens = ["pedra", "papel", "tesoura"]
computador = randint(0, 2)
jogador = int(input("\033[1mQual a sua jogada? \033[m"))

print("\033[31mJÓ\033[m")
sleep(1)
print("\033[33mKEN\033[m")
sleep(1)
print("\033[32mPÔ!\033[m")

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("VITORIA!")
    elif jogador == 2:
        print("DERROTA!")
    else:
        print("JOGADA INVALIDA!")

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print("DERROTA!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("VITORIA!")
    else:
        print("JOGADA INVALIDA!")

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("VITORIA!")
    elif jogador == 1:
        print("DERROTA!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVALIDA!")

if jogador == 0 or 1 or 2:
    print("=-=" * 10)
    print("\033[1;34mCOMPUTADOR ESCOLHEU: {}\033[m".format(itens[computador]))
    print("\033[1;36mJOGADOR ESCOLHEU: {}\033[m".format(itens[jogador]))
    print("=-=" * 10)

else:
    print("JOGADA INVALIDA!")
