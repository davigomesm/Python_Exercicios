#   Exercício Python 082 - Valores únicos em uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista.
#   Depois disso, crie duas listas extras que vão conter apenas os valores pares e
#   os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input("Digite um numero: ")))
    r = str(input("deseja continuar? [S/N] "))
    if r in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f"A lista completa: {lista}")
print(f"A lista de numero pares: {pares}")
print(f"A lista de numeros impares: {impares}")
