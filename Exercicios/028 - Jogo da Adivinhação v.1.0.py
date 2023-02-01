from random import randint
computador = randint(0, 5)
print("COMPUTADOR: -VOU SORTEAR UM NUMERO DE 0 A 5, TENTE ACERTAR.")
print("=-"*40)
jogador = int(input("Digite um número de 0 a 5: "))
print("=-"*40)
print("O NUMÉRO SORTEADO FOI O {}".format(computador))
if jogador == computador:
    print("\033[32mPARABENS VOCE ACERTOU O NÚMERO\033[m")
else:
    print("\033[31mQUE PENA, VOCE ERROU O NÚMERO\033[m")
