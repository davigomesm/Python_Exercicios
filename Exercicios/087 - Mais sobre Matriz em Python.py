#   Exercício Python 087 - Mais sobre Matriz em Python
#    Aprimore o desafio anterior, mostrando no final:
#       A) A soma de todos os valores pares digitados.
#       B) A soma dos valores da terceira coluna.
#       C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite uma valor para {l}, {c}: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end="")
        if matriz[l][c] % 2 == 0:
            somapar =  somapar + matriz[l][c]
    print()
for l in range(0, 3):
    somacol = somacol + matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"A soma dos valores pares: {somapar}")
print(f"A soma dos valores da terceira coluna: {somacol}")
print(f"O maior valor da segunda coluna: {maior}")
