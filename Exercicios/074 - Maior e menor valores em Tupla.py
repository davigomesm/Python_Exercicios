#   Exercício Python 074 - Maior e menor valores em Tupla
#   Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#   Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print("Valores sorteados: ")
for n in sort:
    print(f"{n} ", end=" ")
print(f"\nO maoir numero é {max(sort)}")
print(f"O menor numero é {min(sort)}")
