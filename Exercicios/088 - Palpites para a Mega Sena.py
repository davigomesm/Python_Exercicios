#   Exercício Python 088 - Palpites para a Mega Sena
#   Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#   O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo.

from random import randint
from time import sleep
lista = []
jogos = []
print("MEGA SENA")
quant = int(input("quantos jogos vc quer que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print(f"Sorteando {quant} Jogos ...")
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")
    sleep(1)
print("Boa sorte!")
