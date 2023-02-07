#   Exercício Python 079 - Valores únicos em uma Lista
#   Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#   Caso o número já exista lá dentro, ele não será adicionado.
#   No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    n = int(input("Digite um numero: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado! ")
    else:
        print("numero duplicado!")
    r = str(input("Deseja continuar ? [S/N] "))
    if r in "Nn":
        break
lista.sort()
print(f"Lista em ordem crescente: {lista}")
