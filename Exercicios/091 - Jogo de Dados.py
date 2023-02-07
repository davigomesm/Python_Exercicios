#   Exercício Python 091 - Jogo de Dados em Python
#   Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#   Guarde esses resultados em um dicionário em Python.
#   No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
rank = list()
print('Valores Sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking: ')
for i, v in enumerate(rank):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
    sleep(1)
