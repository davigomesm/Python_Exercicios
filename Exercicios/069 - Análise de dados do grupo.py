#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

total18 = 0
totalhomens = 0
totalmulheres20 = 0
while True:
    idade = int(input("idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Digite o sexo: ")).upper().strip()[0]
    if idade >= 18:
        total18 = total18 + 1
    if sexo == "M":
        totalhomens = totalhomens + 1
    if sexo == "F":
        totalmulheres20 = totalmulheres20 + 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [Sim/Não]: ")).upper().strip()[0]
    if resposta == "N":
        break
print("total de pessoas com mais de 18 anos: {}".format(total18))
print("total de homens: {}".format(totalhomens))
print("total de mulheres com menos de 20 anos: {}".format(totalmulheres20))
