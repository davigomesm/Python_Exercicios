#   Exercício Python 071 - Simulador de Caixa Eletrônico
#   Crie um programa que simule o funcionamento de um caixa eletrônico.
#   No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#   e o programa vai informar quantas cédulas de cada valor serão entregues.
#       OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

import time
print("Banco DaviZin")
valor = int(input("Digite quanto vc quer sacar: R$"))
total = valor
cedula = 50
totalcedula = 0
print("IMPRIMINDO...")
time.sleep(3)
while True:
    if total >= cedula:
        total = total - cedula
        totalcedula = totalcedula + 1
    else:
        if totalcedula > 0:
            print("total de {} cedulas de R${}".format(totalcedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula == 1
        totalcedula = 0
        if total == 0:
            break
