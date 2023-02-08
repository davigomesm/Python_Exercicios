#   Exercício Python 078 - Maior e Menor valores na Lista
#   Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#   No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input("Digite um numero para a posição {}: ".format(c))))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(lista)
print("O maior numero digitado foi: {} nas posições: ".format(maior), end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print()
print("O menor numero digitado foi: {} nas posições: ".format(menor), end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
print()
