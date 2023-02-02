from random import randint


def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Lista: {lista}')


def soma(lista):
    print(f'A soma entre os itens da lista é: {sum(lista)}')


numeros = list()
sorteia(numeros)
soma(numeros)
