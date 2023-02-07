#   Exercício Python 085 - Listas com pares e ímpares
#   Crie um programa onde o usuário possa digitar sete valores numéricos e
#   cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#   No final, mostre os valores pares e ímpares em ordem crescente.

n = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print(f"Os valores pares: {n[0]}")
print(f"Os valores impares: {n[1]}")
